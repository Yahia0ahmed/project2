from highrise import BaseBot
from highrise.models import SessionMetadata, User, Item

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        await self.highrise.walk_to([5,0,5],'Frontright')
        pass
    async def on_user_join(self, user: User) -> None:
        await self.highrise.chat(f"ولكم نورت الروم{user.username}!")
    async def on_tip(self, sender: User, receiver: User, tip: Item) -> None:
        await self.highrise.chat(f"{sender.username} تبرع الى {receiver.username} {tip.amount} قولد")