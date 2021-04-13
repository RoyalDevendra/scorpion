 

# For @scorpionHelp

"""Check if your userbot is working."""

import time

from datetime import datetime

from io import BytesIO

import requests

from PIL import Image

from scorpion import ALIVE_NAME, CMD_HELP, telever

from scorpion.__init__ import StartTime

from scorpion.scorpionConfig import Config, Var

# ======CONSTANTS=========#

CUSTOM_ALIVE = (

    Var.CUSTOM_ALIVE

    if Var.CUSTOM_ALIVE

    else "HELLO THIS IS 🦂scorpion🦂....I AM ALIVE and All functions are working!🤩"

)

ALV_PIC = Var.ALIVE_PIC 

if Var.ALIVE_PIC 

else "https://telegra.ph/file/b552e1c370a8269975d6a.jpg"

scorpionemoji = Var.CUSTOM_ALIVE_EMOJI if Var.CUSTOM_ALIVE_EMOJI else "**ꨄ︎**"

if Config.SUDO_USERS:

    sudo = "Enabled"

else:

    sudo = "Disabled"

# ======CONSTANTS=========#

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

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@scorpion_helpchat"

@scorpion.on(admin_cmd(outgoing=True, pattern="alive"))

@scorpion.on(sudo_cmd(outgoing=True, pattern="alive", allow_sudo=True))

async def amireallyalive(alive):

    start = datetime.now()

    myid = bot.uid

    """ For .alive command, check if the bot is running.  """

    end = datetime.now()

    (end - start).microseconds / 1000

    uptime = get_readable_time((time.time() - StartTime))

    if ALV_PIC:

        scorpion = f"**THIS IS SCORPION**\n\n"

        scorpion += f"`{CUSTOM_ALIVE}`\n\n"

        scorpion += (

            f"{scorpionemoji} **Telethon version**: `1.17`\n{scorpionemoji} **Python**: `3.8.3`\n"

        )

        scorpion += f"{scorpionemoji} **scorpionVersion**: `"1.0.1"`\n"

        scorpion += f"{scorpionemoji} **SUPPORT**: @scorpion_helpchat\n"

        scorpion += f"{scorpionemoji} **Sudo** : `{sudo}`\n"

        scorpion += f"{scorpionemoji} **scorpionUptime**: `{uptime}`\n"

        scorpion += f"{scorpionemoji} **Database Status**: `NO NEED TO WORRY ALL IS OK🤩`\n"

        scorpion += (

            f"{scorpionemoji} **My MASTER😌** : [{DEFAULTUSER}](tg://user?id={myid})\n\n"

        )

        await alive.get_chat()

        await alive.delete()

        """ For .alive command, check if the bot is running.  """

        await borg.send_file(alive.chat_id, ALV_PIC, caption=tele, link_preview=False)

        await alive.delete()

        return

    req = requests.get("https://telegra.ph/file/b552e1c370a8269975d6a.jpg")

    req.raise_for_status()

    file = BytesIO(req.content)

    file.seek(0)

    img = Image.open(file)

        await borg.send_message(

            alive.chat_id,

            f"**THIS IS SCORPION**\n\n"

         f"`{CUSTOM_ALIVE}`\n\n"

         (

            f"{telemoji} **Telethon version**: `1.17`\n{scorpionemoji} **Python**: `3.8.3`\n"

        )

         f"{scorpionemoji} **scorpionVersion**: `"1.0.1"`\n"

         f"{scorpionemoji} **SUPPORT**: @scorpion_helpchat\n"

         f"{scorpionemoji} **Sudo** : `{sudo}`\n"

         f"{scorpionemoji} **scorpionUptime**: `{uptime}`\n"

         f"{scorpionemoji} **Database Status**: `NO NEED TO WORRY ALL IS OK🤩`\n"

        scorpion += (

            f"{scorpionemoji} **My MASTER😌** : [{DEFAULTUSER}](tg://user?id={myid})\n\n"

        )

        await borg.send_file(alive.chat_id, file="https://telegra.ph/file/b552e1c370a8269975d6a.jpg")

        await alive.delete()

CMD_HELP.update({"alive": "➟ `.alive`\nUse - Check if your bot is working."})
