# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 18:36
# @Author  : charl-z

""""
如果要更改脚本名称，请同步修改服务监控脚本的名称
"""

import requests
import time
import redis
import threading
from libs.utils import get_conf_handle, connect_postgresql_db, close_db_connection

conf_data = get_conf_handle()
r = redis.Redis(host=conf_data['REDIS_CONF']['host'],
                port=conf_data['REDIS_CONF']['port'],
                password=conf_data['REDIS_CONF']['password'],
                decode_responses=True, db=1
                )


def call_exec_network_query(network):
	try:
		payload = {"network": network}
		requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
		requests.post('http://127.0.0.1:8000/network_query/exec_network_query_task/', data=payload)
	finally:
		pass


if __name__ == "__main__":
	while True:
		time.sleep(10)
		thread_list = []
		for i in range(10):
			if r.llen(conf_data['NETWORK_QUERY_QUEUE']) != 0:
				network = r.lpop(conf_data['NETWORK_QUERY_QUEUE'])
				t = threading.Thread(target=call_exec_network_query, args=(network,))
				thread_list.append(t)
			else:
				break
		for thread in thread_list:
			thread.start()
		for thread in thread_list:
			thread.join()

