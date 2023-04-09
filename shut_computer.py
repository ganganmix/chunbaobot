import nonebot
from nonebot.adapters.onebot.v11 import MessageSegment, Message, Event
import os


gj = nonebot.on_fullmatch(msg=("gj", "关机"), priority=1, block=True)


@gj.handle()
async def _(event: Event):
    e = event.dict()
    if e.get("user_id") == 2174188197:
        await gj.send(MessageSegment.text(f"正在关机..."))
        os.system("shutdown/p")
    else:
        await gj.send(Message(f"[CQ:at,qq={e.get('user_id')}]")+MessageSegment.text("小宝贝,你的权限不足哟，请联系主人2174188197"))