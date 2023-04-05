from highrise import BaseBot, User

class Bot(BaseBot):
    pass
async def on_user_join(self, user: User) -> None:
        await self.highrise.chat(f"✨welcome✨ {user.username}!")
    