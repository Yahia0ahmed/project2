from highrise import BaseBot
from highrise.models import SessionMetadata, User, Item, GetWalletRequest, Error, Position, ChatRequest
class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        await self.highrise.walk_to(Position(6,2.5,0,"FrontRight"))
        pass
    async def on_user_join(self, user: User) -> None:
        await self.highrise.chat(f"نورت مزاد النخبة 🔥 {user.username}!")
    async def on_tip(self, sender: User, receiver: User, tip: Item) -> None:
        await self.highrise.chat(f"{sender.username} gived {tip.amount} gold to {receiver.username}!")
    async def get_wallet(self) -> GetWalletRequest.GetWalletResponse | Error :
        await self.highrise.get_wallet()
        print(wallet)