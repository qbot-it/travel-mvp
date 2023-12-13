from sqlalchemy.orm import Session
from ...models.task import Task
from ..task_service import TaskService
from ...dto.result import Result
from ...vo.status import Status
from ....trip.dto.search import Search
from ....trip.services.trip_service import TripService


class SearchTaskHandler:
    __trip_service: TripService
    __task_service: TaskService

    def __init__(self, db: Session):
        self.__trip_service = TripService()
        self.__task_service = TaskService(db)

    def handle(self, task: Task):
        super_task: Task | None = task.depends_on
        if task.status.PENDING and (super_task is None or super_task.status == Status.FINISHED):
            task.status = Status.RUNNING
            self.__task_service.update_task(task)
            search_dto = Search.from_json(task.data if task.data is not None else {})
            trips = self.__trip_service.find_trips(task.user, search_dto)
            task.status = Status.FINISHED
            task.result = Result(trips=trips).to_json()
            self.__task_service.update_task(task)
