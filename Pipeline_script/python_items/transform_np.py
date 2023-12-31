import numpy as np
import csv
import pickle
import pandas as pd
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

tissue_list = ['Lymph node', 'Esophagus, Tumor, Infiltrating cell', 'Lung, Infiltrating cell, Tumor-center', 'Skin', 
               'Bone marrow', 'Tumor-adjacent, Liver', 'Tumor, Infiltrating cell', 'Thymus', 'Synovial fluid', 
               'Tumor, Lung, Infiltrating cell', 'Liver, Infiltrating cell', 'Blood', 'Tumor, Lipoma, Infiltrating cell', 
               'Tumor, Infiltrating cell, Breast', 'Duodenum', 'Lung', 'Breast, Tumor-adjacent', 'Lung, Tumor, Infiltrating cell', 
               'Bronchoalveolar lavage', 'Axillary lymph node', 'Breast, Tumor, Infiltrating cell', 'Unknown', 'PBMC', 
               'Salivary gland', 'Lung, Tumor-adjacent, Infiltrating cell', 'Brain, Tumor, Infiltrating cell', 
               'Lung, Infiltrating cell, Tumor-margin', 'Cord blood', 'Tumor-adjacent, Esophagus']

#定义打分矩阵
blosum62_20aa = {
        'A': np.array(( 4, -1, -2, -2,  0, -1, -1,  0, -2, -1, -1, -1, -1, -2, -1,  1,  0, -3, -2,  0)),
        'R': np.array((-1,  5,  0, -2, -3,  1,  0, -2,  0, -3, -2,  2, -1, -3, -2, -1, -1, -3, -2, -3 )),
        'N': np.array((-2,  0,  6,  1, -3,  0,  0,  0,  1, -3, -3,  0, -2, -3, -2,  1,  0, -4, -2, -3)),
        'D': np.array((-2, -2,  1,  6, -3,  0,  2, -1, -1, -3, -4, -1, -3, -3, -1,  0, -1, -4, -3, -3)),
        'C': np.array(( 0, -3, -3, -3,  9, -3, -4, -3, -3, -1, -1, -3, -1, -2, -3, -1, -1, -2, -2, -1)),
        'Q': np.array((-1,  1,  0,  0, -3,  5,  2, -2,  0, -3, -2,  1,  0, -3, -1,  0, -1, -2, -1, -2)),
        'E': np.array((-1,  0,  0,  2, -4,  2,  5, -2,  0, -3, -3,  1, -2, -3, -1,  0, -1, -3, -2, -2)),
        'G': np.array(( 0, -2,  0, -1, -3, -2, -2,  6, -2, -4, -4, -2, -3, -3, -2,  0, -2, -2, -3, -3)),
        'H': np.array((-2,  0,  1, -1, -3,  0,  0, -2,  8, -3, -3, -1, -2, -1, -2, -1, -2, -2,  2, -3)),
        'I': np.array((-1, -3, -3, -3, -1, -3, -3, -4, -3,  4,  2, -3,  1,  0, -3, -2, -1, -3, -1,  3)),
        'L': np.array((-1, -2, -3, -4, -1, -2, -3, -4, -3,  2,  4, -2,  2,  0, -3, -2, -1, -2, -1,  1)),
        'K': np.array((-1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -2,  5, -1, -3, -1,  0, -1, -3, -2, -2)),
        'M': np.array((-1, -1, -2, -3, -1,  0, -2, -3, -2,  1,  2, -1,  5,  0, -2, -1, -1, -1, -1,  1)),
        'F': np.array((-2, -3, -3, -3, -2, -3, -3, -3, -1,  0,  0, -3,  0,  6, -4, -2, -2,  1,  3, -1)),
        'P': np.array((-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -1, -2, -4,  7, -1, -1, -4, -3, -2)),
        'S': np.array(( 1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -2,  0, -1, -2, -1,  4,  1, -3, -2, -2)),
        'T': np.array(( 0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -1, -1, -1, -2, -1,  1,  5, -2, -2,  0)),
        'W': np.array((-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -3, -1,  1, -4, -3, -2, 11,  2, -3)),
        'Y': np.array((-2, -2, -2, -3, -2, -1, -2, -3,  2, -1, -1, -2, -1,  3, -3, -2, -2,  2,  7, -1)),
        'V': np.array(( 0, -3, -3, -3, -1, -2, -2, -3, -3,  3,  1, -2,  1, -1, -2, -2,  0, -3, -1,  4))}

#different from what was written in previous file. In here this function can only detect and deal with single sequence
def encodeBlosum(aa_seq,blosum):
    num=0
    e_seq=np.zeros((25,20),dtype=dt)
    for aa in aa_seq:
        if aa in blosum:
            e_seq[num]=blosum[aa]
            num+=1
            if num==24:
                break
        else:
            print('warning!')

    e_flat_seq=e_seq.reshape(1,500)
    return e_flat_seq

def find_disease_row(disease):
    with open("/mnt/volume1/2023SRTP/library/cyr/code_meida_data/NCBI_disease.csv", "r") as diseases:
        diseases_reader = csv.reader(diseases)
        for row_num, row in enumerate(diseases_reader):
            if row[0] == disease:
                return row_num 
        return -1 

def find_celltype_row(celltype):
    with open("/mnt/volume1/2023SRTP/library/cyr/code_meida_data/NCBI_celltype.csv", "r") as celltypes:
        celltypes_reader = csv.reader(celltypes)
        for row_num, row in enumerate(celltypes_reader):
            if row[0] == celltype:
                return row_num 
        return -1 

def find_tissue(tissue):
    for id_tissue, tissue_name in enumerate(tissue_list):
        if tissue == tissue_name:
            return id_tissue
    return -1
dt = np.dtype(np.int32)
transform_result = np.array([],dtype=dt)

with open('/mnt/volume1/2023SRTP/library/TCRdb/Output/new_new_merged_ncbi.csv', 'r') as input_file, open('/mnt/volume1/2023SRTP/library/TCRdb/Output/one_last.csv','a') as output_file:
    next(input_file)
    input_reader = csv.reader(input_file)
    id = 0
    output_writer = csv.writer(output_file)
    for row in input_reader:
        cdr3=encodeBlosum(row[5],blosum62_20aa)
        disease=find_disease_row(row[7])
        tissue=find_tissue(row[8])
        celltype=find_celltype_row(row[9])
        tem_np=np.array([disease,tissue,celltype],dtype=dt)
        info= np.append(cdr3,tem_np)
        transform_result=np.concatenate((transform_result,info),axis=0)
        id += 1
        print(id)
np.save('/mnt/volume1/2023SRTP/library/TCRdb/Output/ndarray.npy',transform_result)



# info_pd=reduce_mem_usage(info_pd)[0]

# with open('/mnt/volume1/2023SRTP/library/TCRdb/Output/Pickle/ncbi/simpledata.pkl','wb') as file:
#     pickle.dump(info_pd,file)
    # if id % 1000 == 0:
    #     with open(f'/mnt/volume1/2023SRTP/library/TCRdb/Output/Pickle/ncbi/tfd{id//1000}.pkl', 'wb') as file:
    # with open('/mnt/volume1/2023SRTP/library/TCRdb/Output/Pickle/ncbi/traindata.pkl','wb') as file:
    #     pickle.dump(info_pd, file)



