import dash
from dash import dcc, html, Input, Output, State
import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import plotly.graph_objects as go

from get_everyday_data import get_everyday_data


app = dash.Dash(__name__)

DATA_FOLDER = 'C:/Users/csy0e/Desktop/WORK/限电覆雪标记和清除/光伏单场站数据输出 分辨率（小时）/光伏单场站数据输出 分辨率（小时）'  # 原始数据地址
data_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith('.csv')]  # 读取csv文件
# mark_messages = []
app.layout = html.Div([
    html.H1("光伏数据标记工具", style={'textAlign': 'center'}),

    dcc.Dropdown(id='file-dropdown', options=[{'label': file, 'value': file} for file in data_files],
                 placeholder='选择数据表', style={'width': '100%', 'margin-bottom': '20px'}),

    dcc.RadioItems(
        id='chart-type',
        options=[
            {'label': '实测功率与实测辐照度走向', 'value': 'rtpower_and_fzd'},
            {'label': '实测功率与预测走向', 'value': 'rtpower_and_ybpower'}
        ],
        value='rtpower_and_fzd',  # 默认选项
        labelStyle={'display': 'block', 'margin-bottom': '10px', 'width': '10', 'height': '30%'}  # 每个选项单独一行
    ),

    html.Div(
        dcc.Graph(
            id='line_chart',
            style={'width': '3000px', 'height': '600px'}  # 设置图表的固定宽度和高度
        ),
        style={'width': '1500px', 'height': '600px', 'overflow': 'auto'}  # 设置容器的固定宽度和高度，并启用滚动条
    ),

    dcc.Input(id='date-input', type='text', placeholder='输入日期 (YYYY-MM-DD)',
              style={'width': '50%', 'height': '100%', 'margin-bottom': '20px', 'margin-top': '30px'}),

    dcc.Dropdown(id='mark-dropdown', options=[
        {'label': '限电', 'value': 1},
        {'label': '覆雪', 'value': 2},
        {'label': '不确定', 'value': 3}
    ], placeholder='选择标记类型', style={'width': '50%', 'margin-bottom': '20px'}),
    html.Button('标记', id='mark-button', n_clicks=0,
                style={'margin-bottom': '20px', 'margin-right': '60px', 'width': '10%', 'height': '10%'}),
    # html.Button('修改标记', id='modify-button', n_clicks=0,
    #             style={'margin-bottom': '20px', 'margin-right': '20px', 'width': '10%', 'height': '30%'}),
    # dcc.Dropdown(id='output-dropdown', options=[
    #     {'label': msg, 'value': msg} for msg in mark_messages
    # ], placeholder='标记信息'),
    html.Button('保存标记文件', id='save-button', n_clicks=0,
                style={'margin-bottom': '20px', 'margin-right': '20px', 'width': '10%', 'height': '30%'}),

    html.Div(id='output')
], style={'width': '100%', 'height': '100%'})


# 假设您有一个全局变量来存储标记数据
marked_data_1 = pd.DataFrame()
marked_data_2 = pd.DataFrame()
mark_date = []
@app.callback(
    Output('output', 'children'),
    Input('mark-button', 'n_clicks'),
    Input('save-button', 'n_clicks'),
    State('date-input', 'value'),
    State('file-dropdown', 'value'),
    State('mark-dropdown', 'value')
)
def save_mark(n_clicks_mark, n_clicks_save, date, selected_file, mark_value):
    global marked_data_1  # 使用全局变量
    global marked_data_2  # 使用全局变量

    if selected_file is None:
        return "请先选择一个 CSV 文件"

    # 读取数据表


    # 数据处理


    if n_clicks_mark > 0:
        if not (date and selected_file and mark_value):
            return "请填写所有字段！"

        # 更新对应日期的标记


        # 将新标记合并到标记数据中

        type = {
            1: '限电',
            2: '覆雪',
            3: '不确定'
        }
        print(f'成功标记场站{selected_file}日期：{date}，标记类型为{type[pd.to_numeric(mark_value)]}')
        mark_date.append(date)
    if n_clicks_save > 0:
        if marked_data_1.empty:
            return "没有标记数据可保存！"

        dir = 'C:/Users/csy0e/Desktop/限电覆雪标记和清除/已标记特征表'
        save_path_fea_1 = os.path.join(dir,
                                        selected_file + '_实测功率与实测辐照度特征表.csv')  # 保存的路径
        save_path_fea_2 = os.path.join(dir,
                                        selected_file + '_实测功率与预测功率特征表.csv')   # 保存的路径

        # 保存所有标记数据


        newfea_data_rtpower_with_fzd.to_csv(save_path_fea_1, index=False)
        newfea_data_rtpower_with_ybpower.to_csv(save_path_fea_2, index=False)

        return f"已保存{dir}/{selected_file}文件"


    return ""




@app.callback(
    Output('line_chart', 'figure'),
    Input('file-dropdown', 'value'),
    Input('chart-type', 'value')
)
def update_graph(selected_file, chart_type):
    if selected_file is None:
        return go.Figure()

    # 读取数据


    width = 12000
    height = 600

    # 图标设置
    figure = go.Figure()

    if chart_type == 'rtpower_and_fzd':  # 选择实测功率与实测辐照度的图表


    elif chart_type == 'rtpower_and_ybpower':  # 选择实测功率与预测功率的图表

    return figure


if __name__ == '__main__':
    app.run_server(debug=True)
