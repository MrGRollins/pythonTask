from uuid import UUID
from sqlmodel import Session
from fastAPI_project.db.models.base_model import GroupModel
from fastAPI_project.persistence.common import GroupPersistence


class PostgresGroupPersistence(GroupPersistence):
    def __init__(self, session: Session):
        self.__session = session

    def save(self, name: str, number: str) -> GroupModel:
        group_model = GroupModel(name=name, number=number)
        self.__session.add(group_model)
        self.__session.commit()
        return GroupModel(id=group_model.id, name=group_model.name, number=group_model.number)

    def get_by_id(self, group_id: UUID):
        ...

