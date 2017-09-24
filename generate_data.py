import random

humidity = [random.normalvariate(mu=70, sigma=5) for i in range(100)]
humidity_round = [int(x) for x in humidity]
print humidity_round

temp = [random.normalvariate(mu=40, sigma=2) for i in range(100)]
temp_round = [int(x) for x in temp]
print temp_round

import time

curr_time = int(time.time())
times = [curr_time + i for i in range(100)]
print times


import nifty_sql

nifty_sql.insert(column_names=["Timestamp", "Temperature", "Humidity"], values=zip(times, temp_round, humidity_round))