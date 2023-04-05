from highrise import BaseBot
from highrise.models import SessionMetadata, User, Item, Literal, ChatEvent

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
    async def walk_to(self, dest: tuple[float, float, float],facing: Literal["FrontRight", "FrontLeft", "BackRight", "BackLeft"],) -> None:
          await self.highrise.walk_to([0,0,0],'FrontRight')
          pass
    