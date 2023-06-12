from abc import abstractmethod
from uuid import UUID
from fastAPI_project.db.models.base_model import GroupModel


class GroupPersistence:
    @abstractmethod
    def save(self, name: str, number: str) -> GroupModel:
        ...

    @abstractmethod
    def get_by_id(self, group_id: UUID):
        ...
