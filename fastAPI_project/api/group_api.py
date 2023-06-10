from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from pydantic.schema import List
from sqlalchemy.orm import Session
from fastAPI_project.db.models.base_model import GroupModel
from fastAPI_project.dependencies.persistence import group_persistence_dependency


router = APIRouter()

# Создать группу
@router.post("/", summary="Create Group", description="Create group for students")
def create_group(group: GroupModel, session: Session = Depends(group_persistence_dependency)):
    db_group = GroupModel(
        name=group.name,
        number=group.number
    )
    session.add(db_group)
    session.commit()
    session.refresh(db_group)
    return db_group

# Получить информацию о группе по ее id
@router.get("/groups/{group_id}")
def get_group(group_id: int, session: Session = Depends(group_persistence_dependency)):
    group = session.query(GroupModel).get(group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group

# Удалить группу
@router.delete("/groups/{group_id}")
def delete_group(group_id: int, session: Session = Depends(group_persistence_dependency)):
    group = session.query(GroupModel).get(group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    session.delete(group)
    session.commit()
    return {"message": "Group deleted"}

# Получить список групп
@router.get("/groups", response_model=List[GroupModel])
def get_groups(session: Session = Depends(group_persistence_dependency)):
    groups = session.query(GroupModel).all()
    return groups