import random
from .sql_sgin import data_select
import nonebot
from nonebot.adapters.onebot.v11 import Message, MessageSegment, Event, exception

setu1 = nonebot.on_startswith(msg=("壁纸", "图片", 'tup', 'bz'), priority=3, block=True)


@setu1.handle()
async def _(event: Event):
    if data_select(event.get_user_id()) != None:
        if int(data_select(event.get_user_id())[2]) >= 100:
                await setu1.send(MessageSegment.image(file=fr"file:///E:\desktop\云酱bot\nonebotfile\nonebotfile\plugins\image\{random.randint(0, 292)}.jpg"))
        else:
            await setu1.send(message=MessageSegment.text(f'当前对你的好感度为{data_select(event.get_user_id())[2]},还不能给你看哦'))
    else:
        await setu1.send(message=MessageSegment.text('你先签到,让小纯想想发哪张'))