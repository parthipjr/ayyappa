#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG & @Mrk_YT

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
from bot import UPDATE_CHANNEL # Update Text Message Channel Update
from bot import MRK_YT_MASTER
from bot import MT_GROUP
from bot import MT_CHANNEL # Main Channel Added
from bot.motech import MT_BOT_UPDATES

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("😔 Sorry Dude, You are **🅱︎🅰︎🅽︎🅽︎🅴︎🅳︎ 🤣🤣🤣**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="<b>📢 READ THIS INSTRUCTION  📢</b>\n\n🗣️ചോദിക്കുന്ന സിനിമകൾ നിങ്ങൾക്ക് ലഭിക്കണം എന്നുണ്ടെങ്കിൽ നിങ്ങൾ താഴെ കൊടുത്തിട്ടുള്ള ചാനലിൽ ജോയിൻ ചെയ്യണം. ജോയിൻ ചെയ്ത ശേഷം വീണ്ടും ഗ്രൂപ്പിൽ പോയി ആ ബട്ടനിൽ അമർത്തിയാൽ നിങ്ങൾക്ക് ഞാൻ ആ സിനിമ പ്രൈവറ്റ് ആയി അയച്ചു തരുന്നതാണ്..😍\n\n 🗣 In Order To Get The Movie Requested By You in Our Groups, You Will Have To Join Our Official Channel First. After That, Try Accessing That Movie Again From Our Group. I'll Send You That Movie Privately...😍 \n\n𝗝𝗢𝗜𝗡  𝗢𝗨𝗥  𝗠𝗔𝗜𝗡  𝗖𝗛𝗔𝗡𝗡𝗘𝗟 🙏",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="🔰 𝙹𝙾𝙸𝙽 𝙼𝙰𝙸𝙽 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 🔰", url=f"https://t.me/{UPDATE_CHANNEL}")]
              ])
            )
            return
        except Exception:
            await update.reply_text(f"<b>This bot should be the admin on your update channel</b>\n\n<b>💢 ഈ ചാനലിൽ  @{UPDATE_CHANNEL} ബോട്ടിനെ അഡ്മിൻ ആക്. എന്നിട്ട് /start കൊടുക്</b>\n\n<b>🗣️ any Doubt @Mo_Tech_Group</b>")
            return  
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '🔔Join Main Channel🔔', url=f"{MT_CHANNEL}"
                                )
                        ],
                        [
                            InlineKeyboardButton
                                (
                                    '⚔ PDISK LINKS ⚔', url=f"{MT_BOT_UPDATES}"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await update.bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '👨‍💼 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛𝚜 👨‍💼', url="https://t.me/Mo_TECH_YT"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await update.bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '👨‍💼 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛𝚜 👨‍💼', url="https://t.me/Mo_TECH_YT"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('👨‍💼Creater', url=f'https://t.me/{MRK_YT_MASTER}'),
        InlineKeyboardButton('Help 🤔', callback_data="help")
    ],[
        InlineKeyboardButton('🗣️Group', url=f'{MT_GROUP}'),
        InlineKeyboardButton('Channel🔊', url=f'{MT_CHANNEL}')
    ],[
        InlineKeyboardButton('🎯 Pdisk links 🎯', url='https://t.me/Filmy_beats')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('🏠 𝙷𝚘𝚖𝚎', callback_data='start'),
        InlineKeyboardButton('𝙰𝚋𝚘𝚞𝚝 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('🔐 𝙲𝚕𝚘𝚜𝚎 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('👤 Mrk YT👤', url='https://t.me/MRK_YT'),
        InlineKeyboardButton('Skp KP👤', url='https://t.me/Skp_Kp')
    ],[
        InlineKeyboardButton('👤 AlbertEinstein 👤', url='https://t.me/AlbertEinsteinTG')
    ],[
        InlineKeyboardButton('🏠 Home', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
