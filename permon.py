# coding:utf8
import os
import time
import json
import random
from locust import HttpUser, task, between, events

metamap = {}


# 只执行一次的初始化处理任务
@events.init.add_listener
def on_locust_init(environment, **kwargs):
    print("been run for only once.")
    nids = os.listdir("./metadata")
    for nid in nids:
        filename = "./metadata/{}".format(nid)
        with open(filename, "r") as f:
            if nid not in metamap.keys():
                metamap[nid] = f.read()
            f.close()


def getrandommeta():
    global metamap
    nids = list(metamap.keys())
    return metamap[random.choice(nids)]


class Main(HttpUser):
    wait_time = between(1, 2)

    @task
    def activity(self):
        payloads = {
            "appid": "baiduboxapp",
            "token": "cd29e6856979d56786651c243ae1857e",
            # "nid": "16694885760294558536",
            "metaValue": getrandommeta(),
            "from": "shoubai_videoland",
            "appVersion": "11.25.0.0",
            "extParams": '{"cuid":"FB7B5DD26CF988E9804E10ED185AB354D7DFE1E7EOHHBPCPMSE", "imei":"863519042756317","get":{"ut":"vivi_6_0_VIVO"},"iad":"1187265","extRequest":[]}',
            "authorUid": "34743656315",
        }
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
        }
        url = "/activity/getstoactivityconf"
        self.client.post(url, data=payloads, headers=headers)


