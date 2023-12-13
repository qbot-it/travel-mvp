from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dto.search import Search
from ...auth.dependencies.jwt_auth import auth_jwt
from ...task.dto.task import Task
from ...task.exceptions.active_task_exists import ActiveTaskExistsException
from ...task.services.task_service import TaskService
from ...user.exceptions.user_not_found import UserNotFoundException
from ...user.services.user_service import UserService
from ....db.database import get_session

router = APIRouter(prefix='/api/v1/trips')


@router.post("/search", tags=["trip"])
def search(dto: Search, user_id=Depends(auth_jwt), db: Session = Depends(get_session)):
    try:
        user_service = UserService(db)
        user = user_service.get_user(user_id)
        task_service = TaskService(db)
        task = task_service.create_trip_search_task(user, dto)

        return Task(id=str(task.id), type=task.type.value, result=task.result, status=task.status)
    except UserNotFoundException as e:
        raise HTTPException(404, detail=e.message)
    except ActiveTaskExistsException as e:
        raise HTTPException(409, detail=e.message)


