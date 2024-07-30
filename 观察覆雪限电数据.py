import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

from get_everyday_data import get_everyday_data

data = pd.read_csv('C:/Users/csy0e/Desktop/限电覆雪标记和清除/区域9_晋城_端泽二期光伏电站_78808000.csv')
power_scaler = MinMaxScaler()
fzd_scaler = MinMaxScaler()
yb_power_scaler = MinMaxScaler()
snow_scaler = MinMaxScaler()
data['sf_scalered'] = snow_scaler.fit_transform(np.array(data['sf']).reshape(-1, 1))
data['ori_rt_power_scalered'] = power_scaler.fit_transform(np.array(data['ori_rt_power']).reshape(-1, 1))
data['ori_yb_power_scalered'] = yb_power_scaler.fit_transform(np.array(data['ori_yb_power']).reshape(-1, 1))
data['rt_fzd_scalered'] = fzd_scaler.fit_transform(np.array(data['rt_fzd']).reshape(-1, 1))

everyday_data = get_everyday_data(data, 'dateTime', 'ori_rt_power_scalered', 'ori_yb_power_scalered', 'rt_fzd_scalered', window_size=10)

newfea_data_rtpower_with_fzd, newfea_data_rtpower_with_ybpower = everyday_data.Get_Everyday_PowerAndRad()

newfea_data_rtpower_with_fzd.to_csv('C:/Users/csy0e/Desktop/限电覆雪标记和清除/特征表/区域9_晋城_端泽二期光伏电站_78808000_实测功率与实测辐照度特征表.csv', index=False)
newfea_data_rtpower_with_ybpower.to_csv('C:/Users/csy0e/Desktop/限电覆雪标记和清除/特征表/区域9_晋城_端泽二期光伏电站_78808000_实测功率与预测功率特征表.csv', index=False)


# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.figure(figsize=(80,6))
# plt.plot(data['dateTime'], data['ori_rt_power_scalered'], c='b' ,label='实测功率')
# # plt.plot(data['dateTime'], data['rt_fzd_scalered'], c='r' ,label='辐照度')
# plt.plot(data['sf_scalered'], c='g', label='降雪量')
# # plt.plot(data['dateTime'], df['mark'], c='b')
# plt.plot(data['dateTime'], data['ori_yb_power_scalered'], c='r' ,label='预测功率')
# plt.xticks(data['dateTime'].values[::24], rotation=45, fontsize=10)
# plt.legend()
#
#
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.figure(figsize=(80,6))
# plt.plot(data['dateTime'], data['ori_rt_power_scalered'], c='b' ,label='实测功率')
# plt.plot(data['dateTime'], data['rt_fzd_scalered'], c='r' ,label='辐照度')
# plt.plot(data['sf_scalered'], c='g', label='降雪量')
# # plt.plot(data['dateTime'], df['mark'], c='b')
# # plt.plot(data['dateTime'], data['ori_yb_power_scalered'], c='b' ,label='预测功率')
# plt.xticks(data['dateTime'].values[::24], rotation=45, fontsize=10)
# plt.legend()