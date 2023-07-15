import numpy as np
import FinanceDataReader as fdr
import ML_RoboStockbuyer as stock

year_range = 1
Today = 20230315
start_day = str(int(Today) - year_range*10000)

stock = fdr.StockListing('KOSPI')
Find_id = stock['Name']
cmp_code = stock['Code']


iid = int(Find_id.index[np.where(Find_id == '삼성전자')[0][0]])
cmp = cmp_code[iid]
data1 = fdr.DataReader(cmp, start_day, str(Today))
print(data1.columns)
DF_NP = np.array(data1.values)[:, :5]
print(DF_NP.shape)
print(DF_NP)
Close_slice = data1['Close']
print(Close_slice)
print('-------------------------------')