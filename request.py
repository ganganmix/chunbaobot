import nonebot
from nonebot.adapters.onebot.v11 import Event, PrivateMessageEvent, FriendRequestEvent, GroupRequestEvent, Bot
from nonebot.adapters.onebot.v11 import MessageSegment


re = nonebot.on_request(priority=2, block=True)
# 拒绝私聊


@re.handle()
async def reje_eriend(bot: Bot, event: FriendRequestEvent):
    await event.reject(bot=bot)


@re.handle()
async def app_group(event: GroupRequestEvent, bot: Bot):
    await event.approve(bot=bot)



