import requests
from browerConfig import Header
from PIL import Image
import urllib3


def myWork(url,config):
	urllib3.disable_warnings()
	return requests.get(url=url,headers=config,verify=False)

def get_file_content(filePath):
	with open(filePath, 'rb') as fp:
		return fp.read()

#可设置调用百度api实现识别验证码从而达到一直刷的效果
def initBaidu():
	from aip import AipOcr

	""" 你的 APPID AK SK """
	APP_ID = '23106338'
	API_KEY = '1B1KiGBlgHND5TnKkAyYArvV'
	SECRET_KEY = 'WlyvfviBKKmMG7xA0BeoDGU7nAweDUDE'
	client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
	print('服务器连接成功')
	return client

def optical(client,image):
	""" 调用通用文字识别（高精度版） """
	image = Image.open(image)
	image = image.convert('L')
	point = []
	for i in range(256):
		if i<80:
			point.append(0)
		else:
			point.append(1)
	image = image.point(point,'1')
	image.save('tmp.jpg')
	image=get_file_content('tmp.jpg')
	client.basicAccurate(image);
	""" 如果有可选参数 """
	options = {}
	options["detect_direction"] = "true"
	options["probability"] = "true"
	print("开始加载图像验证码人工智能视觉识别技术，请保持网络链接...")
	yzm = client.basicAccurate(image, options).get("words_result")[0].get("words")
	yzm = str(yzm).replace(" ", "")
	if len(yzm)==0:
		return '无法识别'
	else:
		return yzm

def initImage(time,session):
    header = {
            "Host": "seatw.lib.tju.edu.cn",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116"
                          " Safari/537.36 QBCore/4.0.1219.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501"
                          " NetType/WIFI WindowsWechat",
            "Accept": "image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5",
            "Accept-Encoding": "br, gzip, deflate",
            "Refer": "https://seatw.lib.tju.edu.cn/index.php/prereserve/index.html",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4",
            "Cookie": "wechatSESS_ID=" + session + "; Hm_lvt_7ecd21a13263a714793f376c18038a87=" + str(time)
                      + "; Hm_lpvt_7ecd21a13263a714793f376c18038a87=" + time + "",
        }
    return header

def downloadImage(time,session):
	image = 'http://seatw.lib.tju.edu.cn/index.php/misc/verify.html'
	#browerConfig = Header(time,session)
	image = requests.get(image, initImage(str(time), session)).content
	with open('来选座验证码' + '.jpg', 'wb') as f:
		f.write(image)
		f.flush()
		f.close()
