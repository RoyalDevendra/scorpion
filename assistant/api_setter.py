# Scorpion - UserBot
# Copyright (C) 2021 Scorpion-userbot
#
# This file is a part of < https://github.com/loverboyXD/Scorpion-userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/loverboyXD/Scorpion-userbot/blob/main/LICENSE/>.

from . import *

# main menu for api setting


@callback("apiset")
@owner
async def apiset(event):
    await event.edit(
        get_string("ast_1"),
        buttons=[
            [Button.inline("Remove.bg", data="rmbg")],
            [custom.Button.inline("« Back", data="setter")],
        ],
    )


# remove.bg api


@callback("rmbg")
@owner
async def rmbgapi(event):
    await event.delete()
    pru = event.sender_id
    var = "RMBG_API"
    name = "Remove.bg API Key"
    async with event.client.conversation(pru) as conv:
        await conv.send_message(get_string("ast_2"))
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message("Cancelled!!")
        else:
            await setit(event, var, themssg)
            await conv.send_message("{} changed to {}".format(name, themssg))
