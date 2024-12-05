from pydantic import BaseModel
from typing import List, Optional

class MovieModel(BaseModel):
  title: str
  cover_image: str
  gender: List[str]

class UserModel(BaseModel):
  name: str
  email: str
  password: str
  date_of_birth: str