import getpass

def login(users_db):
    print("=== 登录界面 ===")
    username = input("请输入用户名: ")
    password = getpass.getpass("请输入密码: ")
    if username in users_db and users_db[username]['password'] == password:
        print("登录成功！")
        return username
    print("用户名或密码错误！")
    return None

def register(users_db):
    print("=== 注册界面 ===")
    username = input("请输入用户名: ")
    if username in users_db:
        print("该用户名已存在！")
        return None
    password = getpass.getpass("请输入密码: ")
    users_db[username] = {
        'password': password,
        'profile': {},
        'savings': 0,
        'investment': 0,
        'rate': 0
    }
    print("注册成功！")
    return username

def input_profile(user):
    print("=== 输入个人资料 ===")
    name = input("姓名: ")
    age = input("年龄: ")
    email = input("邮箱: ")
    user['profile'] = {
        'name': name,
        'age': age,
        'email': email
    }
    print("资料保存成功！")

def input_finances(user):
    print("=== 储蓄与投资输入 ===")
    try:
        user['savings'] = float(input("当前储蓄金额（元）："))
        user['investment'] = float(input("计划投资金额（元）："))
        user['rate'] = float(input("预计年化收益率（例如7代表7%）：")) / 100
        user['years'] = int(input("投资年限（年）："))
    except ValueError:
        print("输入有误，请重新输入。")
        return False
    print("财务信息录入成功！")
    return True

def compound_interest(principal, rate, years):
    # 利用复利公式A = P*(1 + r)^n
    return principal * ((1 + rate) ** years)

def main():
    users_db = {}
    print("欢迎使用理财系统！")
    while True:
        action = input("请选择: [1] 登录 [2] 注册 [0] 退出：")
        if action == '1':
            username = login(users_db)
            if username:
                user = users_db[username]
            else:
                continue
        elif action == '2':
            username = register(users_db)
            if username:
                user = users_db[username]
            else:
                continue
        elif action == '0':
            print("感谢使用！再见。")
            break
        else:
            print("无效选择，请重试。")
            continue

        # 个人资料
        input_profile(user)

        # 财务输入
        while not input_finances(user): pass

        savings_final = compound_interest(user['savings'], 0.03, user['years'])  # 假设储蓄年利率3%
        investment_final = compound_interest(user['investment'], user['rate'], user['years'])

        print("\n=== 运算结果 ===")
        print(f"{user['profile'].get('name', '')} 您好，{user['years']}年后：")
        print(f"储蓄金额（3%年利率复利）：{savings_final:.2f} 元")
        print(f"投资金额（{user['rate']*100:.2f}%年利率复利）：{investment_final:.2f} 元")
        print("计算完成，可继续登录或注册新用户。\n")

if __name__ == "__main__":
    main()