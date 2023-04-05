from ast import literal_eval
from highrise import BaseBot
from highrise.models import SessionMetadata, User, Item, ChatEvent

class Bot(BaseBot):
  async def on_start(self, session_metadata: SessionMetadata) -> None:
    pass
  async def on_user_join(self, user: User) -> None:
    await self.highrise.chat(f"نورتي الروم يا روح يحيى❤ {user.username}!")
async def teleport(sel)
