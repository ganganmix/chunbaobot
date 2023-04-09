# import httpx
# import nonebot
# from nonebot.adapters.onebot.v11 import MessageSegment, GroupMessageEvent, Bot
# import random
#
# def rec(un):
#     li = httpx.get(
#         url=fr'https://www.taptap.cn/webapiv2/feed/v6/by-group?from={un * 10}&group_id=60015&group_label_id=521987&limit=10&sort=commented&type=group_label&X-UA=V%3D1%26PN%3DWebApp%26LANG%3Dzh_CN%26VN_CODE%3D93%26VN%3D0.1.0%26LOC%3DCN%26PLT%3DPC%26DS%3DAndroid%26UID%3D790b5761-ec46-479d-9310-ceba53e0ab5e%26DT%3DPC%26OS%3DWindows%26OSV%3D14.0.0'
#         )
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
#     请输入数字,获取对应的连接\
#     或是没有您想要的攻略,请输入 下一页
#     """
#     return str_title, lis_id, lis_summary, lis_img
#
#
# def y():
#     for i in range(10):
#         yield i
#
#
# l = y()
#
#
# k = nonebot.on_keyword(keywords={'攻略', 'gl'}, priority=3, block=True)
#
#
# @k.got(f'_', prompt=f"{rec(0)[0]}")
# async def _(event: GroupMessageEvent, bot: Bot):
#     u = next(l)
#     re = rec(u)
#     if str(event.get_message()) == '下一页':
#         await k.reject(prompt=re[0])
#     try:
#         if str(event.get_message()) in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
#             await bot.send(event=event, message=MessageSegment.at(event.get_user_id()) + MessageSegment.text(
#             fr'{re[2][int(str(event.get_message()))-1]}') + MessageSegment.image(
#             file=fr'{re[3][int(str(event.get_message()))-1]}') + MessageSegment.text(
#             fr'https://www.taptap.cn/topic/{re[1][int(str(event.get_message()))-1]}'))
#             await bot.send(event=event, message=MessageSegment.text(fr'rec({u}[3][{int(str(event.get_message()))-1}])'))
#     except ValueError:
#         await bot.send(event=event, message=MessageSegment.at(event.get_user_id())+MessageSegment.text(random.choice(['请输入阿拉伯数字', '输入像 1 这样的数字', '小可爱, 可能是小纯的问题呢，请麻烦联系一下主人吧'])))
