import random

import httpx
import nonebot
from nonebot.adapters.onebot.v11 import MessageSegment, Bot, Event
from nonebot.adapters.onebot.v11.helpers import extract_image_urls
import os

# 获取对应url
# 存入image_datebase

f = nonebot.on_keyword(keywords={'存入', '保存', '纯宝存入'}, priority=3, block=True)


@f.handle()
async def _(bot: Bot, event: Event):
    with open(file=r'.\ikun\ikun_url.txt', mode='a') as f:
        # 将图片链接存入ikun_url.txt中，可能会失真
        f.write(str(extract_image_urls(event.get_message())[0])+'\n')
    await bot.send(event=event, message=MessageSegment.text(f"存入成功了,小黑子"))



k = nonebot.on_keyword(keywords={'ikun', '坤坤', '鸡', '只因', '开团', '🐔', '寄', '坤'}, priority=3, block=True)


@k.handle()
async def __(bot: Bot, event:Event):
    with open(file=r'.\ikun\ikun_url.txt', mode='r') as f:
        d = f.readlines()
    await bot.send(event=event, message=MessageSegment.image(file=fr"{d[random.randint(0, len(d)-1)][:-1]}"))