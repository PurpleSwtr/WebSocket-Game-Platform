from sqlmodel import Field, SQLModel


class Player(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
