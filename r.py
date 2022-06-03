import getpass
print('''
***********************
        小游戏
***********************
     ''')
username = input('请输入用户名:')
password = getpass.getpass('请输入密码:')

print('%s请输入您的真名'%username)
name=input('请输入名字:')
name1='hanbing'
hehe = name == name1
print('名字',hehe)
print('%s输入您的岁数'%username)
age=input('请输入岁数:')
age1='13'
haha = age == age1
print('岁数:',haha)
print('本人验证成功欢迎:%s'%name)
print('正在为您登陆游戏.............')