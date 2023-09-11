from typing import Optional
from sqlmodel import Field, SQLModel

class Campaign(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    party: str

if __name__ == "__main__":
    