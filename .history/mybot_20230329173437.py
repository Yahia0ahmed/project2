from highrise import BaseBot

class Bot(BaseBot):
    pass
async def on_user_join(self, user: User) -> None:
        await self.highrise.chat(f"Welcome to the room, {user.username}!)