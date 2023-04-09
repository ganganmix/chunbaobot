import random
import nonebot
from .sql_sgin import *
from nonebot.adapters.onebot.v11 import Event, Bot, MessageSegment

m = nonebot.on_keyword(keywords={'cbqd', '纯宝签到', '签到', 'qd', '每日签到'}, priority=2, block=True)


@m.handle()
async def _(event: Event, bot: Bot):
    da = data_select(str(event.dict().get('user_id')))
    if da == None:
        i = data_insert((f"{event.get_user_id()}", f"{event.dict()['sender']['nickname'] if len(event.dict()['sender']['nickname'])<= 5 else event.dict()['sender']['nickname'][0:5]}"))
        await bot.send(event=event, message=f'{i}')
    elif (len(da) != 0) & (datetime.datetime.now().day != da[3].day):
        ra = random.randint(1, 10)
        update = data_update((f"{event.get_user_id()}", f'{ra}'))
        await bot.send(event=event,
                       message=f"{update},今日好感度加{ra}，{random.choice(['真的好喜欢你呀', '每天都要和我贴贴哟^V^'])}")
    elif (len(da) != 0) & (datetime.datetime.now().day == da[3].day):
        await bot.send(event=event, message=MessageSegment.text(
            f"{random.choice([f'今天已签到，现在的好感度是{data_select(str(event.get_user_id()))[2]}，改天再来刷我好感吧', '感受过你的热情了，爱你哟'])}"
        )
                                            + MessageSegment.image(
            fr"file:///E:\desktop\云酱bot\nonebotfile\nonebotfile\plugins\emj\{random.randint(1, 3)}.jpg"))


get = nonebot.on_startswith(msg=('查询', '查询好感度', '查看积分'), priority=2, block=True)


@get.handle()
async def __(event: Event, bot: Bot):
    g = data_select(event.get_user_id())
    await bot.send(event=event,
                   message=MessageSegment.at(event.get_user_id()) + MessageSegment.text(fr"纯宝对你的好感为{g[2]}"))
