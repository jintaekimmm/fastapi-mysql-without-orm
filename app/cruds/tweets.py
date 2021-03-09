from datetime import datetime

from app.core.db import database
from app.schemas.tweets import Tweet


async def get_all_tweet():
    query = "SELECT * FROM tweets"
    data = await database.fetch_all(query)

    return [{**i} for i in data]


async def get_user_tweets(user_id: int):
    query = f"SELECT id, user_id, tweet, created_at FROM tweets WHERE user_id={user_id}"
    data = await database.fetch_all(query)

    return data


async def get_tweets(tweet_id: int):
    query = f"SELECT id, user_id, tweet, created_at FROM tweets WHERE id={tweet_id}"
    data = await database.fetch_one(query)

    return data


async def insert_tweets(tweet: Tweet):
    created_at = datetime.today()
    values = {"user_id": tweet.user_id, "tweet": tweet.tweet, "created_at": created_at}

    query = "INSERT INTO tweets(user_id, tweet, created_at) VALUES (:user_id, :tweet, :created_at)"
    insert_id = await database.execute(query=query, values=values)

    return await get_tweets(insert_id)
