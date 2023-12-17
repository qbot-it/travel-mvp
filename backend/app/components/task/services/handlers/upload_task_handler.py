from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Session
from ...models.task import Task
from ..task_service import TaskService
from ...vo.status import Status
from ....config import settings
from ....image.services.descriptor_builder import DescriptorBuilder
from ....image.services.image_service import ImageService
from cryptography.fernet import Fernet
import base64


class UploadTaskHandler:
    __image_service: ImageService
    __descriptor_builder: DescriptorBuilder
    __task_service: TaskService
    __fernet: Fernet

    def __init__(self, db: Session, descriptor_builder: DescriptorBuilder):
        self.__image_service = ImageService(db)
        self.__descriptor_builder = descriptor_builder
        self.__task_service = TaskService(db)
        self.__fernet = Fernet(settings.encryption_secret_key)

    def handle(self, task: Task):
        super_task: Task | None = task.depends_on
        if task.status.PENDING and (super_task is None or super_task.status == Status.FINISHED):
            task.status = Status.RUNNING
            self.__task_service.update_task(task)

            images = []
            for token in task.data:
                try:
                    image_bytes = self.__fernet.decrypt(base64.b64decode(token))
                    images.append(image_bytes)
                except Exception as e:
                    print(e)

            self.__image_service.create(task.user, self.__descriptor_builder, images)
            task.status = Status.FINISHED
            task.data = JSONB.NULL
            self.__task_service.update_task(task)
