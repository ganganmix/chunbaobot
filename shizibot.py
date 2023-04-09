import httpx
import nonebot
from nonebot.adapters.onebot.v11 import Event, Bot, MessageSegment
import nonebot.rule
import random


def re_shiz(text_data):
        data = {
    "spoken": f"{text_data}",
    "appid": "c99b68f68c3bc32e48b5aa4d1de25ff5",
    "userid": "abVSdgSu"
                }
        re_shiz = httpx.post(url="https://api.ownthink.com/bot", data=data)
        d_re = re_shiz.json()
        da_re = d_re.get('data').get('info').get('text').replace('小思', '小纯')
        return da_re


shiz = nonebot.on_startswith(msg="纯宝", priority=4, block=True)


@shiz.handle()
async def _(event: Event, bot: Bot):
    try:
        myda = event.get_message()
        myre = re_shiz(str(myda).replace('纯宝', '小思'))
        await bot.send(MessageSegment.text(myre))
    except httpx.ReadTimeout:
        await shiz.send(MessageSegment.text("time out了すみません"))


se = nonebot.on_keyword(keywords={'纯宝在吗', '纯宝在'}, priority=3, block=True)


@se.handle()
async def __():
    await se.send(MessageSegment.text(random.choice(['我一直在', '在你心里旅游', '你觉得呢'])))
    await se.send(MessageSegment.image(rf'file:///E:\desktop\云酱bot\nonebotfile\nonebotfile\plugins\emj\{random.randint(2,3)}.jpg'))


k = nonebot.on_keyword(keywords={'纯宝贴贴'}, priority=3, block=True)


k.handle()
async def ___(bot: Bot, event: Event):
    await bot.send(event=event, message=MessageSegment.text('贴贴，爱你'))