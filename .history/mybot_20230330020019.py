from highrise import BaseBot
from highrise.models import SessionMetadata, User, Item, TipReactionEvent

class Bot(BaseBot):
  async def on_start(self, session_metadata: SessionMetadata) -> None:
    pass
  async def on_user_join(self, user: User) -> None:
    await self.highrise.chat(f"ولكم نورت الروم✨ {user.username}!")
    
    async def on_tip(self, sender: User, receiver: User, tip: int) -> None:
     await self.highrise.chat(f"شكرا {sender.username} للتبرع {tip.amount} الى {receiver.username}!")