import xlrd
import xlwt
from xlutils.copy import copy

# 参数设置
filter_column = 1  # 原始电话号码所在列,从1开始
result_column = 2  # 筛选后电话号码所放列,从1开始
xls_name = "phone.xls"


sheet = xlrd.open_workbook(xls_name)  # 打开文件
read_sheet = sheet.sheet_by_index(0)
wb = copy(sheet)
write_sheet = wb.get_sheet(0)  # 选取表单

num = 0
for row in range(0, read_sheet.nrows):
    str_phone = str(read_sheet.cell_value(row, filter_column-1))  # 提取出的原始电话号码
    phone_split = str_phone.split()   # 空格分割后的电话号码, 默认空格
    print(phone_split)

    result_phone = ""
    for number in phone_split:
        if number.startswith('1'):
            result_phone = result_phone + " " + number[0:11]
    if result_phone!="":
        global num
        num = num + 1
        write_sheet.write(num, result_column-1, result_phone)  # 写入数据

wb.save('筛选后的电话号码.xls')  # 保存
