from highrise import BaseBot
from highrise.models import SessionMetadata, User, Item, Literal

class Bot(BaseBot):
  async def on_start(self, session_metadata: SessionMetadata) -> None:
    pass
  async def on_user_join(self, user: User) -> None:
    await self.highrise.chat(f"نورتي الروم يا روح يحيى❤ {user.username}!")
async def walk_to(self, dest: tuple[float, float, float],facing: Literal["FrontRight", "FrontLeft", "BackRight", "BackLeft"],) -> None:
 await self.highrise.walk_to([7,0,0],'FrontRight')
 