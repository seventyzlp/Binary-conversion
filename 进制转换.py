"""
实现了在16进制内任意进制到任意进制的转换
"""

String16 = "0123456789ABCDEF"
print('输入原始数据:')
Raw_data = input()
for i in range(len(Raw_data)):  # 检测输入数值的正确性
    if String16.find(Raw_data[i]) == -1:
        print("原始数据输入错误")
        quit()

print('输入原始数据的进制:')
Raw_update = int(input())
if Raw_update <= 1 or String16.find(max(Raw_data)) >= Raw_update: # 分条件检测输入进制的正确性
    print('进制输入错误，请重试')
    quit()
elif Raw_update > 16:
    print('目前进制转换最多支持输入16进制数')
    quit()
print('输入目标进制:')
Aim_update = int(input())
if Aim_update <= 1:  # 检测目标进制的正确性
    print('进制输入错误，请重试')
    quit()


def Math_translate(Raw, Raw_base, Aim_base):
    i = 0
    Aim = ''
    global String16
    Raw_base10 = 0
    # 若初始数据不是10进制，那么先把初始数据转化为10进制
    for n in range(-1, -len(Raw) - 1, -1):
        Raw_base10 = String16.find(Raw[n]) * int(Raw_base) ** i + Raw_base10
        i += 1
    # 如果目标数据是10进制，那么就直接输出结果
    if Aim_base == 10:
        Aim = str(Raw_base10)
        return Aim
    # 目标数据不是10进制，那么就相除倒取余
    i = Raw_base10
    while i > 0:
        Aim = String16[i % Aim_base] + Aim
        i //= Aim_base
    return Aim


print("进制转换结果为：" + Math_translate(Raw_data, Raw_update, Aim_update))
