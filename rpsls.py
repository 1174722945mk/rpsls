#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：马匡
日期：2020/4/14
"""
import random
# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀
def name_to_number(cboice_name):
    """
    将游戏对象对应到不同的整数
    """
    if cboice_name=="石头":
	    return 0
    elif cboice_name=="史波克": 
	    return 1
    elif cboice_name=="布":
	    return 2
    elif cboice_name=="蜥蜴":
	    return 3
    elif cboice_name=="剪刀":
	    return 4
    else:
        return 5    
    # 使用if/elif/else语句将各游戏对象对应到不同的整数
    # 不要忘记返回结果
def number_to_name(comp_number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if comp_number==0:
      return "石头"
    elif comp_number==1:
      return "史波克"
    elif comp_number==2:
      return "布"
    elif comp_number==3:
      return "蜥蜴"
    elif comp_number==4:
      return "剪刀"
    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    # 不要忘记返回结果
def rpsls(cboice_name):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """
    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
    player_cboice=name_to_number(cboice_name)
    if player_cboice==5:
      print("Error: No Correct Name")
    else:
      print("您的选择为：%s"%(cboice_name))
    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
      comp_number=random.randint(0,4)
    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
      player_cboice_number=number_to_name(comp_number)	
    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
      print("机器的选择为：%s"%(player_cboice_number))
    # 在屏幕上显示计算机选择的随机对象
      rule=comp_number-player_cboice 
      if rule==2 or rule==-3 or rule==1 or rule==-4:
        print("机器赢了")
      elif rule==0:
        print("机器和你出的一样呢")
      else:
       print("您赢了")  
    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”
# 以下为完成游戏所需要用到的自定义函数
# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
cboice_name=input()
rpsls(cboice_name)
