import time
import asyncio
from highrise import BaseBot
from highrise.models import SessionMetadata, User, Item, GetWalletRequest, Error, Position, ChatRequest, Reaction
class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        await self.highrise.walk_to(Position(6,2.5,0,"FrontRight"))
        pass
    async def on_chat(self, user: User, message: str) -> None:
        pass
    async def on_user_join(self, user: User) -> None:
        await self.highrise.chat(f"نورت مزاد النخبه 💸 {user.username}")
        if user.username == "Sszm":
         await self.highrise.chat("نورتي الروم يا مزة 🤭")
    async def on_tip(self, sender: User, receiver: User, tip: Item) -> None:
        await self.highrise.chat(f"{sender.username} gived {tip.amount} gold to {receiver.username}!")
    async def get_wallet(self) -> GetWalletRequest.GetWalletResponse | Error :
        pass
    async def on_chat(self, user: User, message: str) -> None:
        if message.startswith('k'):
            msg = await self.highrise.get_wallet()
            print(msg)
    username_to_id = {}
    async def on_chat(self, user: User, message: str) -> None:    
        if message.startswith("‎"):
            parts = message.split()
            room_users = (await self.highrise.get_room_users()).content
            for users, pos in room_users:
                self.username_to_id[users.username] = users.id
            if len(parts) > 3:
                await self.highrise.chat("Invalid teleport command format.")
                return
            elif len(parts) == 3:
                username = parts[1][1:]
                if username not in self.username_to_id:
                    await self.highrise.chat("User not found.")
                    return
                try:
                    coords = parts[2].split(',')
                    x, y, z = map(float, coords)
                except ValueError:
                    await self.highrise.chat("Invalid coordinates format.")
                    return
                user_id = self.username_to_id[username]
            elif len(parts) == 2:
                try:
                    coords = parts[1].split(',')
                    x, y, z = map(float, coords)
                except ValueError:
                    await self.highrise.chat("Invalid coordinates format.")
                    return
                user_id = user.id
            elif len(parts) < 2:
                await self.highrise.chat("Invalid teleport command format.")
                return
            await self.highrise.teleport(user_id, Position(x, y, z))
            pass
    async def messageLoop(self):
        while True:
        await self.highrise.chat("This message will be sent every 30 seconds")
        await asyncio.sleep(30)
        asyncio.create_task(self.messageLoop())