from highrise import BaseBot
from highrise.models import SessionMetadata, User, Item, Literal, ChatEvent

class Bot(BaseBot):
  async def on_start(self, session_metadata: SessionMetadata) -> None:
    pass
  async def on_user_join(self, user: User) -> None:
    await self.highrise.chat(f"نورتي الروم يا روح يحيى❤ {user.username}!")
    username_to_id = {}
    async def on_chat(self, user: User, message: str) -> None:    
        if message.startswith("teleport"):
            user_list = await self.highrise.get_room_users()
            for users, _ in user_list:
                self.username_to_id[users.username] = users.id
            parts = message.split()
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
            await self.highrise.teleport(user_id, (x, y, 0))
            await self.highrise.chat(f"{user.username} has been teleported to ({x}, {y}, {z})")