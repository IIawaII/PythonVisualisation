import dash
from dash import dcc, html, Input, Output, State, callback
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
import os
warnings.filterwarnings('ignore')

# 初始化Dash应用
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# 定义颜色主题
COLOR_THEME = {
    'primary': '#1A5276',
    'secondary': '#2874A6',
    'accent': '#3498DB',
    'light': '#85C1E9',
    'background': '#F8F9FA',
    'text': '#2C3E50',
    'success': '#27AE60',
    'warning': '#F39C12',
    'danger': '#E74C3C'
}

# 区域映射
REGION_MAPPING = {
    '华北': ['北京市', '天津市', '河北省', '山西省', '内蒙古自治区'],
    '华东': ['上海市', '江苏省', '浙江省', '安徽省', '福建省', '江西省', '山东省'],
    '华南': ['广东省', '广西壮族自治区', '海南省'],
    '华中': ['河南省', '湖北省', '湖南省'],
    '西南': ['重庆市', '四川省', '贵州省', '云南省', '西藏自治区'],
    '西北': ['陕西省', '甘肃省', '青海省', '宁夏回族自治区', '新疆维吾尔自治区'],
    '东北': ['辽宁省', '吉林省', '黑龙江省']
}

# 数据缓存
_DATA_CACHE = None

def get_data_path(filename):
    """获取数据文件的绝对路径"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, '..', '数据生成', filename)

def categorize_product(product_name):
    """根据商品名称中的关键词进行产品分类"""
    if pd.isna(product_name):
        return '其他'

    product_name = str(product_name).upper()

    category_mapping = {
        'POLO衫': ['POLO'],
        '短裤': ['短裤'],
        '休闲衫': ['休闲衬衫'],
        '风衣': ['风衣'],
        '卫衣': ['卫衣'],
        'T恤': ['T恤'],
        '衬衫': ['衬衫'],
        '羽绒服': ['羽绒服'],
        '裤子': ['休闲裤'],
        '家居服': ['家居服'],
        '连衣裙': ['连衣裙'],
        '外套': ['外套']
    }

    for category, keywords in category_mapping.items():
        for keyword in keywords:
            if keyword in product_name:
                return category

    return '其他'

def apply_filters(df, filters):
    """统一应用筛选条件到数据集"""
    df_filtered = df.copy()
    
    # 区域筛选
    if filters.get('region') and filters['region'] != 'all':
        df_filtered = df_filtered[df_filtered['区域'] == filters['region']]
    
    # 时间筛选
    if filters.get('time') and filters['time'] != 'all':
        days = int(filters['time'].replace('d', ''))
        cutoff_date = datetime.now() - timedelta(days=days)
        df_filtered = df_filtered[df_filtered['下单时间'] >= cutoff_date]
    
    # 产品分类筛选
    if filters.get('category') and filters['category'] != 'all':
        df_filtered = df_filtered[df_filtered['产品分类'] == filters['category']]
    
    return df_filtered

def load_data():
    """加载数据（带缓存）"""
    global _DATA_CACHE

    if _DATA_CACHE is not None:
        return _DATA_CACHE

    try:
        print("正在加载数据文件...")
        df_orders = pd.read_csv(get_data_path('erp_order.csv'), encoding='utf-8-sig')

        # 数据清洗和处理
        df_orders = df_orders[df_orders['省份'].notna()].copy()

        def map_region(province):
            for region, provinces in REGION_MAPPING.items():
                if province in provinces:
                    return region
            return '其他'

        df_orders['区域'] = df_orders['省份'].apply(map_region)
        df_orders['产品分类'] = df_orders['商品名称'].apply(categorize_product)
        df_orders['下单时间'] = pd.to_datetime(df_orders['下单时间'])
        df_orders['下单月份'] = df_orders['下单时间'].dt.to_period('M').astype(str) # type: ignore

        _DATA_CACHE = {
            'orders': df_orders
        }

        print(f"数据加载成功 - 订单: {len(df_orders)}")
        return _DATA_CACHE

    except Exception as e:
        print(f"数据加载失败: {e}")
        return None

# 页面布局
def create_layout():
    return html.Div([
        html.Div([
            html.H1('电商数据可视化交互看板',
                   className='dashboard-header',
                   style={
                       'color': COLOR_THEME['primary'],
                       'textAlign': 'center',
                       'marginBottom': '30px',
                       'fontWeight': 'bold',
                       'fontSize': '2.5rem'
                   }),
            html.P('实时监控订单、销售、产品等关键指标',
                   style={
                       'textAlign': 'center',
                       'color': COLOR_THEME['text'],
                       'marginBottom': '40px',
                       'fontSize': '1.1rem'
                   })
        ]),

        html.Div([
            html.Div([
                html.Label('选择区域:', style={'fontWeight': 'bold', 'marginRight': '10px'}),
                dcc.Dropdown(
                    id='region-filter',
                    options=[
                        {'label': '全部区域', 'value': 'all'},
                        {'label': '华北', 'value': '华北'},
                        {'label': '华东', 'value': '华东'},
                        {'label': '华南', 'value': '华南'},
                        {'label': '华中', 'value': '华中'},
                        {'label': '西南', 'value': '西南'},
                        {'label': '西北', 'value': '西北'},
                        {'label': '东北', 'value': '东北'}
                    ],
                    value='all',
                    style={'width': '150px', 'display': 'inline-block'}
                )
            ], style={'display': 'inline-block', 'marginRight': '20px'}),

            html.Div([
                html.Label('时间范围:', style={'fontWeight': 'bold', 'marginRight': '10px'}),
                dcc.Dropdown(
                    id='time-filter',
                    options=[
                        {'label': '全部时间', 'value': 'all'},
                        {'label': '最近30天', 'value': '30d'},
                        {'label': '最近60天', 'value': '60d'},
                        {'label': '最近90天', 'value': '90d'}
                    ],
                    value='all',
                    style={'width': '120px', 'display': 'inline-block'}
                )
            ], style={'display': 'inline-block', 'marginRight': '20px'}),

            html.Div([
                html.Label('产品分类:', style={'fontWeight': 'bold', 'marginRight': '10px'}),
                dcc.Dropdown(
                    id='category-filter',
                    options=[{'label': '全部分类', 'value': 'all'}],
                    value='all',
                    style={'width': '150px', 'display': 'inline-block'}
                )
            ], style={'display': 'inline-block'})
        ], style={
            'backgroundColor': COLOR_THEME['background'],
            'padding': '20px',
            'borderRadius': '10px',
            'marginBottom': '30px',
            'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'
        }),

        html.Div(id='kpi-cards', style={'marginBottom': '30px'}),

        html.Div([
            html.Div([dcc.Graph(id='order-trend-chart', style={'width': '100%'})], 
                    style={'padding': '10px', 'marginBottom': '20px'}),
            html.Div([dcc.Graph(id='region-distribution-chart', style={'width': '100%'})], 
                    style={'padding': '10px', 'marginBottom': '20px'}),
            html.Div([dcc.Graph(id='category-performance-chart', style={'width': '100%'})], 
                    style={'padding': '10px', 'marginBottom': '20px'}),
            html.Div([dcc.Graph(id='sales-funnel-chart', style={'width': '100%'})], 
                    style={'padding': '10px', 'marginBottom': '20px'}),
            html.Div([dcc.Graph(id='product-analysis-chart', style={'width': '100%'})], 
                    style={'padding': '10px', 'marginBottom': '20px'})
        ]),

            html.Div([
                # 标题行：左边标题，右边显示条数选择
                html.Div([
                    html.H3(
                        '订单详情',
                        style={
                            'color': COLOR_THEME['primary'],
                            'margin': '0',
                            'fontWeight': 'bold'
                        }
                    ),
                    html.Div([
                        html.Label(
                            '显示条数：',
                            style={
                                'fontWeight': 'bold',
                                'marginRight': '8px',
                                'fontSize': '0.9rem'
                            }
                        ),
                        dcc.Dropdown(
                            id='records-count-filter',
                            options=[
                                {'label': '20 条', 'value': 20},
                                {'label': '50 条', 'value': 50},
                                {'label': '100 条', 'value': 100},
                                {'label': '200 条', 'value': 200}
                            ],
                            value=50,
                            clearable=False,
                            style={
                                'width': '120px',
                                'fontSize': '0.9rem'
                            }
                        )
                    ], style={
                        'display': 'flex',
                        'alignItems': 'center',
                        'gap': '8px'
                    })
                ], style={
                    'width': '100%',
                    'marginBottom': '15px',
                    'display': 'flex',
                    'justifyContent': 'space-between',
                    'alignItems': 'center'
                }),

                # 表格容器
                html.Div(id='orders-table')
            ], style={
                'marginTop': '30px',
                'padding': '20px',
                'backgroundColor': COLOR_THEME['background'],
                'borderRadius': '10px',
                'boxShadow': '0 2px 4px rgba(0,0,0,0.05)'
            })
    ], style={
        'fontFamily': 'Arial, sans-serif',
        'padding': '20px',
        'maxWidth': '1400px',
        'margin': '0 auto',
        'backgroundColor': 'white'
    })

# 创建KPI卡片
def create_kpi_cards(data, filters=None):
    if not data:
        return html.Div('数据加载中...')

    df_orders = apply_filters(data['orders'], filters) if filters else data['orders'].copy()

    total_orders = len(df_orders)
    total_revenue = df_orders['商品金额'].sum() if '商品金额' in df_orders.columns else 0
    total_customers = df_orders['全渠道用户ID'].nunique() if '全渠道用户ID' in df_orders.columns else 0
    avg_order_value = total_revenue / total_orders if total_orders > 0 else 0

    kpi_cards = html.Div([
        html.Div([
            html.Div([
                html.H4(f"{int(total_orders):,}",
                       style={'color': COLOR_THEME['primary'], 'margin': '0', 'fontSize': '2rem'}),
                html.P('总订单数',
                       style={'color': COLOR_THEME['text'], 'margin': '5px 0 0 0', 'fontSize': '0.9rem'})
            ]),
            html.Div(style={'backgroundColor': COLOR_THEME['light'], 'width': '4px', 'margin': '0 15px'})
        ], style={'backgroundColor': COLOR_THEME['background'], 'padding': '20px', 'borderRadius': '10px',
                 'display': 'flex', 'alignItems': 'center', 'flex': '1', 'margin': '0 10px',
                 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}),

        html.Div([
            html.Div([
                html.H4(f'¥{int(total_revenue):,}',
                       style={'color': COLOR_THEME['success'], 'margin': '0', 'fontSize': '2rem'}),
                html.P('总收入',
                       style={'color': COLOR_THEME['text'], 'margin': '5px 0 0 0', 'fontSize': '0.9rem'})
            ]),
            html.Div(style={'backgroundColor': COLOR_THEME['success'], 'width': '4px', 'margin': '0 15px'})
        ], style={'backgroundColor': COLOR_THEME['background'], 'padding': '20px', 'borderRadius': '10px',
                 'display': 'flex', 'alignItems': 'center', 'flex': '1', 'margin': '0 10px',
                 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}),

        html.Div([
            html.Div([
                html.H4(f"{int(total_customers):,}",
                       style={'color': COLOR_THEME['warning'], 'margin': '0', 'fontSize': '2rem'}),
                html.P('总客户数',
                       style={'color': COLOR_THEME['text'], 'margin': '5px 0 0 0', 'fontSize': '0.9rem'})
            ]),
            html.Div(style={'backgroundColor': COLOR_THEME['warning'], 'width': '4px', 'margin': '0 15px'})
        ], style={'backgroundColor': COLOR_THEME['background'], 'padding': '20px', 'borderRadius': '10px',
                 'display': 'flex', 'alignItems': 'center', 'flex': '1', 'margin': '0 10px',
                 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'}),

        html.Div([
            html.Div([
                html.H4(f'¥{int(avg_order_value):,}',
                       style={'color': COLOR_THEME['secondary'], 'margin': '0', 'fontSize': '2rem'}),
                html.P('平均订单价值',
                       style={'color': COLOR_THEME['text'], 'margin': '5px 0 0 0', 'fontSize': '0.9rem'})
            ]),
            html.Div(style={'backgroundColor': COLOR_THEME['secondary'], 'width': '4px', 'margin': '0 15px'})
        ], style={'backgroundColor': COLOR_THEME['background'], 'padding': '20px', 'borderRadius': '10px',
                 'display': 'flex', 'alignItems': 'center', 'flex': '1', 'margin': '0 10px',
                 'boxShadow': '0 2px 4px rgba(0,0,0,0.1)'})
    ], style={'display': 'flex', 'justifyContent': 'space-between', 'flexWrap': 'wrap'})

    return kpi_cards

# 创建订单趋势图
def create_order_trend_chart(data, filters):
    if not data:
        return go.Figure().update_layout(title='数据加载中...')

    df_orders = apply_filters(data['orders'], filters) if filters else data['orders'].copy()

    if filters and filters.get('time') and filters['time'] != 'all':
        df_orders['下单日期'] = df_orders['下单时间'].dt.date
        daily_orders = df_orders.groupby('下单日期').agg({
            '内部订单号': 'count',
            '商品金额': 'sum'
        }).reset_index()
        daily_orders.columns = ['日期', '订单数量', '销售金额']
        daily_orders = daily_orders.sort_values('日期')

        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(x=daily_orders['日期'], y=daily_orders['订单数量'], 
                                mode='lines+markers', name='订单数量',
                                line=dict(color=COLOR_THEME['primary'], width=3)),
                     secondary_y=False)
        fig.add_trace(go.Scatter(x=daily_orders['日期'], y=daily_orders['销售金额'], 
                                mode='lines+markers', name='销售金额',
                                line=dict(color=COLOR_THEME['success'], width=3)),
                     secondary_y=True)
        fig.update_xaxes(title_text="日期")
        fig.update_yaxes(title_text="订单数量", secondary_y=False)
        fig.update_yaxes(title_text="销售金额 (¥)", secondary_y=True)
    else:
        monthly_orders = df_orders.groupby('下单月份').agg({
            '内部订单号': 'count',
            '商品金额': 'sum'
        }).reset_index()
        monthly_orders.columns = ['月份', '订单数量', '销售金额']

        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(x=monthly_orders['月份'], y=monthly_orders['订单数量'], 
                                mode='lines+markers', name='订单数量',
                                line=dict(color=COLOR_THEME['primary'], width=3)),
                     secondary_y=False)
        fig.add_trace(go.Scatter(x=monthly_orders['月份'], y=monthly_orders['销售金额'], 
                                mode='lines+markers', name='销售金额',
                                line=dict(color=COLOR_THEME['success'], width=3)),
                     secondary_y=True)
        fig.update_xaxes(title_text="月份")
        fig.update_yaxes(title_text="订单数量", secondary_y=False)
        fig.update_yaxes(title_text="销售金额 (¥)", secondary_y=True)

    fig.update_layout(
        title='订单趋势分析',
        title_x=0.5,
        height=500,
        showlegend=True,
        plot_bgcolor='white',
        xaxis_title_font_size=12,
        yaxis_title_font_size=12,
        title_font_size=16
    )
    return fig

# 创建区域分布图
def create_region_distribution_chart(data, filters):
    if not data:
        return go.Figure().update_layout(title='数据加载中...')

    df_orders = apply_filters(data['orders'], filters) if filters else data['orders'].copy()

    if filters and filters.get('region') and filters['region'] != 'all':
        region_data = df_orders.groupby('省份').size().reset_index(name='订单量')
        title = f"{filters['region']}省份订单分布"
    else:
        region_data = df_orders.groupby('区域').size().reset_index(name='订单量')
        title = '各区域订单分布'

    fig = px.bar(region_data, x=region_data.columns[0], y='订单量', 
                color='订单量', color_continuous_scale='Blues')
    fig.update_layout(
        title=title,
        title_x=0.5,
        height=400,
        showlegend=False,
        plot_bgcolor='white',
        xaxis_title_font_size=12,
        yaxis_title_font_size=12,
        title_font_size=16
    )
    return fig

# 产品分类绩效分析
def create_category_performance_chart(data, filters):
    if not data:
        return go.Figure().update_layout(title='数据加载中...')

    df_orders = apply_filters(data['orders'], filters) if filters else data['orders'].copy()

    category_stats = df_orders.groupby('产品分类').agg({
        '内部订单号': 'count',
        '商品金额': 'sum',
        '数量': 'sum'
    }).reset_index()
    category_stats.columns = ['产品分类', '订单数量', '销售金额', '销售数量']

    fig = px.scatter(category_stats, x='销售数量', y='销售金额', 
                    size='订单数量', color='产品分类', hover_data=['订单数量'])
    fig.update_layout(
        title='产品分类绩效分析',
        title_x=0.5,
        height=500,
        plot_bgcolor='white',
        xaxis_title_font_size=12,
        yaxis_title_font_size=12,
        title_font_size=16
    )
    return fig

# 销售漏斗图
def create_sales_funnel_chart(data, filters):
    if not data:
        return go.Figure().update_layout(title='数据加载中...')

    df_orders = apply_filters(data['orders'], filters) if filters else data['orders'].copy()

    funnel_data = [
        {'阶段': '下单', '数量': len(df_orders)},
        {'阶段': '已付款', '数量': len(df_orders[df_orders['状态'].isin(['已付款', '已发货', '已完成'])])},
        {'阶段': '已发货', '数量': len(df_orders[df_orders['状态'].isin(['已发货', '已完成'])])},
        {'阶段': '已完成', '数量': len(df_orders[df_orders['状态'] == '已完成'])}
    ]

    df_funnel = pd.DataFrame(funnel_data)
    fig = px.funnel(df_funnel, x='数量', y='阶段', title='订单状态转化漏斗')
    fig.update_layout(
        height=400,
        plot_bgcolor='white',
        title_x=0.5,
        title_font_size=16
    )
    return fig

# 产品分析图
def create_product_analysis_chart(data, filters):
    if not data:
        return {'data': [], 'layout': {'title': '数据加载中...'}}

    df_orders = data['orders'].copy()

    # 应用筛选条件
    if filters:
        if filters.get('region') and filters['region'] != 'all':
            df_orders = df_orders[df_orders['区域'] == filters['region']]

        if filters.get('time') and filters['time'] != 'all':
            days = int(filters['time'].replace('d', ''))
            cutoff_date = datetime.now() - timedelta(days=days)
            df_orders = df_orders[df_orders['下单时间'] >= cutoff_date]

        if filters.get('category') and filters['category'] != 'all':
            df_orders = df_orders[df_orders['产品分类'] == filters['category']]

    # 按商品名称统计销售额，取前10
    top_products = df_orders.groupby('商品名称').agg({
        '商品金额': 'sum',
        '数量': 'sum'
    }).reset_index()
    top_products = top_products.nlargest(min(10, len(top_products)), '商品金额')

    num_products = len(top_products)
    colors = np.linspace(0, 1, num_products)

    fig = go.Figure()

    for i in range(num_products):
        product_name = top_products['商品名称'].iloc[i]
        product_amount = top_products['商品金额'].iloc[i]
        color_value = colors[i]

        fig.add_trace(go.Bar(
            x=[product_amount],
            y=[product_name],
            orientation='h',
            name=product_name,  # 设置图例文字为商品名称
            marker=dict(
                color='rgba(74, 144, 226, {})'.format(0.6 + 0.4 * color_value),
            )
        ))

    fig.update_layout(
        title='热销产品TOP10',
        height=500,
        yaxis={'categoryorder': 'total ascending'},
        plot_bgcolor='white',
        title_x=0.5,
        title_font_size=16
    )

    return fig

# 订单详情表格
def create_orders_table(data, filters, records_count=50):
    if not data:
        return html.Div('数据加载中...')

    df_orders = apply_filters(data['orders'], filters) if filters else data['orders'].copy()
    
    # 按下单时间倒序排序
    df_orders = df_orders.sort_values('下单时间', ascending=False)

    display_columns = ['内部订单号', '店铺名称', '商品名称', '商品金额', '状态', '省份', '下单时间']
    if all(col in df_orders.columns for col in display_columns):
        display_data = df_orders[display_columns].copy()
        display_data['商品金额'] = display_data['商品金额'].apply(lambda x: f'¥{x:,.2f}')
        display_data['下单时间'] = display_data['下单时间'].dt.strftime('%Y-%m-%d %H:%M')

        # 如果是 'all' 就不截断
        if isinstance(records_count, str) and records_count == 'all':
            pass   # 不做 head，显示全部
        else:
            # 防御一下非 int 的情况
            try:
                records_count_int = int(records_count)
                display_data = display_data.head(records_count_int)
            except (TypeError, ValueError):
                # 如果出意外，退回默认 50
                display_data = display_data.head(50)

        # 下面你的表格代码不变
        table_rows = []
        for i in range(len(display_data)):
            bg_color = '#FFFFFF' if i % 2 == 0 else '#F5F7FA'
            row = html.Tr([
                html.Td(
                    display_data.iloc[i][col],
                    style={
                        'padding': '8px',
                        'border': '1px solid #ddd',
                        'textAlign': 'center',
                    }
                ) for col in display_columns
            ], style={'backgroundColor': bg_color})
            table_rows.append(row)

        return html.Div(
            html.Table([
                html.Thead([
                    html.Tr([html.Th(
                        col,
                        style={
                            'backgroundColor': COLOR_THEME['primary'],
                            'color': 'white',
                            'padding': '10px',
                            'border': '1px solid #ddd',
                            'textAlign': 'center',
                            'fontWeight': 'bold',
                            'fontSize': '0.9rem',
                            'whiteSpace': 'nowrap'
                        }
                    ) for col in display_columns])
                ]),
                html.Tbody(table_rows)
            ],
            style={
                'width': '100%',
                'borderCollapse': 'collapse',
                'tableLayout': 'fixed'
            }),
            style={
                'maxHeight': '500px',
                'overflowY': 'auto',
                'border': '1px solid #ddd',
                'borderRadius': '6px'
            }
        )
    return html.Div('数据格式错误')

# 更新主回调函数，增加记录数输入
@callback(
    [Output('category-filter', 'options'),
     Output('category-filter', 'value')],
    [Input('region-filter', 'value'),
     Input('time-filter', 'value')],
    [State('category-filter', 'value')]
)
def update_category_dropdown(selected_region, selected_time, current_category):
    data = load_data()
    if not data:
        # 数据加载失败时，至少保证下拉框可用
        return [{'label': '全部分类', 'value': 'all'}], 'all'

    df_orders = data['orders'].copy()
    
    # 应用区域和时间筛选
    if selected_region != 'all':
        df_orders = df_orders[df_orders['区域'] == selected_region]
    
    if selected_time != 'all':
        days = int(selected_time.replace('d', ''))
        cutoff_date = datetime.now() - timedelta(days=days)
        df_orders = df_orders[df_orders['下单时间'] >= cutoff_date]
    
    # 获取有效分类
    categories = df_orders['产品分类'].dropna().unique()
    options = [{'label': '全部分类', 'value': 'all'}]
    for cat in sorted(categories):
        options.append({'label': cat, 'value': cat})
    
    # 如果当前选中的分类在新的 options 里不存在，则重置为 all
    new_value = current_category
    if (current_category is None) or (current_category != 'all' and current_category not in categories):
        new_value = 'all'
    
    return options, new_value

# 主回调函数
@callback(
    [Output('kpi-cards', 'children'),
     Output('order-trend-chart', 'figure'),
     Output('region-distribution-chart', 'figure'),
     Output('category-performance-chart', 'figure'),
     Output('sales-funnel-chart', 'figure'),
     Output('product-analysis-chart', 'figure'),
     Output('orders-table', 'children')],
    [Input('region-filter', 'value'),
     Input('time-filter', 'value'),
     Input('category-filter', 'value'),
     Input('records-count-filter', 'value')]   # ✅新增
)
def update_dashboard(selected_region, selected_time, selected_category, records_count):
    data = load_data()
    if not data:
        empty_fig = go.Figure().update_layout(title='数据加载失败')
        return [
            html.Div('数据加载失败'),
            empty_fig, empty_fig, empty_fig, empty_fig, empty_fig,
            html.Div('数据加载失败')
        ]

    filters = {
        'region': selected_region,
        'time': selected_time,
        'category': selected_category
    }

    return [
        create_kpi_cards(data, filters),
        create_order_trend_chart(data, filters),
        create_region_distribution_chart(data, filters),
        create_category_performance_chart(data, filters),
        create_sales_funnel_chart(data, filters),
        create_product_analysis_chart(data, filters),
        create_orders_table(data, filters, records_count)
    ]

# 初始化应用
app.layout = create_layout()

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8050)
  
