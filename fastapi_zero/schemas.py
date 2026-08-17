from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class Sobre(BaseModel):
    nome: str
    versao: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    username: str
    email: EmailStr
    id: int


class UserDB(UserSchema):
    id: int
