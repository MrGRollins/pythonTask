from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from fastAPI_project.db.models.group import GroupModel


class StudentModel(SQLModel, table=True):

    __tablename__ = "student"

    id: Optional[int] = Field(
        primary_key=True,
        default=None
    )

    first_name: str = Field(
        max_length=100,
        unique=False
    )

    last_name: str = Field(
        max_length=100,
        unique=False
    )

    age: int = Field(
        max_length=100,
        unique=False
    )

    group_id: Optional[int] = Field(
        default=None,
        foreign_key="group.id"
    )

    group: Optional[GroupModel] = Relationship(
        back_populates="students"
    )