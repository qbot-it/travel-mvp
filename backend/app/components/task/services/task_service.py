from typing import List, Type
from fastapi import UploadFile
from sqlalchemy.orm import Session
from ...config import settings
from ..exceptions.active_task_exists import ActiveTaskExistsException
from ..exceptions.task_not_found import TaskNotFoundException
from ..models.task import Task
from ..vo.status import Status
from ..vo.type import Type as TaskType
from ...trip.dto.search import Search
from ...user.models.user import User
from cryptography.fernet import Fernet
import base64


class TaskService:
    __db: Session
    __fernet: any

    def __init__(self, db: Session):
        self.__db = db
        self.__fernet = Fernet(settings.encryption_secret_key)

    def create_image_upload_task(self, user: User, files: List[UploadFile]) -> Task:
        """
        :raises ActiveTaskExistsException
        """

        active_task = self.get_user_active_task(user, TaskType.UPLOAD)

        if isinstance(active_task, Task):
            raise ActiveTaskExistsException()

        images = []
        for file in files:
            try:
                file_bytes = file.file.read()
                images.append(base64.b64encode(self.__fernet.encrypt(file_bytes)).decode('ASCII'))
            finally:
                file.file.close()

        task = Task()
        task.user_id = user.id
        task.type = TaskType.UPLOAD
        task.status = Status.PENDING
        task.data = images

        self.__db.add(task)
        self.__db.commit()
        self.__db.refresh(task)

        return task

    def create_trip_search_task(self, user: User, search: Search) -> Task:
        """
        :raises ActiveTaskExistsException
        """

        active_search_task = self.get_user_active_task(user, TaskType.SEARCH)
        active_upload_task = self.get_user_active_task(user, TaskType.UPLOAD)

        if isinstance(active_search_task, Task):
            raise ActiveTaskExistsException()

        task = Task()
        task.user_id = user.id
        task.type = TaskType.SEARCH
        task.status = Status.PENDING
        task.data = search.to_json()

        if isinstance(active_upload_task, Task):
            task.depends_on_id = active_upload_task.id

        self.__db.add(task)
        self.__db.commit()
        self.__db.refresh(task)

        return task

    def get_user_task(self, user: User, task_id: str) -> Task:
        """
        :raises TaskNotFoundException
        """

        task: Task | None = (self.__db.query(Task)
                             .where(Task.user_id == str(user.id))
                             .where(Task.id == task_id)
                             .first())

        if not isinstance(task, Task):
            raise TaskNotFoundException()

        return task

    def get_task(self, task_id: str) -> Task:
        """
        :raises TaskNotFoundException
        """

        task: Task | None = (self.__db.query(Task)
                             .where(Task.id == task_id)
                             .first())

        if not isinstance(task, Task):
            raise TaskNotFoundException()

        return task

    def get_user_active_tasks(self, user: User) -> list[Type[Task]]:
        return (self.__db.query(Task)
                .where(Task.user_id == str(user.id))
                .where(Task.status != Status.FINISHED).all())

    def get_user_active_task(self, user: User, task_type: TaskType) -> Task | None:
        return (self.__db.query(Task)
                .where(Task.user_id == str(user.id))
                .where(Task.type == task_type)
                .where(Task.status != Status.FINISHED).first())

    def get_active_tasks(self) -> list[Type[Task]]:
        return (self.__db.query(Task)
                .where(Task.status != Status.FINISHED).all())

    def update_task(self, task: Task) -> Task:
        db_task = self.get_task(str(task.id))
        db_task.status = task.status
        db_task.data = task.data
        db_task.result = task.result
        db_task.depends_on_id = db_task.depends_on_id
        self.__db.commit()
        self.__db.refresh(db_task)

        return task
