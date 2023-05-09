import time
import random
import asyncio
from datetime import datetime
from datetime import date
from highrise import __main__
from asyncio import run as arun
from highrise import Highrise
from highrise import BaseBot
from highrise.models import SessionMetadata, User, Item, Position, Reaction

Welcomemsg = [
    "منور احلا من يدخل الروم",
    "منور فديتك",
    "منور يعمري",
    "وسع وسع دخل الملك",
    "ايده هو ليه انت منور وحدك",
    "احبك كحب عنتر و عبله",
    "ادخل ادحل فديتك",
    "حياك نورت المقهى",
    "حي الله من يانه",
    "يا مرحبا نورك غطى على الكهربا",
    "حياك حياك الكل يستناك",
    "الجلب الي عضك كلتنا وين لغيبة",
    " جبنه طارية جا ريتنا قلنا مليون",
    "ارحب من نور الروم",
    "حللت أهلاً ووطئت سهلاً",
    "اجمل من يدخل الروم",
    "شوف مين جا اففف منور",
]

word = [
   "كلب",
   "حيوان",
   "قندرة",
   "زق",
   "قحبه",
   "سافل",
   "منحط",
   "زنجي",
   "عبيط",
   "ابن",
   "طيز",
   "كحبه",
   "ايجه",
   "اثول",
   "بربوك",
   "اموت",
   "انتحر",
   "اقتلك",
   "اذبحك",
   "جلب",
   "ديوس",
   "زمال",
   "صرم",
   "طيز",
   "كس",
   "عير",
   "منيوك",
   "منيوج",
   "انيجك",
   "ام العيورة",
   "بلاع العير",
   "عير",
   "امك تنيج",
   "ابوك كواد",
   "كواد",
   "بلاع الموس",
   "طيزك",
   "كس اختك",
   "كس امك",
   "يبن المنتاكه",
   "يبن المتنيكه",
   "ابوك ينيج",
   "ديوس",
   "تعال دكلي موطه",
   "سويلي موطه",
   "فرخ",
   "ابن ام العيوره",
   "خوات الكحبه",
   "كحاب",
   "كحبه",
   "ممكن قولد",
   "ممكن كولد",
   "ممكن ذهب",
   "اعطيني قولد",
   "اعطيني كولد",
   "اعطيني ذهب",
   "اعطوني قولد",
   "اعطوني كولد",
   "اعطوني ذهب",
   "متجري",
   "sf",
   "شوفو متجري",
   "اعطيني ملابس",
   "اعطوني ملابس",
]

emotes = [
    "idle-loop-sitfloor",
    "emoji-thumbsup",
    "emote-lust",
    "emoji-cursing",
    "emote-greedy",
    "emoji-flex",
    "emoji-gagging",
    "emoji-celebrate",
    "dance-macarena",
    "dance-tiktok8",
    "dance-blackpink",
    "emote-model",
    "dance-tiktok2",
    "dance-pennywise",
    "emote-bow",
    "dance-russian",
    "emote-curtsy",
    "emote-snowball",
    "emote-hot",
    "emote-snowangel",
    "emote-charging",
    "dance-shoppingcart",
    "emote-confused",
    "idle-enthusiastic",
    "emote-telekinesis",
    "emote-float",
    "emote-teleporting",
    "emote-swordfight",
    "emote-maniac",
    "emote-energyball",
    "emote-snake",
    "idle_singing",
    "emote-frog",
    "emote-superpose",
    "emote-cute",
    "dance-tiktok9",
    "dance-weird",
    "dance-tiktok10",
    "emote-pose7",
    "emote-pose8",
    "idle-dance-casual",
    "emote-pose1",
    "emote-pose3",
    "emote-pose5",
    "emote-cutey"
]
mods = [
    "D.IQ",
    "ItsYahya",
    "_1w1_",
    "Is1am",
    "mg_00_g",
]
modss = [
    "ItsYahya",
    "Is1am",
    "_1w1_",
    "xi9a",
    "mg_00_g",
]
class Bot(BaseBot):
    async def messageLoop(self):
     while True:
        msg = ("روم المقهى يحيكم☕🍴")
        await self.highrise.chat(msg)
        await asyncio.sleep(120)
    async def on_start(self, session_metadata: SessionMetadata) -> None:
        asyncio.create_task(self.messageLoop())
        await self.highrise.walk_to(Position(16.5,0,3.5,"FrontRight"))
        pass

    async def on_user_join(self, user: User) -> None:
        randomEmote = random.choice(emotes)
        await self.highrise.send_emote(randomEmote)
        wel = random.choice(Welcomemsg)
        await self.highrise.chat(f"{wel} {user.username}")
        if user.username == "_swtm":
            await self.highrise.chat("نورتي الروم يمزه 🤭")
        if user.username == "Wag19":
            await self.highrise.chat("عمتكم وجد دخلتتت🔥")
        if user.username == "only.y":
            await self.highrise.chat("الملك سلطان وصل")
        if user.username == "D.IQ":
            await self.highrise.chat("نورتي ضحوو 🔥")
        msg = f"[joined🟢]: {user.username}"
        print(msg)
    async def on_user_leave(self, user: User) -> None:
      msg = f"[left🔴]: {user.username}"
      print(msg)

    async def on_tip(self, sender: User, receiver: User, tip: Item) -> None:
        await self.highrise.chat(f"مسوي فيها غني يا {sender.username}")

    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
     try:
        if reaction == "clap" and user.username not in modss:
           await self.highrise.send_emote("emoji-flex")
     except:
         return      
     try:
      if reaction == "clap" and user.username in modss:
            await self.highrise.moderate_room(receiver.id, 'kick')
     except:
            await self.highrise.chat("ما اقدر تراه مشرف 😑")

    username_to_id = {}
    async def on_chat(self, user: User, message: str) -> None:
        if message.startswith("/help") and user.username not in mods:
            await self.highrise.chat("\n1.وقت : لأظهار الوقت و التاريخ الحالي\n2.رقصني : لرقصه عشوائيه\n")
        if message.startswith("/help") and user.username in mods:
            await self.highrise.send_whisper(user.id, "\n1.وقت : لأظهار الوقت و التاريخ الحالي\n2.تشيز : لرقصه عشوائيه\n3.(.)نقطه : لجعل البوت يتكلم عبر الهمس")
        if message.startswith("وقت"):
            now = datetime.now()
            # dd/mm/YY H:M:S
            dt_string = now.strftime("\n%Y/%m/%d\n%I:%M %p")
            await self.highrise.chat(f"🕑: {dt_string}")
        if message.startswith("تشيز"):
            randomEmote = random.choice(emotes)
            await self.highrise.send_emote(randomEmote, user.id)
            print(f"{randomEmote} {user.username}")
        if message in word:
         try:
          await self.highrise.moderate_room(user.id, 'kick')
         except:
                await self.highrise.chat("ما اطردك راح امشيها هاي المرة 😪")
        if message.startswith('k'):
            msg = await self.highrise.get_wallet()
            print(msg)
    async def on_whisper(self, user: User, message: str) -> None:
        if message.startswith("") and user.username in mods:
            text = message.replace("", "").strip()
            await self.highrise.chat(text)
        if message.lstrip().startswith('انقل'): #change the command name here
            if user.username.lower() in ["ihsein"]: # to add specific users, make sure its lowercase "ihsein" and not "iHsein"
                response = await self.highrise.get_room_users()
                users = [content[0]
                         for content in response.content]  # Extract the User objects
                usernames = [user.username.lower()
                             for user in users]  # Extract the usernames
                parts = message[1:].split()
                args = parts[1:]

                if len(args) < 2:
                    await self.highrise.send_whisper(user.id, "Usage: /tp <@username> <position>")
                    return
                elif args[0][0] != "@":
                    await self.highrise.send_whisper(user.id, f"Invalid user format. Please use '@username'.")
                    return
                elif args[0][1:].lower() not in usernames:
                    await self.highrise.send_whisper(user.id, f"{args[0][1:]} is not in the room.")
                    return

                position_name = " ".join(args[1:])
                if position_name == 'داخل':
                    dest = Position(8.5, 0, 14.5)
                elif position_name == 'خارج':
                    dest = Position(8.5, 0.75, 4.5)
                # if you want to add more locations, use the same method elif etc .. 
                else:
                    return await self.highrise.send_whisper(user.id, f"Unkown location ")
                user_id = next(
                    (u.id for u in users if u.username.lower() == args[0][1:].lower()), None)
                if not user_id:
                    await self.highrise.send_whisper(user.id, f"User {args[0][1:]} not found")
                    return
                await self.highrise.teleport(user_id, dest)
                await self.highrise.send_whisper(user.id, f"Teleported {args[0][1:]} to ({dest.x}, {dest.y}, {dest.z})")
            else:
                await self.highrise.send_whisper(user.id, "You can't use this command")
        else:
            pass
    async def on_user_move(self, user: User, pos: Position) -> None:
        if user.username == "ItsYahya":
           print(pos)
    async def run(self, room_id, token):
      await __main__.main(self, room_id, token)

if __name__ == "__main__":
    room_id = '62b1047b5d6d2f9b522ef3b7'
    token = 'b266b5636860d0a7f0ef411929d768d6425215facfd75c68a8b5f728ac615597'
    pass
    arun(Bot().run(room_id, token))
