from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..services.image_service import ImageService
from ...auth.dependencies.jwt_auth import auth_jwt
from ...task.dto.task import Task
from ...task.exceptions.active_task_exists import ActiveTaskExistsException
from ...task.services.task_service import TaskService
from ...user.exceptions.user_not_found import UserNotFoundException
from ...user.services.user_service import UserService
from ....db.database import get_session

router = APIRouter(prefix='/api/v1/images')


@router.post("", tags=["image"])
def upload(user_id=Depends(auth_jwt), files: List[UploadFile] = File(),
           db: Session = Depends(get_session)):
    try:
        user_service = UserService(db)
        task_service = TaskService(db)
        user = user_service.get_user(user_id)
        task = task_service.create_image_upload_task(user, files)

        return Task(id=str(task.id), type=task.type.value, result=task.result, status=task.status)
    except UserNotFoundException as e:
        raise HTTPException(404, detail=e.message)
    except ActiveTaskExistsException as e:
        raise HTTPException(409, detail=e.message)


@router.delete("", tags=["image"])
def delete(user_id=Depends(auth_jwt), db: Session = Depends(get_session)):
    try:
        user_service = UserService(db)
        image_service = ImageService(db)
        user = user_service.get_user(user_id)
        image_service.drop(user)

        return {"message": "Successfully deleted"}
    except UserNotFoundException as e:
        raise HTTPException(404, detail=e.message)
