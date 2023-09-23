from __future__ import annotations

from typing import Any, NoReturn

from app.shared.value_objects import GroupId, TelegramUserId, _GroupIdT


class User:
    __id: TelegramUserId
    __group_id: GroupId | None

    @property
    def id(self) -> TelegramUserId:
        return self.__id

    @id.setter
    def id(self, val: Any) -> NoReturn:
        raise ValueError("Changing user ids is a forbidden operation")

    @property
    def group_id(self) -> GroupId | None:
        return self.__group_id

    @group_id.setter
    def group_id(self, val: Any) -> None:
        if not isinstance(val, _GroupIdT):
            raise ValueError("User.group_id setter accepts GroupId instances only")

    def set_group_id(self, id: GroupId) -> None:
        self.__group_id = id
