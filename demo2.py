a =  {"name":"李四","password":"123321"}

zh = input("请输入账号:")
mm = input("请输入密码:")

for i in a:
    if zh == i.get("name"):
        i.get("password") = mm
    else:
        a.update("name") = zh
        a.update("password") = mm




