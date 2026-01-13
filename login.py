# 用户登录功能

def login(username, password):
    """简单的登录函数"""
    if username == "admin" and password == "123456":
        return True
    return False

def logout():
    """登出功能"""
    print("用户已登出")
    return True
