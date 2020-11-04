#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Anandpskerala


#Secret configs
from config import Config
from telegram import ParseMode


def start(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text=f"<b>Hello</b> [{update.message.from_user.first_name}](tg://user?id={update.message.from_user.id}), <b>I'm 𝗔𝗧𝗧𝗔𝗖𝗛 𝗙𝗜𝗟𝗘 𝗕𝗢𝗧.\n\nI Can <u>𝗔𝗧𝗧𝗔𝗖𝗛 𝗠𝗘𝗗𝗜𝗔𝗦</u> To Your Long Text, Send Me File & Reply File With Your Text Choice</b>\n\n<b>❌ 𝗦𝗣𝗔𝗠𝗠𝗜𝗡𝗚 𝗜𝗦 𝗦𝗧𝗥𝗜𝗖𝗧𝗟𝗬 𝗣𝗥𝗢𝗛𝗜𝗕𝗜𝗧𝗘𝗗.</b>", parse_mode="html")
