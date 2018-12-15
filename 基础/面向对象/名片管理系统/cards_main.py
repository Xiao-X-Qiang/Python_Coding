#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3



import sys
sys.path.append('.')
import cards_tools

#1,2,3的操作，0退出，其它的提示
while True:

    cards_tools.show_menu()


    action_str = input('请输入你的选择：')
    print('您的操作选项是:%s' % action_str)

    #针对1，2，3的操作
    if action_str in ["1","2","3"]:
        # TODO(小强) 新建名片
        if action_str == "1":
            cards_tools.new_card()

        #显示全部
        elif action_str == "2":
            cards_tools.show_all()
        #查询名片
        elif action_str == "3":
            cards_tools.search_card()

    #针对0的操作
    elif action_str == "0":
        print('欢迎再次使用名片管理系统')
        break
    else:
        print('输入选项错误，请重新输入')
