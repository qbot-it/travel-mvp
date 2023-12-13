import hashlib
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from .descriptor_builder import DescriptorBuilder
from ..dto.descriptor import Descriptor
from ..models.image import Image
from ...user.models.user import User


class ImageService:
    __db: Session

    def __init__(self, db: Session):
        self.__db = db

    def create(self, user: User, builder: DescriptorBuilder, image_bytes_list: list):
        for image_bytes in image_bytes_list:
            try:
                descriptor = builder.build(image_bytes)
                self.__create(user, descriptor)
            except Exception as e:
                pass

    def __create(self, user: User, descriptor: Descriptor):
        try:
            value_to_hash = f"{user.id}#{descriptor.text}"
            image = Image()
            image.user_id = user.id
            image.descriptor = descriptor.to_json()
            image.hash = hashlib.sha256(value_to_hash.encode('utf-8')).hexdigest()
            self.__db.add(image)
            self.__db.commit()
            self.__db.refresh(image)
        except IntegrityError:
            self.__db.rollback()

    def drop(self, user: User):
        for image in user.images:
            self.__db.delete(image)
        self.__db.commit()
