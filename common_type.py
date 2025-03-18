from typing import TypeVar, Protocol
class Model(Protocol):
    __tablename__:str
    id:int



Model = TypeVar("Model",bound=Model)