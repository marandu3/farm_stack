from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(..., title="User ID", description="Unique identifier for the user")
    username: str = Field(..., title="Username", description="Username of the user")
    