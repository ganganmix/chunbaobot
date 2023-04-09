import json

import httpx

# with open(file="setu.json", mode="r", encoding="utf-8") as f:
#     k = f.read()
# # kk = json.load(k)
# kk = json.loads(k)
# l = kk.get("posts")
# for i in range(172,562):
#     url = l[i].get("file_url")
#     url_requ = httpx.get(url)
#     name = l[i].get("tags")
#     with open(file=f"{i}.jpg", mode="wb") as f:
#         f.write(url_requ.content)
#     print("完成")