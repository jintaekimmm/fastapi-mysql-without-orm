from pydantic.main import BaseModel


class Tweet(BaseModel):
    user_id: int
    tweet: str
