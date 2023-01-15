from unittest.mock import Mock, patch
import pytest
from caronte_infra.database.connection.mongo_connection import MongoConnection


class TestMongoConnection:
    @patch("caronte_infra.database.connection.mongo_connection.AsyncIOMotorClient")
    @pytest.mark.asyncio
    async def test_should_connect_to_dabase_using_the_correct_database_name(
        self, mock_motor: Mock
    ):
        mock_collection = Mock(name="Collection")
        mock_motor.return_value = {"test": mock_collection}

        instance = MongoConnection(
            user="unit_test",
            pwd="123test",
            host="localhost",
            port=27017,
            db_name="test",
        )
        callback = await instance.execute()

        mock_motor.assert_called_once_with(
            "mongodb://unit_test:123test@localhost:27017"
        )
        mock_collection.assert_not_called()
        assert callback == mock_collection
