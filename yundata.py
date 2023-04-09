import datetime
import httpx
import nonebot
from nonebot.adapters.onebot.v11 import MessageSegment

timing = nonebot.require("nonebot_plugin_apscheduler").scheduler

yy = nonebot.on_keyword(keywords={"mryy", "yy", "每日一言", "一言"}, priority=3, block=True)


@yy.handle()
async def _():
    me_yy = httpx.get(url=r"https://v1.hitokoto.cn/").json()
    yy_data = me_yy.get('hitokoto')
    yy_author = me_yy.get('from')
    await yy.send(MessageSegment.text("{data}——————{name:>}".format(data=yy_data, name=yy_author)))


@timing.scheduled_job("cron", hour="*", minute="00", id="timg")
async def timg():
    if datetime.datetime.now().hour in [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]:
        me_yy = httpx.get(url=r"https://v1.hitokoto.cn/").json()
        (bt,) = nonebot.get_bots().values()
        yy_data = me_yy.get('hitokoto')
        yy_author = me_yy.get('from')
        await bt.send_msg(
            # event=event,
            message_type="private",
            user_id=int(2174188197),
            message="{}————{:>}\n".format(yy_data,
                                          yy_author) + f"已经{datetime.datetime.now().hour}点了，还不起床陪我玩嘛\n输入/help陪我玩吧"
        )
        # await bt.send_group_msg(
        #     group_id=int(729725255),
        #     message="{}————{:>}".format(yy_data, yy_author)
        # )
        # await bt.send_group_msg(
        #     group_id=int(729725255),
        #     message=f"已经{datetime.datetime.now().hour}了，还不起床陪我玩嘛\n输入/help陪我玩吧"
        # )
    else:
        ...
