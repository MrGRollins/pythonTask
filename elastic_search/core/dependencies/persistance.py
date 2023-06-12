from typing import Generator
from fastapi import Depends
from sqlmodel import Session
from elastic_search.core.db_config import DB_ENGINE
from elastic_search.persistence.common import ShopPersistence
from elastic_search.persistence.postgress import PostgresShopPersistence


def session_dependecy() -> Generator[Session, None, None]:
    with Session(DB_ENGINE) as session:
        yield session

def shop_persistence_dependency(session: Session = Depends(session_dependecy)) -> ShopPersistence:
    return PostgresShopPersistence(session=session)