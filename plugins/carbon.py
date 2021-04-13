# scorpion - userbot

# Copyright (C) 2021 Scorpion

# This file is a part of < https://github.com/loverboyXD/Scorpion-userbot/ >

# PLease read the GNU Affero General Public License in

# <https://www.github.com/LoverboyXD/scorpion-userbot/blob/mainfucker/LICENSE/>.


import os
import random

from carbonnow import Carbon

from . import *

all_col = [
    "Black",
    "Navy",
    "DarkBlue",
    "MediumBlue",
    "Blue",
    "DarkGreen",
    "Green",
    "Teal",
    "DarkCyan",
    "DeepSkyBlue",
    "DarkTurquoise",
    "MediumSpringGreen",
    "Lime",
    "SpringGreen",
    "Aqua",
    "Cyan",
    "MidnightBlue",
    "DodgerBlue",
    "LightSeaGreen",
    "ForestGreen",
    "SeaGreen",
    "DarkSlateGray",
    "DarkSlateGrey",
    "LimeGreen",
    "MediumSeaGreen",
    "Turquoise",
    "RoyalBlue",
    "SteelBlue",
    "DarkSlateBlue",
    "MediumTurquoise",
    "Indigo  ",
    "DarkOliveGreen",
    "CadetBlue",
    "CornflowerBlue",
    "RebeccaPurple",
    "MediumAquaMarine",
    "DimGray",
    "DimGrey",
    "SlateBlue",
    "OliveDrab",
    "SlateGray",
    "SlateGrey",
    "LightSlateGray",
    "LightSlateGrey",
    "MediumSlateBlue",
    "LawnGreen",
    "Chartreuse",
    "Aquamarine",
    "Maroon",
    "Purple",
    "Olive",
    "Gray",
    "Grey",
    "SkyBlue",
    "LightSkyBlue",
    "BlueViolet",
    "DarkRed",
    "DarkMagenta",
    "SaddleBrown",
    "DarkSeaGreen",
    "LightGreen",
    "MediumPurple",
    "DarkViolet",
    "PaleGreen",
    "DarkOrchid",
    "YellowGreen",
    "Sienna",
    "Brown",
    "DarkGray",
    "DarkGrey",
    "LightBlue",
    "GreenYellow",
    "PaleTurquoise",
    "LightSteelBlue",
    "PowderBlue",
    "FireBrick",
    "DarkGoldenRod",
    "MediumOrchid",
    "RosyBrown",
    "DarkKhaki",
    "Silver",
    "MediumVioletRed",
    "IndianRed ",
    "Peru",
    "Chocolate",
    "Tan",
    "LightGray",
    "LightGrey",
    "Thistle",
    "Orchid",
    "GoldenRod",
    "PaleVioletRed",
    "Crimson",
    "Gainsboro",
    "Plum",
    "BurlyWood",
    "LightCyan",
    "Lavender",
    "DarkSalmon",
    "Violet",
    "PaleGoldenRod",
    "LightCoral",
    "Khaki",
    "AliceBlue",
    "HoneyDew",
    "Azure",
    "SandyBrown",
    "Wheat",
    "Beige",
    "WhiteSmoke",
    "MintCream",
    "GhostWhite",
    "Salmon",
    "AntiqueWhite",
    "Linen",
    "LightGoldenRodYellow",
    "OldLace",
    "Red",
    "Fuchsia",
    "Magenta",
    "DeepPink",
    "OrangeRed",
    "Tomato",
    "HotPink",
    "Coral",
    "DarkOrange",
    "LightSalmon",
    "Orange",
    "LightPink",
    "Pink",
    "Gold",
    "PeachPuff",
    "NavajoWhite",
    "Moccasin",
    "Bisque",
    "MistyRose",
    "BlanchedAlmond",
    "PapayaWhip",
    "LavenderBlush",
    "SeaShell",
    "Cornsilk",
    "LemonChiffon",
    "FloralWhite",
    "Snow",
    "Yellow",
    "LightYellow",
    "Ivory",
    "White",
]


@scorpion_cmd(
    pattern="carbon",
)
async def crbn(event):
    xxxx = await eor(event, "Processing...")
    if event.reply_to_msg_id:
        temp = await event.get_reply_message()
        if temp.media:
            b = await scorpion_bot.download_media(temp)
            a = open(b, "r")
            code = a.read()
            a.close()
            os.remove(b)
        else:
            code = temp.message
    else:
        code = event.text.split(" ", maxsplit=1)[1]
    carbon = Carbon(code=code)
    await e.edit("`Meking Carbon...\n25%`")
    url = CARBON.format(code=code, lang=CARBONLANG)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    prefs = {"download.default_directory": "./"}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER, options=chrome_options)
    driver.get(url)
    await e.edit("`Be Patient...\n50%`")
    download_path = "./"
    driver.command_executor._commands["send_command"] = (
        "POST",
        "/session/$sessionId/chromium/send_command",
    )
    params = {
        "cmd": "Page.setDownloadBehavior",
        "params": {"behavior": "allow", "downloadPath": download_path},
    }
    driver.execute("send_command", params)
    driver.find_element_by_xpath("//button[contains(text(),'Export')]").click()
    await e.edit("`Processing..\n75%`")
    # Waiting for downloading
    sleep(0.5)
    await e.edit("`Yahh! Done dana Done.\n100% Completed.`")
    xx = await carbon.save("Scorpion_carbon")
    await e.edit("`Uploading`")
    await e.edit("`Uploading.`")
    await e.edit("`Uploading..`")
    await e.edit("`Uploading...`")
    await xxxx.delete()
    await scorpion_bot.send_file(
        event.chat_id,
        xx,
        caption=f"Carbonised by [{OWNER_NAME}](tg://user?id={OWNER_ID})\n with help of [Scorpion](https://github.com/loverboyXD/Scorpion-userbot).",
        force_document=True,
    )
    os.remove(xx)


@scorpion_cmd(
    pattern="rcarbon",
)
async def crbn(event):
    xxxx = await eor(event, "Processing..")
    if event.reply_to_msg_id:
        temp = await event.get_reply_message()
        if temp.media:
            b = await scorpion_bot.download_media(temp)
            a = open(b, "r")
            code = a.read()
            a.close()
            os.remove(b)
        else:
            code = temp.message
    else:
        code = event.text.split(" ", maxsplit=1)[1]
    col = random.choice(all_col)
    carbon = Carbon(code=code, background=col)
    await e.edit("`Meking Carbon...\n25%`")
    await e.edit("`Be Patient...\n50%`")
    await e.edit("`Processing..\n75%`")
    # Waiting for downloading
    sleep(0.5)
    await e.edit("`Yahh! Done dana Done.\n100% Completed.`")
    xx = await carbon.save("Scorpion_carbon")
    await e.edit("`Uploading`")
    await e.edit("`Uploading.`")
    await e.edit("`Uploading..`")
    await e.edit("`Uploading...`")
    await xxxx.delete()
    await scorpion_bot.send_file(
        event.chat_id,
        xx,
        caption=f"Carbonised by [{OWNER_NAME}](tg://user?id={OWNER_ID})",
        force_document=True,
    )
    os.remove(xx)


CMD_HELP.update(
    {
        "carbon": "**Carbon**"
    • .carbon <text/reply to msg/reply to document>
    Carbonise the text with default settings.
    • .rcarbon <text/reply to msg/reply to document>
    Carbonise the text, with random bg colours.
    }
)