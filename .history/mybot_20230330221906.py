from highrise import BaseBot
from highrise.models import SessionMetadata, User, Item

class Bot(BaseBot):
  async def on_start(self, session_metadata: SessionMetadata) -> None:
    pass
  
    await self.highrise.chat(f"نورتي الروم يا روح يحيى❤ {user.username}!")
async def teleport(self, user: User) -> None:
  pass