import pydantic


class JoinRoomRequest(pydantic.BaseModel):
  code: str
