from fastapi import Depends
from sqlmodel import Session
from fastAPI_project.core.db_config import DB_ENGINE
from fastAPI_project.persistence.common import GroupPersistence
from fastAPI_project.persistence.postgres import PostgresGroupPersistence
from typing import Generator

def session_dependency() -> Generator[Session, None, None]:
    with Session(DB_ENGINE) as session:
        yield session

def group_persistence_dependency(session: Session = Depends()) -> GroupPersistence:
    return PostgresGroupPersistence(session=session)