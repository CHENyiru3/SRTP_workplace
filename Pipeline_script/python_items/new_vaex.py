import vaex
df =vaex.open('/mnt/volume1/2023SRTP/library/TCRdb/Output/vaex/result/second_one_last.csv_chunk_159.hdf5')
print(df['C503'].values)
