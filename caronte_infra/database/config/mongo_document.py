from __future__ import annotations

from typing import Awaitable

from caronte_common.data.db_document import Document
from caronte_common.interfaces.command import AsyncCommand
from pymongo.collection import Collection

from caronte_infra.errors.database import UndefinedFieldConfiguration


class MongoConfigDocument(AsyncCommand[None]):
    def __init__(self, database: Collection, document: Document[Collection]) -> None:
        self.document = document
        self.document.instance = database.get_collection(
            self.document.name, **self.document.config
        )

    async def execute(self) -> Awaitable[None]:
        for field_config in self.document.field_config:
            if field_config.config_type == "create_index":
                await self.document.instance.create_index(
                    field_config.field_name, **field_config.params
                )
            else:
                raise UndefinedFieldConfiguration(
                    error="There are avaible this configurations: create_index"
                )
