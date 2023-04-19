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
        pass
    async def on_tip(self, sender: User, receiver: User, tip: Item) -> None:
        await self.highrise.chat(f"{sender.username} gived {tip.amount} gold to {receiver.username}!")
    async def get_wallet(self) -> GetWalletRequest.GetWalletResponse | Error :
        pass
    async def on_chat(self, user: User, message: str) -> None:
        if message.startswith('k'):
            msg = await self.highrise.get_wallet()
            print(msg)
    async def on_user_join(self, user: User) -> None:
        await self.highrise.get_room_users()
    async def on_chat(self, user: User, message: str) -> None:
        if message.startswith('‎'):
            await self.highrise.teleport(user.id,Position(6,10.75,3))
    username_to_id = {}
    async def on_chat(self, user: User, message: str) -> None:    
        if message.startswith("‎"):
            user_list = (await self.highrise.get_room_users()).content
            for users, _ in user_list:
                self.username_to_id[users.username] = users.id
            parts = message.split()
            if len(parts) > 3:
                await self.highrise.chat("تنسيق امر نقل غير صحيح")
                return
            elif len(parts) == 3:
                username = parts[1][1:]
                if username not in self.username_to_id:
                    await self.highrise.chat("لم يتم العثور على اللاعب")
                    return
                try:
                    coords = parts[2].split(',')
                    x, y, z = map(float, coords)
                except ValueError:
                    await self.highrise.chat("تنسيق احداثيات غير صحيح")
                    return
                user_id = self.username_to_id[username]
            elif len(parts) == 2:
                try:
                    coords = parts[1].split(',')
                    x, y, z = map(float, coords)
                except ValueError:
                    await self.highrise.chat("تنسيق احداثيات غير صحيح")
                    return
            user_id = user.id
            await self.highrise.teleport(user_id, (x, y, z))
            await _do_req_no_resp(self, TeleportRequest(user_id, dest))
            await self.highrise.chat(f"{user.username} has been teleported to ({x}, {y}, {z})")
        