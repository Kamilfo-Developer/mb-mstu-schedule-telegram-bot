from typing import NewType

TelegramUserId = NewType("TelegramUserId", int)

# isinstance never likes NewType instances so this compromise takes place
_GroupIdT = int
GroupId = NewType("GroupId", _GroupIdT)
