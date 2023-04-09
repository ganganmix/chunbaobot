import nonebot
from nonebot.adapters.onebot.v11 import GroupIncreaseNoticeEvent, Bot, Message, GroupDecreaseNoticeEvent, MessageSegment
import random
from nonebot.params import Depends
add_group = nonebot.on_notice(priority=2,block=True)


@add_group.handle()
async def _(bot: Bot, event: GroupIncreaseNoticeEvent):
    await bot.send(
        event=event,
        message='大家好，我叫纯宝，是个bot，以后请多指教，想了解更多，就请输入菜单或帮助,一起来玩吧 ⁽( ˃̵͈̑ᴗ˂̵͈̑)⁽')
    await bot.send_group_msg(group_id=event.group_id, message=Message(rf'[CQ:at,qq={event.user_id}]')+MessageSegment.text('亲爱的勇者哟，欢迎你加入,输入帮助或者菜单一起玩吧'))


@add_group.handle()
async def _(bot: Bot, event: GroupDecreaseNoticeEvent):
    await bot.send_group_msg(group_id=event.group_id, message=Message(random.choice(['有位勇者迷失在了时间之中...', '时间很长,有人被改变而离开了,而有人却能在这里成了守望者', '旧人的离去,是为了更好的相逢,或者更好的开始...'])))