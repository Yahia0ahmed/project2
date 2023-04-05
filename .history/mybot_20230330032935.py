from highrise import BaseBot
from highrise.models import SessionMetadata, User, Item

class Bot(BaseBot):
  async def on_start(self, session_metadata: SessionMetadata) -> None:
    pass
  async def on_user_join(self, user: User) -> None:
    await self.highrise.chat(f"ولكم نورت الروم✨ {user.username}!") 
async def chat(self, message: str) -> None:
        """Broadcast a room-wide chat message."""
        await self.ws.send_json({"_type": "السلام عليكم", "و عليكم السلام": message})