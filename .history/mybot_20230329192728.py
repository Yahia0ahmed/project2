from highrise import BaseBot, User, SessionMetadata

class Bot(BaseBot):
        pass
async def on_start(self, session_metadata: SessionMetadata) -> None:
        self.highrise.vhat
        pass
async def on_user_join(self, user: User) -> None:
        await self.highrise.chat(f"welcome to my room, {user.username}!")
    