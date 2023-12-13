from time import sleep
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from ....db.database import engine
from .handlers.search_task_handler import SearchTaskHandler
from .handlers.upload_task_handler import UploadTaskHandler
from ..models.task import Task
from ..vo.status import Status
from ..vo.type import Type
from ...image.services.descriptor_builder import DescriptorBuilder


class TaskRunner:
    __db: Session
    __upload_task_handler: UploadTaskHandler
    __search_task_handler: SearchTaskHandler

    def run(self):
        session_factory = sessionmaker(bind=engine)
        session = scoped_session(session_factory)

        self.__db = session()
        self.__upload_task_handler = UploadTaskHandler(self.__db, DescriptorBuilder())
        self.__search_task_handler = SearchTaskHandler(self.__db)

        while True:
            tasks: list = self.__db.query(Task).where(Task.status == Status.PENDING).all()
            for task in tasks:
                try:
                    self.__run_task(task)
                except Exception as e:
                    print(e)
            sleep(10)

    def __run_task(self, task: Task):
        if task.status.PENDING:
            if task.type == Type.UPLOAD:
                self.__upload_task_handler.handle(task)
            elif task.type == Type.SEARCH:
                self.__search_task_handler.handle(task)
