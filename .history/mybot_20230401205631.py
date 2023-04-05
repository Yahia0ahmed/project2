
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

