# import csv  
# import numpy as np  
  
# # 定义块大小  
# block_size = 100000  # 根据实际情况调整块大小  
  
# # 读取CSV文件并逐块处理  
# with open('/mnt/volume1/2023SRTP/library/TCRdb/Output/one_last.csv', 'r') as csv_file:  
#     reader = csv.reader(csv_file)  
#     data_blocks = []  
#     for row_block in reader:  
#         data_block=np.array(row_block,dtype=np.float16)
#         data_block = np.array(data_block, dtype=np.int8)  # 将行块转换为numpy数组  
#         data_blocks.append(data_block)  
  
#     # 将所有数据块拼接为单个numpy数组  
#     data_array = np.concatenate(data_blocks)  
  
# # 输出numpy数组  
# np.save('/mnt/volume1/2023SRTP/library/TCRdb/Output/ndarray2.npy',data_array)

import csv  
import numpy as np
  
# 读取CSV文件并逐行处理  
with open('/mnt/volume1/2023SRTP/library/TCRdb/Output/vaex/test_randomed.csv', 'r') as csv_file:  
    reader = csv.reader(csv_file)  
    for row in reader:  
        # 对每一行的数据进行处理  

        processed_row = np.array(row, dtype=np.float32)  # 假设我们要将每个字段转换为int类型  
        processed_row=np.array(processed_row,dtype=np.int8)
        # 将处理后的数据写入新的CSV文件  
        with open('/mnt/volume1/2023SRTP/library/TCRdb/Output/vaex/test_int_randomed.csv', 'a', newline='') as csv_file:  
            writer = csv.writer(csv_file)  
            writer.writerow(processed_row)

# import numpy as np # linear algebra
# import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# def reduce_mem_usage(props):
#     start_mem_usg = props.memory_usage().sum() / 1024**2 
#     print("Memory usage of properties dataframe is :",start_mem_usg," MB")
#     NAlist = [] # Keeps track of columns that have missing values filled in. 
#     for col in props.columns:
#         if props[col].dtype != object:  # Exclude strings
            
#             # Print current column type
#             print("******************************")
#             print("Column: ",col)
#             print("dtype before: ",props[col].dtype)
            
#             # make variables for Int, max and min
#             IsInt = False
#             mx = props[col].max()
#             mn = props[col].min()
            
#             # Integer does not support NA, therefore, NA needs to be filled
#             if not np.isfinite(props[col]).all(): 
#                 NAlist.append(col)
#                 props[col].fillna(mn-1,inplace=True)  
                   
#             # test if column can be converted to an integer
#             asint = props[col].fillna(0).astype(np.int64)
#             result = (props[col] - asint)
#             result = result.sum()
#             if result > -0.01 and result < 0.01:
#                 IsInt = True

            
#             # Make Integer/unsigned Integer datatypes
#             if IsInt:
#                 if mn >= 0:
#                     if mx < 255:
#                         props[col] = props[col].astype(np.uint8)
#                     elif mx < 65535:
#                         props[col] = props[col].astype(np.uint16)
#                     elif mx < 4294967295:
#                         props[col] = props[col].astype(np.uint32)
#                     else:
#                         props[col] = props[col].astype(np.uint64)
#                 else:
#                     if mn > np.iinfo(np.int8).min and mx < np.iinfo(np.int8).max:
#                         props[col] = props[col].astype(np.int8)
#                     elif mn > np.iinfo(np.int16).min and mx < np.iinfo(np.int16).max:
#                         props[col] = props[col].astype(np.int16)
#                     elif mn > np.iinfo(np.int32).min and mx < np.iinfo(np.int32).max:
#                         props[col] = props[col].astype(np.int32)
#                     elif mn > np.iinfo(np.int64).min and mx < np.iinfo(np.int64).max:
#                         props[col] = props[col].astype(np.int64)    
            
#             # Make float datatypes 32 bit
#             else:
#                 props[col] = props[col].astype(np.float32)
            
#             # Print new column type
#             print("dtype after: ",props[col].dtype)
#             print("******************************")
    
#     # Print final result
#     print("___MEMORY USAGE AFTER COMPLETION:___")
#     mem_usg = props.memory_usage().sum() / 1024**2 
#     print("Memory usage is: ",mem_usg," MB")
#     print("This is ",100*mem_usg/start_mem_usg,"% of the initial size")
#     return props, NAlist

