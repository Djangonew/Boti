# Variable created is grey
# recode by Rexa
# Gausah hapus memek


import os
import random
from telethon.tl.types import InputMessagesFilterPhotos, InputMessagesFilterVideo, InputMessagesFilterVoice
from Hikari.events import register
from Hikari import telethn as tbot, ubot2                 


@register(pattern="^/asupan ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari Video Asupan...🔍**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@punyakenkan", filter=InputMessagesFilterVideo
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih Asupan nya Kak", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Asupan Mulu")  


@register(pattern="^/ppanime ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari PP Anime...🔍**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@animehikarixa", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih pp animenya", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("PP animenya ga ada")  


@register(pattern="^/wallanime ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari Wallpaper Anime...🔍**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@Anime_WallpapersHD", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih Wallpaper Animenya", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Wallpaper Animenya Kosong")  


@register(pattern="^/ayang ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari ayang...💕**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Nih kak ayang nya", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Asupannya gaada komsol")  
        
        
@register(pattern="^/ppcp ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari Mentahan Foto Couple ...**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@mentahanppcp", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Mentahan PP couple by Hikari robot", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Asupannya gaada komsol")  
        
@register(pattern="^/bokep?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari Bokep....**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@bahaninimah", filter=InputMessagesFilterVideo
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Negative Content By Hikari robot", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Asupannya gaada komsol")  
        
@register(pattern="^/bugil ?(.*)")
async def _(event):
    memeks = await event.reply("**Mencari Foto Bugil...**") 
    try:
        asupannya = [
            asupan
            async for asupan in ubot2.iter_messages(
            "@durovbgst", filter=InputMessagesFilterPhotos
            )
        ]
        kontols = random.choice(asupannya)
        pantek = await ubot2.download_media(kontols)
        await tbot.send_file(
            event.chat.id, 
            caption="Adult Photos by Hikari robot", 
            file=pantek
            )
        await memeks.delete()
    except Exception:
        await memeks.edit("Asupannya gaada komsol")  


__mod_name__ = "ᴀꜱᴜᴘᴀɴ"

__help__ = """
🎥 Special Video

๏ /asupan - Video Tiktok random.

📷 Special Foto

๏ /ayang - Untuk mendapatkan ayang mu (sering digunakan oleh jomblo)
๏ /bugil - Coba sendiri (tobat anj)
๏ /bokep - Coli mulu anj
๏ /ppcp - Untuk Mendapatkan Mentahan PP couple Secara Random

"""
















  




