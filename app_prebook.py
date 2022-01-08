import function
import url
from browerConfig import Header
import jscode
import time
import re

from bs4 import BeautifulSoup
import timer
import threading
import requests
import sys

# #session = input("请输入提取的系统鉴权（wechatSESS_ID）:\n")
# session = '362a773bbb83646018af250e0ef65b08'
# #session = get_session_from_web()
# firstTime = int(time.time())
# browerConfig = Header(firstTime,session)
# r = function.myWork(url.pageIndex,browerConfig.initPageIndex()).text
# your_seats = []



def judge_session():
	'''在首页判断'''
	if("您好" in r):
	    print("====================\n成功访问选座系统！\n====================\n")
	else:
	    print("====================\n访问选座系统失败，请检查你的wechatSESS_ID是否正确！\n====================\n")
	    exit()

def personal_information():
	#html = function.myWork(url.pageCenter,browerConfig.initPageIndex()).text
	html = str(function.myWork(url.pageCenter,browerConfig.initPageIndex()).content,'utf-8')
	soup = BeautifulSoup(html, "html.parser")
	print("您的个人信息如下：\n")
	for k in soup.find_all('div', class_='nick'):
	    print("您的系统昵称：" + k.string)
	for k in soup.find_all('div', class_='userinfo'):
	    print(str(k).replace("</div>", "").replace('<div class="userinfo" data-href="/index.php/times/index.html">', "")
	          .replace('<div class="nick">', "用户名：").replace('<div class="study-detail">', "").replace("<div>", "")
	          .replace('<div class="bg">', "").replace("学习时间", "：学习时间").replace("排名", "：排名").replace("单日最长", "：单日最长")
	          .replace("\t", ""),end='')
	print("====================\n\n个人信息获取完毕,开始继续执行！\n\n====================\n")

def usual_seat_information():
	print('您的常用座位为：')
	soup = BeautifulSoup(r,'lxml')
    #print(soup)
	seat = soup.select('#seat_info tr td')

	print(seat)
	if len(seat)>1:
		for i in range(2):
			your_seats.append([seat[i]['lib_id'],seat[i]['seat_key'],seat[i].text.strip()])
			print(seat[i].text.strip())
		# print(seat)
		print('\n====================\n')
	else:
		print('请先设置常用座位！')
		exit()

def yzm_ocr():
	yzm='0'
	for i in range(1,15):
	    if len(str(int(yzm))) != 4: # int(yzm)目的是为了排错
		    secondTime = time.time()
		    print('\n====================\n开始获取图片验证码')
		    t = threading.Thread(target=function.downloadImage(str(secondTime),session))
		    t.setDaemon(True)
		    t.start()
		    t.join()



		    print('初始化百度验证码识别功能')
		    client = function.initBaidu();
		    print('读取图片')
		    yzm = function.optical(client,'来选座验证码.jpg')
		    print("来选座系统验证码自动识别为：%s\n====================\n"%yzm)
	    else:
		    print('识别成功，开始预定\n\n====================\n')
		    return yzm
	print('验证码识别失败！')

def decode_verify(method='book'):
	print('\n====================\n\n开始识别动态验证码')
	for i in range(100):
		try:
			if method=='book':
				#html = function.myWork(url.pageIndex,browerConfig.initPageIndex()).text
				html = str(function.myWork(url.pageIndex,browerConfig.initPageIndex()).content,'utf-8')
			else:
				#html = function.myWork(url.pagePre,browerConfig.initPagePre()).text
				html = str(function.myWork(url.pagePre,browerConfig.initPagePre()).content,'utf-8')
			verity = re.compile(r'/layout/(.*?).js').findall(html,re.S)[0]
			print('动态验证码为：',verity)
			decode_verity = jscode.js_code[verity]
			print('动态验证码破解成功：',decode_verity)
			return decode_verity
		except:
			#time.sleep(0.01)
			continue
	print('动态验证码破解失败，请重试或手动订座');
	#exit()

def booking_today(lib_id,seat_key):
	seat_time = 0
	#print(url.pageBook(lib_id,seat_key,decode_verify()));exit()
	result = function.myWork(url.pageBook(lib_id,seat_key,decode_verify()),browerConfig.initBook_today()).json()
	print(result['msg'])
	if '成功' in result['msg']:
		#function.myWork(result['url'],browerConfig.initBook_today()).text
		str(function.myWork(result['url'],browerConfig.initBook_today()).content,'utf-8')
	elif '验证码' in result['msg']:
		print('\n====================\n检测到需要图片验证码\n====================\n')
		#time.sleep(30)
		#booking_today(lib_id, seat_key)
		result = function.myWork(url.pageBook(lib_id,seat_key,decode_verify(),yzm_ocr()),browerConfig.initBook_today()).json()
		#html = function.myWork(url.pageFeed, browerConfig.Feedback()).text
		html = str(function.myWork(url.pageFeed, browerConfig.Feedback()).content,'utf-8')
		if '取消预订' in html:
			feedbackinfo = BeautifulSoup(html, 'lxml').select('#reserve-list div.block-warp')[0].text.replace('延时','').replace('取消预订', '').replace('签到', '').replace('\n\n', '')
			print('\n预定结果：\n', feedbackinfo)
		else:
			print('预定失败')
			seat_time += 1
			print('开始座位', your_seats[seat_time][2])
			booking_today(your_seats[seat_time][0], your_seats[seat_time][1])
			#booking_today(lib_id, seat_key)
	else:
		time.sleep(0.1)
		#seat_time += 1
		booking_today(your_seats[seat_time][0], your_seats[seat_time][1])
		#booking_today(lib_id, seat_key)
		#exit()
	feedback()

def booking_tomorrow(lib_id,seat_key):
	result = function.myWork(url.pageBook(lib_id,seat_key,decode_verify('prebook'),method='prebook'),browerConfig.initBook(lib_id)).json()
	print(result)
	if '成功' in result['msg']:
		#function.myWork(result['url'],browerConfig.initPagePre(firstTime,time.time(),session)).text
		str(function.myWork(result['url'],browerConfig.initPagePre(firstTime,time.time(),session)).content,'utf-8')
	elif '验证码' in result['msg']:
		print('\n====================\n检测到需要图片验证码，开始识别\n====================\n')
		function.myWork(url.pageBook(lib_id,seat_key,decode_verify('prebook'),yzm_ocr(),method='prebook'),browerConfig.initBook(lib_id)).json()
	else:
		print(result['msg'])
		booking_tomorrow(lib_id,seat_key)
		#exit()
	feedback_pre()

def feedback_pre():
	print('\n====================\n\n正在检测您所选的座位信息......')
	#html = function.myWork(url.pagePre,browerConfig.initPagePre(firstTime,time.time(),session)).text
	html = str(function.myWork(url.pagePre,browerConfig.initPagePre(firstTime,time.time(),session)).content,'utf-8')
	if '已经预定' in html:
		feedbackinfo = BeautifulSoup(html,'lxml').select('div.row-msg')[0].text
		print('\n预定结果：\n',feedbackinfo)
	else:
		print('预定失败！')

def feedback():
	print('\n====================\n\n正在检测您所选的座位信息......')
	#html = function.myWork(url.pageFeed,browerConfig.Feedback()).text
	html = str(function.myWork(url.pageFeed,browerConfig.Feedback()).content,'utf-8')
	if '取消预订' in html:
		feedbackinfo = BeautifulSoup(html,'lxml').select('#reserve-list div.block-warp')[0].text.replace('延时','').replace('取消预订','').replace('签到','').replace('\n\n','')
		print('\n预定结果：\n',feedbackinfo)
	else:
		print('预定失败')

if __name__ == "__main__":
	print('欢迎使用来选座')
	print('=========================================\n开始执行\n=========================================\n')
	your_seats = []
	session = '0d190b48f1065d920e1ae7e05424a3a14a8552b37afd74e3'
	newsettime = "12:00:00"
	if len(sys.argv) == 1 :
		print('默认设置')
	elif len(sys.argv) == 2:
		session = str(sys.argv[1])
	
	else :
		print('参数错误')
	print('Session: '+session+'\nTime:\t '+newsettime+'\n')  
                

	while True:
		if (timer.timer_setting(newsettime) == 3):
			# session = input("请输入提取的系统鉴权（wechatSESS_ID）:\n")

			# session = get_session_from_web() #这个没用
			firstTime = int(time.time())
			browerConfig = Header(firstTime, session)
			#r = function.myWork(url.pageIndex, browerConfig.initPageIndex()).text		#这里应该使用utf-8编码
			r = str(function.myWork(url.pageIndex, browerConfig.initPageIndex()).content,'utf-8')
			judge_session()
			personal_information()
			#usual_seat_information()  #设置常用座位后，自动抢常用座位
			your_seats.append(['10137', '17,18', '卫津路校区 415 21号'])
			your_seats.append(['10137', '13,18', '卫津路校区 415 29号'])
		    # 已知id和座位号之后可以赋值在这里，这是我的两个常用座位麻烦换一个座位抢免得冲突了哈哈

			#print(your_seats)
		# 开始抢座
		elif (timer.timer_setting(newsettime) == 2):
			#这里要预约和要抢今天的就把相应的语句取消注释
			print('开始预定明天座位', your_seats[0][2])
			booking_tomorrow(your_seats[0][0], your_seats[0][1])
			#print('开始选择今天座位', your_seats[0][2])
			#booking_today(your_seats[0][0], your_seats[0][1])
		else:#以下没啥用
			print('开始选择今天座位', your_seats[0][2])
			print(your_seats[0][0])
			print(your_seats[0][1])
			print(your_seats[1][0])
			print(your_seats[1][1])
			booking_today(your_seats[0][0], your_seats[0][1])



