print('输入原始数据:')
Raw_data = input()
print('输入原始数据的进制:')
Raw_update = int(input())
if Raw_update <= 1 or int(max(Raw_data)) >= Raw_update:
    print('进制输入错误，请重试')
    quit()
elif Raw_update > 16:
    print('目前进制转换最多支持输入16进制数')
    quit()
print('输入目标进制:')
Aim_update = int(input())
if Aim_update == 0:
    print('进制输入错误，请重试')
    quit()
String16 = "0123456789ABCDEF"
# 若初始数据不是10进制，那么先把初始数据转化为10进制
i = 0
t = 0
Raw_base10 = 0
for n in range(-1, -len(Raw_data)-1, -1):
    Raw_base10 = String16.find(Raw_data[n]) * int(Raw_update) ** i + Raw_base10
    i += 1
# 如果目标数据是10进制，那么就直接输出结果
if Aim_update == 10:
    print('进制运算结果为：')
    print(Raw_base10)
    quit()
# 目标数据不是10进制，那么就相除倒取余
i = Raw_base10
Aim = ''
while i > 0:
    Aim = str(i % Aim_update)+Aim
    i //= Aim_update
print('进制运算结果为：')
print(Aim)
