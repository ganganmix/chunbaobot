import httpx
import re
import nonebot
from nonebot.adapters.onebot.v11 import MessageSegment, Bot, Event


def get(uid):
    d = httpx.get(url=fr'https://api.lsrnb.com/lsrapi/qs/?qq={uid}').json()
    return d


h = nonebot.on_startswith(msg='纯宝开盒', priority=3, block=True)


@h.got(key='_', prompt='你要查看谁，请@出来')
async def _(bot: Bot, event: Event):
    try:
        pattern = re.compile(r'\d+')
        da= pattern.findall(event.dict()['raw_message'])
        u = get(int(da[0]))
        await bot.send(event=event, message=MessageSegment.text(fr"小纯查到,这个老实人是{u['phonediqu'].strip('移动联通')}人,手机尾号为{u['phone'][-4:]},请注意隐私保护"))  if u["status"] != 500 else await bot.send(event=event, message=MessageSegment.text('纯宝没有找到'))
    except ValueError:
        await bot.send(event=event, message=MessageSegment.text('纯宝出错了，请联系主人'))