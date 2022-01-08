# 环境说明
## python3(3.6 3.7 3.8试过都没问题)
## 要安装的包：pillow bs4 requests（应该是这几个就够了，如果提示缺少就按照报错补充安装就行）
# 文件名说明
## 1、app_book.py 是抢今天的位置的，一般是用于明日预约失败后，设置第二天早上6点自动抢，时间已设定为6点，只需要在当天（晚上12点后）启动脚本即可
## 2、app_prebook.py 是预约明天的位置的，用于每天中午12点整预约明日座位
## 3、url.py 是抢座的链接，当前为天津大学来选座的地址，其他学校的同学要想改的话只需要抓包改为自己学校的url即可
# 关于抢哪个座位的问题
## 需要靠抓包来确定你想要抢的那个座位的id，然后填入app文件里面的座位信息
# 关于wechat_session
## 1、首先需要使用抓包软件抓取你的wechat_session
## 2、session的变动问题：session有两个变动的情况，一是每隔一段时间会自动更新一次session，大概是半天左右；二是每当你隔了大概十几分钟后在微信上点进去你的来选座主页，session也会变，所以在你运行脚本之后就不要再点进主页了
## 3、然后在改好你的座位id后使用命令
##    python app_prebook.py(或者app_book.py) 然后再加上你抓包的session即可
##    例如python app_prebook.py 123456
# 关于成功率
## 通过我考研期间的实践，只要不是两个脚本同时抢同一个位置，成功率在百分之98以上，所以！！！大家一定要改好自己的座位id，发现没抢到很可能就是撞脚本了，那就换一个位置吧，别死磕一个位置！
# 本脚本开源免费，大家别被骗了，有问题欢迎留言联系