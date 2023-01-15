from unittest.mock import Mock, patch
import pytest

from caronte_infra.database.factory.connection import ConnectionFactory
from caronte_infra.errors.database import UndefinedDatabaseException


class TestConnectionFactory:
    mock_connection: Mock
    instance: ConnectionFactory

    def setup_method(self):
        self.mock_connection = Mock(name="Connection")
        self.instance = ConnectionFactory(
            user="unit_test",
            pwd="123test",
            host="localhost",
            port=27017,
            db_name="test",
        )

    @patch("caronte_infra.database.factory.connection.MongoConnection")
    @patch("caronte_infra.database.factory.connection.RedisConnection")
    @pytest.mark.asyncio
    async def test_should_manufacture_redis_connection(
        self, mock_redis: Mock, mock_mongo: Mock
    ):
        mock_redis.return_value = self.mock_connection

        callback = await self.instance.manufacture("redis")

        assert callback == self.mock_connection
        mock_mongo.assert_not_called()
        mock_redis.assert_called_once_with(
            user="unit_test",
            pwd="123test",
            host="localhost",
            port=27017,
            db_name="test",
        )

    @patch("caronte_infra.database.factory.connection.MongoConnection")
    @patch("caronte_infra.database.factory.connection.RedisConnection")
    @pytest.mark.asyncio
    async def test_should_manufacture_mongo_connection(
        self, mock_redis: Mock, mock_mongo: Mock
    ):
        mock_mongo.return_value = self.mock_connection

        callback = await self.instance.manufacture("mongo")

        assert callback == self.mock_connection
        mock_redis.assert_not_called()
        mock_mongo.assert_called_once_with(
            user="unit_test",
            pwd="123test",
            host="localhost",
            port=27017,
            db_name="test",
        )

    @patch("caronte_infra.database.factory.connection.MongoConnection")
    @patch("caronte_infra.database.factory.connection.RedisConnection")
    @pytest.mark.asyncio
    async def test_should_manufacture_raise_undefined_database_exception(
        self, mock_redis: Mock, mock_mongo: Mock
    ):
        mock_mongo.return_value = self.mock_connection

        with pytest.raises(UndefinedDatabaseException):
            await self.instance.manufacture("not defined db")

        mock_redis.assert_not_called()
        mock_mongo.assert_not_called()
