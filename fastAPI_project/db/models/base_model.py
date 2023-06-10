from pydantic import BaseModel


class GroupModel(BaseModel):
    id: int
    name: str
    number: str

class StudentModel(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
