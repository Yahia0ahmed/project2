from highrise import BaseBot
from highrise.models import SessionMetadata, User, Item, Literal, ChatEvent

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        pass
    async def on_user_join(self, user: User) -> None:
        await self.highrise.chat(f"نورت الروم يا مز✨ {user.username}!")
    username_to_id = {}
    print("pass 1")
    async def on_chat(self, user: User, message: str) -> None:    
        if message.startswith("tele"):
            user_list = await self.highrise.get_room_users()
            for users, _ in user_list:
                self.username_to_id[users.username] = users.id
            parts = message.split()
            if len(parts) > 3:
                print("pass 2")
                await self.highrise.chat("تنسيق النقل الأنى غير صحيحة !")
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
                    print("pass 3")
                    await self.highrise.chat("تنسيق احداثيات غير صحيح !")
                    return
                user_id = self.username_to_id[username]
            elif len(parts) == 2:
                try:
                    coords = parts[1].split(',')
                    x, y, z = map(float, coords)
                    v
                except ValueError:
                    await self.highrise.chat("تنسيق احداثيات غير صحيح !.")
                    return
                user_id = user_id
            await self.highrise.teleport(user_id, (x, y, z))
            await self.highrise.chat(f"{user.username} تم نقله الى ({x}, {y}, {z})")
