from ast import literal_eval
from highrise import BaseBot
from highrise.models import SessionMetadata, User, Item

class Bot(BaseBot):
  async def on_start(self, session_metadata: SessionMetadata) -> None:
    pass
  async def on_user_join(self, user: User) -> None:
    await self.highrise.chat(f"نورتي الروم يا روح يحيى❤ {user.username}!")
async def walk_to(self,dest: tuple[7, 0, 0],facing: ["FrontRight") -> None:
      pass
      await self.ws.send_json({"_type": "FloorHitRequest", "destination": dest, "facing": facing})