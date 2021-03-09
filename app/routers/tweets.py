from fastapi import APIRouter
from app.cruds.tweets import get_user_tweets, insert_tweets, get_all_tweet
from app.schemas.tweets import Tweet

router = APIRouter()


@router.get("/tweets/", tags=["tweet"])
async def read_tweets():
    tweet_list = await get_all_tweet()

    return tweet_list


@router.get("/tweets/{user_id}", tags=["tweet"])
async def read_tweet(user_id: int):
    tweet = await get_user_tweets(user_id)

    return tweet


@router.post("/tweets/{user_id}", tags=["tweet"])
async def create_tweet(tweet: Tweet):
    res = await insert_tweets(tweet)

    return res
