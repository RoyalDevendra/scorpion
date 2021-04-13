# Scorpion - Userbot

# Copyright (C) 2021 Scorpion

# This file is a part of < https://github.com/loverboyXD/Scorpion-userbot/ >

# PLease read the GNU Affero General Public License in

# <https://www.github.com/LoverboyXD/scorpion-userbot/blob/mainfucker/LICENSE/>.

from telethon.errors import ChatSendInlineForbiddenError

from . import *

REPOMSG = (
    "• **SCORPION USERBOT** •\n\n",
    "• Repo - [Click Here](https://github.com/loverboyXD/Scorpion-userbot)\n",
    "• Support - @scorpion_helpchat",
)


@scorpion_cmd(pattern="repo$")
async def repify(e):
    try:
        q = await scorpion_bot.inline_query(Var.BOT_USERNAME, "repo")
        await q[0].click(e.chat_id)
        if e.sender_id == scorpion_bot.uid:
            await e.delete()
    except ChatSendInlineForbiddenError:
        await eor(e, REPOMSG)
