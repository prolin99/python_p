#計算星期數
#【最後目標】
#已知1900年元旦是星期一，求1901年1月到2000年12月中，有多少月份的第一天(1號)是星期日。
#【討論】
#Python可以從某一天的日期得到該天是星期幾，星期一的值是0，星期日的值是6。

import datetime

day= datetime.datetime(1900,1,1)
print(day.weekday())

sun_day=0
for y in range(1901,2001):
    for m in range(1,13):
        dayw = datetime.datetime(y,m,1).weekday()
        print(y,m,1,dayw)
        if dayw == 6:
            sun_day= sun_day+1

print(sun_day)
