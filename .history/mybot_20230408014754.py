from highrise import BaseBot
from highrise.models import SessionMetadata, User, Item, GetWalletRequest, Error, Position, ChatRequest, Reaction
class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        await self.highrise.walk_to(Position(6,2.5,0,"FrontRight"))
        pass
    async def on_chat(self, user: User, message: str) -> None:
        pass
    async def on_user_join(self, user: User) -> None:
        await self.highrise.chat(f"نورت مزاد النخبة 🔥{user.username}!")
    async def on_tip(self, sender: User, receiver: User, tip: Item) -> None:
        await self.highrise.chat(f"{sender.username} gived {tip.amount} gold to {receiver.username}!")
    async def get_wallet(self) -> GetWalletRequest.GetWalletResponse | Error :
        pass
    async def on_chat(self, user: User, message: str) -> None:
        if message.startswith('k'):
            msg = await self.highrise.get_wallet()
            print(msg)
    
    async def on_chat(self, user: User, message: str) -> None:
        if message.startswith('‎'):
            await self.highrise.teleport(user.id,Position(6,10.75,3))
    async def on_whisper(self, user: User, message: str) -> None:
            await self.highrise.send_whisper(self: )