from highrise import BaseBot
from highrise.models import SessionMetadata, User, Literal

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
       pass
    async def walk_to(self, dest: tuple[float, float, float],facing: Literal["FrontRight", "FrontLeft", "BackRight", "BackLeft"],) -> None:
            await self.highrise.walk_to([9,0,10],'FrontRight')
        
    async def on_user_join(self, user: User) -> None:
        await self.highrise.chat(f"نورتي الروم يا روح يحيى❤ {user.username}!")