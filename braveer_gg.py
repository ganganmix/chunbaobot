# import random
#
# import httpx
# import nonebot
# from nonebot.adapters.onebot.v11 import Message, Bot, Event, GroupMessageEvent, MessageSegment
#
#
# def rec():
#     li = httpx.get(url=r'https://www.taptap.cn/webapiv2/feed/v6/by-group?group_id=60015&type=official&sort=created&X'
#                        r'-UA=V%3D1%26PN%3DWebApp%26LANG%3Dzh_CN%26VN_CODE%3D93%26VN%3D0.1.0%26LOC%3DCN%26PLT%3DPC'
#                        r'%26DS%3DAndroid%26UID%3D790b5761-ec46-479d-9310-ceba53e0ab5e%26DT%3DPC%26OS%3DWindows%26OSV'
#                        r'%3D14.0.0')
#     lis_title = []
#     lis_id = []
#     lis_img = []
#     lis_summary = []
#     for i in range(10):
#         da = li.json()['data']['list'][i]['moment']['extended_entities']['topics'][0]
#         lis_title.append(f"""{i + 1}，{da['title']}""")
#         lis_id.append(da['id'])
#         lis_summary.append(da['summary'])
#         lis_img.append(None if da['images'] == [] else da['images'][0]['url'])
#     str_title = rf"""
#     {lis_title[0]}
#     {lis_title[1]}
#     {lis_title[2]}
#     {lis_title[3]}
#     {lis_title[4]}
#     {lis_title[5]}
#     {lis_title[6]}
#     {lis_title[7]}
#     {lis_title[8]}
#     {lis_title[9]}
#     请输入数字,获取对应的连接
#     """
#     return str_title, lis_id, lis_summary, lis_img
#
#
# k = nonebot.on_keyword(keywords={'勇者公告', '公告'}, priority=3, block=True)
#
#
# @k.got('_', prompt=f"{rec()[0]}")
# async def _(event: GroupMessageEvent, bot: Bot):
#     try:
#         await bot.send(event=event, message=MessageSegment.at(event.get_user_id()) + MessageSegment.text(
#             fr'{rec()[2][int(str(event.get_message()))-1]}') + (None if rec()[3] == [] else MessageSegment.image(
#             file=fr'{rec()[3][int(str(event.get_message()))-1]}')) + MessageSegment.text(
#             fr'https://www.taptap.cn/topic/{rec()[1][int(str(event.get_message()))-1]}'))
#     except ValueError:
#         await bot.send(event=event, message=MessageSegment.at(event.get_user_id())+MessageSegment.text(random.choice(['请输入阿拉伯数字', '输入像 1 这样的数字', '小可爱, 可能是小纯的问题呢，请麻烦联系一下主人吧'])))
