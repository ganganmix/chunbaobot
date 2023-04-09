import nonebot
from nonebot.adapters.onebot.v11 import MessageSegment, Event, Bot
import httpx
import os
import time
import random
from .sql_sgin import data_select

def re_(dat):
    re_speak = httpx.get(url=fr'https://fanyi.sogou.com/reventondc/synthesis?text={dat}&speed=1&lang=zh-CHS&from=translateweb&speaker=6')
    with open(file=fr'E:\desktop\云酱bot\nonebotfile\nonebotfile\plugins\speak\{dat}.mp3', mode="wb") as f:
        f.write(re_speak.content)
    os.system(rf'ffmpeg -i E:\desktop\云酱bot\nonebotfile\nonebotfile\plugins\speak\{dat}.mp3 -ar 8000 -ab 7.9k -ac 1 -y E:\desktop\云酱bot\nonebotfile\nonebotfile\plugins\speak\{dat}.amr')


say = nonebot.on_startswith(msg="纯宝说", priority=3, block=True)


@say.handle()
async def _(event: Event, bot: Bot):
    if data_select(event.get_user_id()) != None:
        if int(data_select(event.get_user_id())[2]) >= 40:
            dat = event.get_message()
            ip_dat = str(dat).strip("纯宝说")
            re_(ip_dat)
            await say.send(MessageSegment.text(random.choice(['让我想想怎么说', 'ちょっと待って让我想想', ])))
            time.sleep(2)
            await bot.send(event=event,message=MessageSegment.record(file=rf'file:///E:\desktop\云酱bot\nonebotfile\nonebotfile\plugins\speak\{ip_dat}.amr'))
            time.sleep(2)
            os.remove(rf'E:\desktop\云酱bot\nonebotfile\nonebotfile\plugins\speak\{ip_dat}.mp3')
            os.remove(rf'E:\desktop\云酱bot\nonebotfile\nonebotfile\plugins\speak\{ip_dat}.amr')
        else:
            await say.send(MessageSegment.text(random.choice(['抱歉最近风控严重除主人外暂时不支持', '小宝贝,你的好感度不足哟', '就不和你说话~哼']))+MessageSegment.image(r'file:///E:\desktop\云酱bot\nonebotfile\nonebotfile\plugins\emj\1.jpg'))
    else:
        await bot.send(event=event, message=MessageSegment.text('先签到, 不然不和你说话...'))