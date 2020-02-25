#!/usr/bin/python3

#################################################################################################################################
#备注
#倪新鹏 <=pb19030816
#郑遣俊 >pb19030816 and <=pb19111696
#陈昊天 >pb19111696
#################################################################################################################################
import os
import pandas as pd
import numpy as np
#全局变量
week="一"
path=week
#这里保存需要忽略的文件名
rmignore=[]

files=os.listdir(path)
filename='作业'+week+'.csv'

def ismygroup(id):
    #用于选择自己分组的作业
    if id<='pb19030816':
        return True
    else:
        return False

if os.path.exists(filename):
    hw=pd.read_csv(filename)
    hw=hw.dropna(subset=['score'])
else:
    hw=pd.DataFrame(columns=['id','score','comment'])

for file in files:
    if file not in rmignore and week not in file or file[-4:]=='.txt'or file[-4:]=='.zip':
        #删除下载附带的的txt文件
        os.remove(os.path.join(path,file))
    else:
        id=file.split('_')[1]
        if id not in hw['id'].values and ismygroup(id):
            new={'id':id,'score': np.nan,'comment':np.nan}
            hw=hw.append(new,ignore_index=True)
            hw.sort_values(by='id').to_csv(filename,index=False)
        else:
            os.remove(os.path.join(path,file))