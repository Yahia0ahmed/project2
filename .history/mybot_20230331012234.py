from highrise import BaseBot
from highrise.models import SessionMetadata, User, Item, Literal, ChatEvent

class Bot(BaseBot):
  async def on_start(self, session_metadata: SessionMetadata) -> None:
    pass
  
   await self.highrise.walk_to([7,0,0],'FrontRight')
  async def on_user_join(self, user: User) -> None:
    await self.highrise.chat(f"نورتي الروم يا روح يحيى❤ {user.username}!")


 