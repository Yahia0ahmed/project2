from highrise import BaseBotو user

class Bot(BaseBot):
    pass
async def on_user_join(self, user: User) -> None:
        await self.highrise.chat(f"ارحب نورت الروم, {user.username}!")
    