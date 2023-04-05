from highrise import BaseBot
from highrise.models import SessionMetadata, User, Item

class Bot(BaseBot):
  async def on_start(self, session_metadata: SessionMetadata) -> None:
    pass
  async def on_user_join(self, user: User) -> None:
    await self.highrise.chat(f"ولكم ابو تيز {user.username}!")
    highrise mybot:Bot '63b0936f790b0b47e4380222' '58e4643695d301aec51df7db1f1e5afabd9817e4b2de57d86c5602a36cecc166'
    