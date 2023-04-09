import random
import time

import nonebot
from nonebot.adapters.onebot.v11 import PokeNotifyEvent, GroupRecallNoticeEvent, Bot, MessageSegment, Message, Event

al = nonebot.on_notice(priority=2, block=True)


a = ['那...那里...那里不能戳...绝对...', '嘤嘤嘤,好疼', '你再戳，我就把你的作案工具没收了，哼哼~', '别戳了别戳了，戳怀孕了',
   '嘤嘤嘤，人家痛痛', '我错了我错了，别戳了', '桥豆麻袋,别戳老子', '手感怎么样', '戳够了吗？该学习了', '戳什么戳，没戳过吗',
   '你用左手戳的还是右手戳的？', '不要啦，别戳啦', '给你一拳', '再摸就是狗', '你这么闲吗？', '代码写完了吗？', '你能AK WF吗？', '爬去学习']


@al.handle()
async def _(bot: Bot, event: PokeNotifyEvent):
    if event.target_id == 3312249917:
        await bot.send(event=event, message=Message(random.choice(a)), at_sender=True)