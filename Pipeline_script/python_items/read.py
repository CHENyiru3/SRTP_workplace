

import numpy as np  
  
# 指定CSV文件路径  
file_path = '/mnt/volume1/2023SRTP/library/TCRdb/Output/new_new_merged_ncbi.csv'  
  
# 定义每列的数据类型  
dtype = (np.str_,np.str_,np.str_,np.str_,np.str_)
col=(5,6,7,8,9)
  
# 使用NumPy的genfromtxt函数读取CSV文件  
data = np.genfromtxt(file_path, delimiter=',', usecols=col,dtype=dtype)  

# 打印读取的数据  
print(data)