
import requests
import locust

class MyUser(locust.HttpUser):  #创建 locust.HttpUser子类
    wait_time = locust.between(1,2) #每个task间隔1-2秒

    @locust.task   #装饰器
    def test_api(self):
        resp = self.client.get('http://127.0.0.1:8081/')
        assert resp.staus_code == 200
#以上是基础语法，实际测试都是自动生成的代码，无需一行行书写。
