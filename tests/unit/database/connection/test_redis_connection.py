from unittest.mock import Mock, patch

import pytest

from caronte_infra.database.connection.redis_connection import RedisConnection


class TestRedisConnection:
    @patch("caronte_infra.database.connection.redis_connection.Redis")
    @pytest.mark.asyncio
    async def test_should_connect_to_dabase_using_the_correct_database_name(
        self, mock_redis: Mock
    ):
        mock_connection = Mock(name="Connection")
        mock_redis.return_value = mock_connection
        instance = RedisConnection(
            user="unit_test",
            pwd="123test",
            host="localhost",
            port=27017,
            db_name="test",
        )
        callback = await instance.execute()

        mock_redis.assert_called_once_with(
            username="unit_test",
            password="123test",
            host="localhost",
            port=27017,
            db="test",
        )
        assert callback == mock_connection
