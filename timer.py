import time
import datetime

def timer_setting(new_settime):
    print('开始判断预定座位的时间\n')
    while True:
        # 获取现在时间
        now_time = datetime.datetime.now()
        today_year = now_time.date().year
        today_month = now_time.date().month
        today_day = now_time.date().day
        # print('now_time=')
        # print(now_time)
        #在这里设置抢的时间，离抢的时间最好留个一分钟以上
        date_time = datetime.datetime.strptime(str(today_year)+"-"+str(today_month)+"-"+str(today_day)+" "+new_settime, "%Y-%m-%d %H:%M:%S")
        # print('date_time=')
        # print(date_time)
        wait_time = (date_time - now_time).total_seconds()
        # print('wait=')
        # print(wait_time)
        if wait_time<1:
            print('处于选座时间！！！\n\n====================\n')
            return 2
        elif wait_time<3:
            print("目标时间" + str(date_time)+ "\t" + "预计等待：" + str(wait_time) + "毫秒")
            time.sleep(0.1)
        elif wait_time<6:
            print("目标时间"+str(date_time)+"\t" + "预计等待：" + str(wait_time*10) + "毫秒")
            time.sleep(0.2)
        elif wait_time<20:
            print("目标时间"+str(date_time)+"\t" + "预计等待：" + str(wait_time) + "秒")
            time.sleep(1)
            return 3
        elif wait_time<100:
            print("目标时间"+str(date_time)+"\t" + "预计等待：" + str(wait_time) + "秒")
            time.sleep(15)
            return 3
        elif wait_time<600:
            print("目标时间"+str(date_time)+"\t" + "预计等待：" + str(wait_time/60) + "分钟")
            time.sleep(75)
            return 3
        elif wait_time<3600:
            print("目标时间"+str(date_time)+"\t" + "预计等待：" + str(wait_time / 60) + "分钟")
            time.sleep(75)
            return 3
        elif wait_time>3600:
           print("目标时间"+str(date_time)+"\t" + "预计等待：" + str(wait_time / 3600) + "小时")
           #return 3
           time.sleep(75)
           return 3

        else:
            return 3
            exit()

if __name__ == '__main__':
    timer_setting()
