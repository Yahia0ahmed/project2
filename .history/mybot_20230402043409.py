from highrise import BaseBot
from highrise.models import SessionMetadata, User, Item

class Bot(BaseBot):
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        await self.highrise.walk_to([5,0,10],'FrontLeft')
        pass
    async def on_user_join(self, user: User) -> None:
        await self.highrise.chat(f"نورتي الروم يا روح يحيى❤ {user.username}!")
    async def on_user_join(self, user: User) -> None:
           await self.highrise.chat(f"نورتي الروم يا روح يحيى❤ {user.username}!")
    async def on_tip(self, sender: User, receiver: User, tip: Item) -> None:
       await self.highrise.chat(f"{sender: User} شكرا لتبرعك الى)




    async def on_chat(self, user: User, message: str) -> None:    
           if message.startswith("السلام عليكم"):
            await self.highrise.chat("وعليكم السلام")
           if message.startswith("شلونك"):
            await self.highrise.chat("الحمد الله وانت ؟")
           if message.startswith("الحمد لله"):
            await self.highrise.chat("دوم")
           if message.startswith("بوت"):
            await self.highrise.chat("انت بوت😡")
           if message.startswith("تحبني"):
            await self.highrise.chat("يا قي")