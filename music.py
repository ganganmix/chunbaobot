import nonebot
import os
from nonebot.adapters.onebot.v11 import Event, Bot, MessageSegment
from .sql_sgin import data_select

def repla(li):
    lis = []
    for i in li:
        oew = i.replace('.amr', '')
        lis.append(oew)
    return lis


mu = nonebot.on_fullmatch(msg=r"纯宝唱首歌", priority=3, block=True)


@mu.got(key='', prompt="什么歌呢")
async def _(bot: Bot, event: Event):
    if data_select(event.get_user_id()) != None:
        if int(data_select(event.get_user_id())[2]) >= 20:
            l = repla(os.listdir(r'.\music'))
            s = str(event.get_message())
            if s in l:
                await bot.send(event=event, message=MessageSegment.record(file=rf'file:///E:\desktop\云酱bot\nonebotfile\nonebotfile\plugins\music\{s}.amr'))
            else:
                await mu.send(MessageSegment.text(f'目前仅支持{l}'))
        else:
            await bot.send(event=event, message=MessageSegment.text('好感度不够，纯宝不能给你唱歌'))
    else:
        await bot.send(event=event, message=MessageSegment.text('还...还不会唱歌...要你签到了,然后我再去学学'))