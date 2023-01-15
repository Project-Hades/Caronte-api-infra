from typing import Awaitable, Generic, Literal, TypeVar

from caronte_common.interfaces.command import AsyncCommand
from caronte_common.interfaces.factory import AsyncFactory

from caronte_infra.database.connection.mongo_connection import MongoConnection
from caronte_infra.database.connection.redis_connection import RedisConnection
from caronte_infra.errors.database import UndefinedDatabaseException

Tr = TypeVar("Tr")


class ConnectionFactory(
    AsyncFactory[AsyncCommand[Tr], Literal["redis", "mongo"]], Generic[Tr]
):
    def __init__(self, user: str, pwd: str, host: str, port: int, db_name: str) -> None:
        self.redis = RedisConnection(
            user=user, pwd=pwd, host=host, port=port, db_name=db_name
        )
        self.mongo = MongoConnection(
            user=user, pwd=pwd, host=host, port=port, db_name=db_name
        )

    async def manufacture(
        self, object_key: Literal["redis", "mongo"]
    ) -> Awaitable[AsyncCommand[Tr]]:
        if object_key == "redis":
            return self.redis
        elif object_key == "mongo":
            return self.mongo
        else:
            raise UndefinedDatabaseException(
                error="Please use redis or mongo as database"
            )
