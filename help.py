import nonebot
from nonebot.adapters.onebot.v11 import MessageSegment, Event


he = nonebot.on_fullmatch(msg=('help', '菜单', '帮助'), priority=2, block=True)


@he.handle()
async def _(event: Event):
    await he.send(MessageSegment.at(event.dict().get('user_id'))+MessageSegment.text("""纯宝目前的轮子:
    我的勇者———公告/攻略(内测中,有一点乱)/计算(鸽)
    ①签到———签到/查询{先签到获取纯宝好感度，解锁更多功能哟(为了防止刷屏做的)}
    ②思知会话——纯宝+内容
    ③每日一言——每日一言|—言|mryy|yy
    ④图片——图片/壁纸(好感度100+)
    ⑤疯狂星期四文案——kfc|肯德基|星期四|疯狂星期四(好感度20+)
    ⑥music————纯宝唱首歌{目前只支持‘千本樱’,'aLIEz'}(好感度50+)
    ⑦说话————纯宝说+内容{测试阶段}（有好听的音源qq我哟）(好感度40+)
    """))