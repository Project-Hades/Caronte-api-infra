from typing import Awaitable

from caronte_common.interfaces.command import AsyncCommand
from redis.asyncio.client import Redis


class RedisConnection(AsyncCommand[Redis]):
    def __init__(self, user: str, pwd: str, host: str, port: int, db_name: str) -> None:
        self.host = host
        self.port = port
        self.pwd = pwd
        self.user = user
        self.db_name = db_name

    async def execute(self) -> Awaitable[Redis]:
        return Redis(
            host=self.host,
            port=self.port,
            password=self.pwd,
            db=self.db_name,
            username=self.user,
        )


class RedisCloseConnection(AsyncCommand[None]):
    def __init__(self, connection: Redis) -> None:
        self.connection = connection

    async def execute(self) -> Awaitable[None]:
        await self.connection.close()
