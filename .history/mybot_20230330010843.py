from highrise import BaseBot
from highrise.models import SessionMetadata, User, Item

class Bot(BaseBot):
  async def on_start(self, session_metadata: SessionMetadata) -> None:
    pass
  async def on_user_join(self, user: User) -> None:
    await self.highrise.chat(f"ولكم نورت الروم✨ {user.username}!")
    async def tip_reaction_event -> None:
      await self.highrise.walk_to(dest: tuple[6.0, 0])