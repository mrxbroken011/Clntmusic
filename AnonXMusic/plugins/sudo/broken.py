import requests
import random
from AnonXMusic import app, userbot
from AnonXMusic.misc import SUDOERS
from pyrogram import * 
from pyrogram.types import *
from AnonXMusic.utils.broken_ban import admin_filter






Yumikoo_text = [
"hey please don't disturb me.",
"who are you",    
"aap kon ho",
"aap mere owner to nhi lgte ",
"hey tum mera name kyu le rhe ho meko sone do",
"ha bolo kya kaam hai ",
"dekho abhi mai busy hu ",
"hey i am busy",
"aapko smj nhi aata kya ",
"leave me alone",
"dude what happend",    
]

strict_txt = [
"i can't restrict against my besties",
"are you serious i am not restrict to my friends",
"Malik Se Gaddaari Nahi Kar Sakti Malik Maa Ch@d Denge", 
"Bhakk lawde bsdk k mai apne dosto ko kyu kru",
"Meri itni Aukaat nahi Tu bhi Aukaat Me Reh Lawde", 
"hey stupid admin @Mrbrokn Ne hi mujhe banaya hai", 
"ha ye phele krlo maar lo ek dusre ki gwaand",  
"i can't he is my closest friend",
"Pagal Hai Kya Chutiye Malik Maar Dalenge mujhe", 
"i love him please don't restict this user try to usertand "
]


 
ban = ["ban","boom","maa"]
unban = ["unban","aazad"]
mute = ["mute","silent","chup"]
unmute = ["unmute","speak","bolne"]
kick = ["kick", "out","nikaal","nikal","laat"]
promote = ["promote","adminship","shabashi"]
fullpromote = ["fullprote","landlord"]
demote = ["demote","lelo"]
group = ["group"]
channel = ["channel"]



# ========================================= #


@app.on_message(filters.command(["aby","aby"], prefixes=["b", "B"]) & admin_filter)
async def restriction_app(app :app, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    if len(message.text) < 2:
        return await message.reply(random.choice(Yumikoo_text))
    bruh = message.text.split(maxsplit=1)[1]
    data = bruh.split(" ")
    
    if reply:
        user_id = reply.from_user.id
        for banned in data:
            print(f"present {banned}")
            if banned in ban:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))          
                else:
                    await app.ban_chat_member(chat_id, user_id)
                    await message.reply("OK Baby 😘😘, Maa chodh di madrchod ki sala Chutiya tha 😝!")
                    
        for unbanned in data:
            print(f"present {unbanned}")
            if unbanned in unban:
                await app.unban_chat_member(chat_id, user_id)
                await message.reply(f"Ok Baby 😘😘, aap bolte hai toh unban kar diya 🥰") 
                
        for kicked in data:
            print(f"present {kicked}")
            if kicked in kick:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))
                
                else:
                    await app.ban_chat_member(chat_id, user_id)
                    await app.unban_chat_member(chat_id, user_id)
                    await message.reply("Ok Baby 😘😘! bhag bhosdike💀") 
                    
        for muted in data:
            print(f"present {muted}") 
            if muted in mute:
                if user_id in SUDOERS:
                    await message.reply(random.choice(strict_txt))
                
                else:
                    permissions = ChatPermissions(can_send_messages=False)
                    await message.chat.restrict_member(user_id, permissions)
                    await message.reply(f"Ok Baby 😘😘, muted successfully! Chup Baith Bhadwe🤫.") 
                    
        for unmuted in data:
            print(f"present {unmuted}")            
            if unmuted in unmute:
                permissions = ChatPermissions(can_send_messages=True)
                await message.chat.restrict_member(user_id, permissions)
                await message.reply(f"Huh, OK,🙂 Bolna madrchod!")   


        for promoted in data:
            print(f"present {promoted}")            
            if promoted in promote:
                await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=True,
                    can_delete_messages=True,
                    can_restrict_members=False,
                    can_pin_messages=True,
                    can_promote_members=False,
                    can_manage_chat=True,
                    can_manage_video_chats=True,
                       )
                     )
                await message.reply("ok Baby 😘😘,Le be promoted 🎉 !")

        for demoted in data:
            print(f"present {demoted}")            
            if demoted in demote:
                await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
                    can_change_info=False,
                    can_invite_users=False,
                    can_delete_messages=False,
                    can_restrict_members=False,
                    can_pin_messages=False,
                    can_promote_members=False,
                    can_manage_chat=False,
                    can_manage_video_chats=False,
                       )
                     )
                await message.reply("Ok Baby 😘😘,Hat BKL demoted 👎!")


#async def your_function():
    for fullpromoted in data:
        print(f"present {fullpromoted}")            
        if fullpromoted in fullpromote:
            await app.promote_chat_member(chat_id, user_id, privileges=ChatPrivileges(
                can_change_info=True,
                can_invite_users=True,
                can_delete_messages=True,
                can_restrict_members=True,
                can_pin_messages=True,
                can_promote_members=True,
                can_manage_chat=True,
                can_manage_video_chats=True,
               )
             )
            await message.reply("Ok Baby 😘😘,Lo Ji fullpromoted !")
