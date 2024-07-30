import pandas as pd
from scipy.stats import pearsonr
class get_everyday_data:
    def __init__(self, data, Time_column, power_column, yb_power_column, fzd_column, window_size):
        self.data = data
        self.power = power_column
        self.fzd = fzd_column
        self.time = Time_column
        self.window_size = window_size
        self.yb_power = yb_power_column

    def judge(self, value):
        if value == 0:
            return 0
        elif value > 0:
            return 1
        elif value < 0:
            return -1

    def get_positive_and_negative(self, value_1, value_2):
        sub_power = []
        sub_fzd = []


        return sub_power, sub_fzd


    def calculate_blocks(self,df):
        # 计算滚动均值和滚动标准偏差并检测平台，通过修改threshold_std和window_size来提升精确度
        window_size = 4  # 滚动窗口大小

        threshold_std = 0.01  # 标准偏差阈值


        # 对整个数据按天分类，对含有平台值的日期赋值key = 1

        return block_feature,rolling_std_feature

    def positive_and_negative_matching(self, value_1, value_2):

        return 1 - (a / (lenth - 1))

    def Get_Everyday_PowerAndRad(self):

        for index in unique_time_index:

            # 实测功率与实测辐照度的每天绝对差值

            #  实测功率与预测功率的每天绝对差值

            # 实测功率、实测辐照度、预测功率每天的值

            if (temp_rt_power.values == 0).all() or (temp_fzd.values == 0).all() or (temp_yb_power.values == 0).all():
                corr_rt_power_with_fzd = 0
                corr_rt_power_with_yb_power = 0
            else:
                corr_rt_power_with_fzd, p_value_1 = pearsonr(temp_rt_power.values, temp_fzd.values)
                corr_rt_power_with_yb_power, p_value_2 = pearsonr(temp_yb_power.values, temp_fzd.values)
            # 实测功率与实测辐照度的所有特征量计算

            if max_fzd == 0:
                ratio_rtpowermax_and_fzdmax = 0
            else:
                ratio_rtpowermax_and_fzdmax = max_rt_power / max_fzd
            if mean_fzd == 0:
                ratio_rtpowermean_and_fzdmean = 0
            else:
                ratio_rtpowermean_and_fzdmean = mean_rt_power / mean_fzd
            match_rtpower_with_fzd = self.positive_and_negative_matching(temp_rt_power.values, temp_fzd.values)

            #  实测功率与预测功率的所有特征量计算

            if max_yb_power == 0:
                ratio_rtpowermax_and_ybpowermax = 0
            else:
                ratio_rtpowermax_and_ybpowermax = max_rt_power / max_yb_power
            if mean_yb_power == 0:
                ratio_rtpowermean_and_ybpowermean = 0
            else:
                ratio_rtpowermean_and_ybpowermean = mean_rt_power / mean_yb_power
            match_rtpower_with_ybpower = self.positive_and_negative_matching(temp_rt_power.values, temp_yb_power.values)

            temp_dataframe_rtpower_with_fzd = pd.DataFrame({
                'date': index,
                'rt_power_max': max_rt_power,
                'rt_fzd_max': max_fzd,
                'rt_power_mean': mean_rt_power,
                'rt_fzd_mean': mean_fzd,
                'max_ratio': ratio_rtpowermax_and_fzdmax,
                'mean_ratio': ratio_rtpowermean_and_fzdmean,
                'pearsonr': corr_rt_power_with_fzd,
                'mean_of_diff': mean_rt_power_with_fzd,
                'std_of_diff': std_rt_power_with_fzd,
                'trend_matching_value': match_rtpower_with_fzd
            }, index=[0])
            temp_dataframe_rtpower_with_ybpower = pd.DataFrame({
                'date': index,
                'rt_power_max': max_rt_power,
                'yb_power_max': max_yb_power,
                'rt_power_mean': mean_rt_power,
                'yb_power_mean': mean_yb_power,
                'max_ratio': ratio_rtpowermax_and_ybpowermax,
                'mean_ratio': ratio_rtpowermean_and_ybpowermean,
                'pearsonr': corr_rt_power_with_yb_power,
                'mean_of_diff': mean_rt_power_with_yb_power,
                'std_of_diff': std_rt_power_with_yb_power,
                'trend_matching_value': match_rtpower_with_ybpower
            }, index=[0])
            newfea_data_rtpower_with_fzd = pd.concat([newfea_data_rtpower_with_fzd, temp_dataframe_rtpower_with_fzd], ignore_index=True)
            newfea_data_rtpower_with_ybpower = pd.concat([newfea_data_rtpower_with_ybpower,  temp_dataframe_rtpower_with_ybpower], ignore_index=True)
            temp_dataframe_rtpower_with_fzd = pd.DataFrame()
            temp_dataframe_rtpower_with_ybpower = pd.DataFrame()
            # print(
            #     f'日期：{index}，实测功率最大值：{max_power:.4f}，预测功率最大值：{max_yb_power:.4f}，实测功率均值：{mean_power:.4f}，预测功率均值：{mean_yb_power:.4f}')
            # print(
            #     f'                  （实测功率比预测功率下） 最大值之比：{(max_power / max_yb_power):.4f}，均值之比：{(mean_power / mean_yb_power):.4f}')
            # print(
            #     f'                  （实测功率与辐照度下）皮尔森系数：{corr:.4f}，差值均值{mean:.4f}，差值标准差{std:.4f}，趋势匹配度：{a:.4f}')
            # print('')

        block_feature, rolling_std_feature = self.calculate_blocks(df)


        newfea_data_rtpower_with_fzd['mark'] = 0
        newfea_data_rtpower_with_ybpower['mark'] = 0
        return newfea_data_rtpower_with_fzd, newfea_data_rtpower_with_ybpower