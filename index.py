# -*- coding: UTF-8 -*-

import requests


url = "https://qmsg.zendee.cn/send/"+${secrets.Qmsg}+"?msg=WPS稻壳签到信息\nwomen"
print("Qmsg推送结果", requests.get(url).text)
