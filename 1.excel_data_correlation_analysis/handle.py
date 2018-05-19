### 对excel数据作相关分析-统计全部数据
import os
import pandas as pd
import numpy as np
from tqdm import tqdm
from scipy.spatial.distance import pdist


excel_folder = "example"
excels = os.listdir(excel_folder)
if not os.path.exists("results"):
	os.mkdir("results")

for excel in tqdm(excels):
	df = pd.read_excel(excel_folder+"/"+excel)  # 默认第一个sheet
	# 参数定义
	num_pairs = 0  # 一共多少对距离相关
	compound1 = []
	compound2 = []
	correlation = []

	# 计算相关系数的绝对值
	compounds = list(df["Compound"])   # 所有的物质名称
	for index1, comp1 in enumerate(compounds):   # index1:第一种物质全局标号
		for index, comp2 in enumerate(compounds[index1+1:]):
			index2 = index1 + index + 1   # 第二种物质的全局标号
			data1 = list(df.loc[index1])[1:]
			data2 = list(df.loc[index2])[1:]
			corr_dis = pdist(np.vstack([data1, data2]), 'correlation')  # 相关距离，结果类似array([-1.])
			corr = abs((1 - corr_dis)[0])

			# 统计结果
			num_pairs += 1
			if index == 0:
				compound1.append(comp1)
			else:
				compound1.append("")
			compound2.append(comp2)
			correlation.append(corr)

	# 输出数据
	writer = pd.ExcelWriter("results/result_" + excel)
	data = {"compound1":compound1, "compound2":compound2, "correlation":correlation}
	output_data = pd.DataFrame(data, columns=['compound1','compound2','correlation'])
	output_data.to_excel(writer, 'Sheet1', index=False)  # 不输出行标号
	writer.save()

	print("%s: 共处理%d种物质, 计算%d个相关对."%(excel, len(compounds), num_pairs))

# 所有excel处理完毕
print("All done!")
