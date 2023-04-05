from highrise import BaseBot
from highrise.models import SessionMetadata, User, Literal

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        await self.highrise.walk_to([11,0,9],'FrontLeft')
        pass
    async def on_user_join(self, user: User) -> None:
        await self.highrise.chat(f"نورتي الروم يا روح يحيى❤ {user.username}!")