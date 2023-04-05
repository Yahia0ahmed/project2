from highrise import BaseBot
from highrise.models import SessionMetadata, User, Item, ChatEvent

class Bot(BaseBot):
  async def on_start(self, session_metadata: SessionMetadata) -> None:
    pass
  