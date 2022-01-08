pageCenter = 'http://seatw.lib.tju.edu.cn/index.php/center.html' # 个人中心

pageIndex = 'http://seatw.lib.tju.edu.cn/index.php/reserve/index.html?f=wechat' # 首页

pagePre = 'http://seatw.lib.tju.edu.cn/index.php/prereserve/index.html' # 预定页面

pageFeed = 'https://seatw.lib.tju.edu.cn/index.php/reserve/index.html' # 预定后返回页面

def pageBook(lib_id,seat_key,dynamic_varity,yzm='',method='book'):
	if method=='book':
	 	return "http://seatw.lib.tju.edu.cn/index.php/reserve/get/libid=%s&%s=%s&yzm=%s"%(lib_id,dynamic_varity,seat_key,yzm)
	else:
		return "http://seatw.lib.tju.edu.cn/index.php/prereserve/save/libid=%s&%s=%s&yzm=%s"%(lib_id,dynamic_varity,seat_key,yzm)

