# 将数据处理为handle07.py的数据格式
import os
import time
import pandas as pd


folder_source = "Gan_test"   # 需要修改
folder_out = "files"   # 结果输出文件夹
time_start = time.time()
excels = os.listdir(folder_source)

# 读取字典
gan = pd.read_excel(folder_source + ".xlsx", header=None)
list1 = list(gan[0])
list2 = list(gan[1])
for index,st in enumerate(list2):
    list2[index] = st.split()[0]
dict_gan = dict(zip(list1,list2))


# Handle the table
excel1_name = excels[0]  # Gan-N-NEG.xlsx
excel2_name = excels[1]  # Gan-N-POS.xlsx
excel3_name = excels[2]  # Gan-P-NEG.xlsx
excel4_name = excels[3]  # Gan-P-POS.xlsx

excel1 = pd.read_excel(folder_source + "/" + excel1_name)
list1_columns = list(excel1.columns)
list1_columns.remove('Compound')
list1_name = []
for material in list1_columns:
    if material in list(dict_gan.keys()):
        list1_name.append(dict_gan[material])
    else:
        list1_name.append("0")

excel2 = pd.read_excel(folder_source + "/" + excel2_name)
list2_columns = list(excel2.columns)
list2_columns.remove('Compound')
list2_name = []
for material in list2_columns:
    if material in list(dict_gan.keys()):
        list2_name.append(dict_gan[material])
    else:
        list2_name.append("0")

excel3 = pd.read_excel(folder_source + "/" + excel3_name)
list3_columns = list(excel3.columns)
list3_columns.remove('Compound')
list3_name = []
for material in list3_columns:
    if material in list(dict_gan.keys()):
        list3_name.append(dict_gan[material])
    else:
        list3_name.append("0")

excel4 = pd.read_excel(folder_source + "/" + excel4_name)
list4_columns = list(excel4.columns)
list4_columns.remove('Compound')
list4_name = []
for material in list4_columns:
    if material in list(dict_gan.keys()):
        list4_name.append(dict_gan[material])
    else:
        list4_name.append("0")  # 如果dict没有此值,以"0"替代


# 求四张表的交集
intersection = list(set(list1_name).intersection(set(list2_name)).
                    intersection(set(list3_name)).intersection(set(list4_name)))
# 筛选出共同的列
list1_columns2 = list1_columns.copy()
list2_columns2 = list2_columns.copy()
list3_columns2 = list3_columns.copy()
list4_columns2 = list4_columns.copy()

for id,value in enumerate(list1_name):
    if value not in intersection:
        # 不能以序号删除,因为每删除一次后索引值会变;解决办法是list1_columns不能删
        del excel1[list1_columns[id]]
        list1_columns2.remove(list1_columns[id])

for id,value in enumerate(list2_name):
    if value not in intersection:
        del excel2[list2_columns[id]]
        list2_columns2.remove(list2_columns[id])

for id,value in enumerate(list3_name):
    if value not in intersection:
        del excel3[list3_columns[id]]
        list3_columns2.remove(list3_columns[id])

for id,value in enumerate(list4_name):
    if value not in intersection:
        del excel4[list4_columns[id]]
        list4_columns2.remove(list4_columns[id])


# 四张表交集后的最小长度
list1_len = len(list1_columns2)
list2_len = len(list2_columns2)
list3_len = len(list3_columns2)
list4_len = len(list4_columns2)
print("四张表交集前大小:", list1_len, list2_len, list3_len, list4_len)
min_length = min(list1_len, list2_len, list3_len, list4_len)


# 删除长的表,表对齐
excel_num = 4  # 表的数目

if len(list1_columns2) != min_length:
    length = list1_len - min_length
    x = [range(list1_len-length, list1_len)]
    excel1.drop(excel1.columns[x], axis=1, inplace=True)

if len(list2_columns2) != min_length:
    length = list2_len - min_length
    x = [range(list2_len-length, list2_len)]
    excel2.drop(excel2.columns[x], axis=1, inplace=True)

if len(list3_columns2) != min_length:
    length = list3_len - min_length
    x = [range(list3_len-length, list3_len)]
    excel3.drop(excel3.columns[x], axis=1, inplace=True)

if len(list4_columns2) != min_length:
    length = list4_len - min_length
    x = [range(list4_len-length, list4_len)]
    excel4.drop(excel4.columns[x], axis=1, inplace=True)


# 合并表格前修改列名
one_list = ["Compound"]
one_list.extend(range(min_length))
excel1.columns = one_list
excel2.columns = one_list
excel3.columns = one_list
excel4.columns = one_list


# 给"Compound"增加表名
material = list(excel1["Compound"])
for i in range(len(material)):
    excel1.iloc[i, 0] = excel1_name[:-5] + "_" + excel1.iloc[i, 0]  # [:-5]:去除".xlsx"

material = list(excel2["Compound"])
for i in range(len(material)):
    excel2.iloc[i, 0] = excel2_name[:-5] + "_" + excel2.iloc[i, 0]

material = list(excel3["Compound"])
for i in range(len(material)):
    excel3.iloc[i, 0] = excel3_name[:-5] + "_" + excel3.iloc[i, 0]

material = list(excel4["Compound"])
for i in range(len(material)):
    excel4.iloc[i, 0] = excel4_name[:-5] + "_" + excel4.iloc[i, 0]


# 合并四张表格
frames = [excel1, excel2, excel3, excel4]
result = pd.concat(frames)


# 结果保存为xlsx
if not os.path.exists(folder_out):  # 存放了三张表
    os.mkdir(folder_out)
writer = pd.ExcelWriter(folder_out + "/result_" + folder_source + ".xlsx")
result.to_excel(writer, 'Sheet1', index = False)  # 不输出行标号
writer.save()
print("计算用时: %.2fs."%(time.time() - time_start))