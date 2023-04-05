from highrise import BaseBot
from highrise.models import SessionMetadata, User, Item

class Bot(BaseBot):
  async def on_start(self, session_metadata: SessionMetadata) -> None:
    pass
  async def on_user_join(self, user: User) -> None:
    await self.highrise.chat(f"نورتي الروم يا روح يحيى❤ {user.username}!")
    if self.highrise.send_whisper(: str, message: str) -> Coroutine[Any, Any, None]