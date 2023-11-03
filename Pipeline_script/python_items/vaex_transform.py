import vaex
list_name=[]

for j in range(503):
    list_name.append(f'C{j}')
vaex.read_csv('/mnt/volume1/2023SRTP/library/TCRdb/Output/vaex/test_int_randomed.csv',convert=True, chunk_size=3000000,header=None,names=list_name)




