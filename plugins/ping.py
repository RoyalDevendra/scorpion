# Scorpion 

# Copyright (C) 2021 Scorpion

# This file is a part of < https://github.com/loverboyXD/Scorpion-userbot/ >

# PLease read the GNU Affero General Public License in

# <https://www.github.com/LoverboyXD/scorpion-userbot/blob/mainfucker/LICENSE/>.

import time
from datetime import datetime

from scorpion import CMD_HELP
from scorpion.__init__ import StartTime
from scorpion.plugins import OWNER_ID, TELE_NAME

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@asst_cmd("ping")
@owner
async def _(event):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await asst.send_message(
        event.chat_id,
        f"**╔═╦═╦═╦╦══╗\n║╬║║║║║║╔═╣\n║╔╣║║║║║╚╗║\n╚╝╚═╩╩═╩══╝**\n\n ➣`{ms}` \n ➣ `{uptime}`\n **Owner** ➣ [{TELE_NAME}](tg://user?id={OWNER_ID})",
    )



