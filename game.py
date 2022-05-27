import getpass
print('''
********************
   黑客编程小游戏
********************
	  ''')
username= input('请输入用户名:')
password=getpass.getpass('请输入密码:')
print('欢迎您:',username)
print('您的密码是:%s	\n请保存' % password)

print('%s您需要充值才能进入游戏'% username)

coins = input('请充值:')
coins = int(coins)

print('%s恭喜您充值成功！ 您的金币是%d' %(username,coins))