# 记录所有的名片的列表
card_list = [{"name": 'xm', "phone": "1333", "qq": "2222", "email": "2222"}]


def show_menu():
    """功能菜单"""
    print('*' * 20)
    print('欢迎使用名片管理系统V1.0')
    print('1.新建名片')
    print('2.显示全部')
    print('3.查询名片')
    print('0.退出系统')
    print('*' * 20)


def new_card():
    """新增名片"""
    print('-' * 20)
    print("新增名片")

    # 1.提示用户输入名片信息
    name_str = input('输入姓名：')
    phone_str = input('输入电话:')
    qq_str = input('qq:')
    email_str = input("输入Email:")

    # 2.建立名片字典

    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    # 3.字典追加到card_list
    card_list.append(card_dict)
    print(card_list)
    # 4.提示用户成功
    print('添加 %s用户成功' % name_str)


def show_all():
    """
    显示所有的名片
    :return: 无返回值
    """
    #"""显示所有名片"""

    # 当名片为空时，提醒用户
    if len(card_list) == 0:
        print('当前名片为空，请使用添加名片功能进行添加')
        return

    print('-' * 20)
    print("显示所有名片")
    # 打印表头和分隔线
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end='\t\t')
    print('')
    print('-' * 20)

    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict['name'], card_dict['phone'], card_dict['qq'], card_dict['email']))


def search_card():
    """搜索名片"""
    print('-' * 20)
    print("搜索名片")

    # 1.提示用户搜索的姓名
    find_name = input("请输入要搜索的姓名：")

    # 2.遍历列表是否存在该用户，如果没有，提示用户

    for card_dict in card_list:
        if card_dict['name'] == find_name:
            print("姓名\t\t电话\t\tQQ\t\temail")
            print("*" * 20)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict['name'], card_dict['phone'], card_dict['qq'], card_dict['email']))

            # 搜索找到后续的操作
            deal_card(card_dict)
            break

    else:
        print('抱歉，没有找到该用户')


def deal_card(find_dict):
    """
    对搜索到的名片的后续处理
    :param find_dict: 搜索到的的名片
    """
    action_str = input("请输入操作："
                       "1.修改"
                       "2.删除"
                       "3.返回上一级")

    if action_str == "1":
        print('修改名片')

        find_dict['name'] = input_card_info(find_dict['name'], '请输入姓名：')
        find_dict['phone'] = input_card_info(find_dict['phone'], '请输入电话')
        find_dict['qq'] = input_card_info(find_dict['qq'], "输入QQ")
        find_dict['email'] = input_card_info(find_dict['email'], "输入email")



    elif action_str == "2":
        print("删除名片")
        card_list.remove(find_dict)
        print('删除名片成功')


def input_card_info(dict_value, tip_message):
    """

    :param dict_value: 字典中原有的值
    :param tip_message:输入的提示文字
    :return:如果用户输入了内容，就返回内容；否则，返回字典中原有的值
    """
    # 提示用户输入内容
    input_str = input(tip_message + '回车默认不修改')

    # 针对用户的输入进行判断，如果输入内容，则返回内容
    if len(input_str) > 0:
        return input_str

    # 如果没有输入，则返回原有的值
    else:
        return dict_value
