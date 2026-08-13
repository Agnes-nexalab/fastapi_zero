from pydantic import BaseModel


class Message(BaseModel):
    message: str


class Sobre(BaseModel):
    nome: str
    versao: str
