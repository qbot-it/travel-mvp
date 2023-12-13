from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dto.task import Task
from ..exceptions.task_not_found import TaskNotFoundException
from ..services.task_service import TaskService
from ...auth.dependencies.jwt_auth import auth_jwt
from ...user.exceptions.user_not_found import UserNotFoundException
from ...user.services.user_service import UserService
from ....db.database import get_session

router = APIRouter(prefix='/api/v1/tasks')


@router.get("/active", tags=["tasks"], name='active tasks')
def active_tasks(user_id=Depends(auth_jwt), db: Session = Depends(get_session)) -> list:
    try:
        user_service = UserService(db)
        user = user_service.get_user(user_id)
        task_service = TaskService(db)
        tasks = task_service.get_user_active_tasks(user)

        return list(map(lambda task:
                        Task(id=str(task.id), type=task.type.value, status=task.status.value, result=task.result),
                        tasks))

    except UserNotFoundException as e:
        raise HTTPException(404, detail=e.message)


@router.get("/{id}", tags=["tasks"], name='task')
def get_task(id: str, user_id=Depends(auth_jwt), db: Session = Depends(get_session)) -> Task:
    try:
        user_service = UserService(db)
        user = user_service.get_user(user_id)
        task_service = TaskService(db)
        task = task_service.get_user_task(user, id)

        return Task(id=str(task.id), type=task.type.value, status=task.status.value, result=task.result)
    except (UserNotFoundException, TaskNotFoundException) as e:
        raise HTTPException(404, detail=e.message)
