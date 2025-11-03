from faker import Faker
import pandas as pd
import random
from datetime import timedelta, date

fake = Faker('zh_CN')  # 使用中文环境

# 设置随机种子以确保可重现性
random.seed(42)

# 省份和城市映射
province_city_map = {
    "北京市": ["北京市"],
    "上海市": ["上海市"],
    "广东省": ["广州市", "深圳市", "珠海市", "汕头市", "佛山市", "韶关市", "湛江市", "肇庆市", "江门市", "茂名市", "惠州市", "梅州市", "汕尾市", "河源市", "阳江市", "清远市", "东莞市", "中山市", "潮州市", "揭阳市", "云浮市"],
    "江苏省": ["南京市", "无锡市", "徐州市", "常州市", "苏州市", "南通市", "连云港市", "淮安市", "盐城市", "扬州市", "镇江市", "泰州市", "宿迁市"],
    "浙江省": ["杭州市", "宁波市", "温州市", "嘉兴市", "湖州市", "绍兴市", "金华市", "衢州市", "舟山市", "台州市", "丽水市"],
    "山东省": ["济南市", "青岛市", "淄博市", "枣庄市", "东营市", "烟台市", "潍坊市", "济宁市", "泰安市", "威海市", "日照市", "临沂市", "德州市", "聊城市", "滨州市", "菏泽市"],
    "河南省": ["郑州市", "开封市", "洛阳市", "平顶山市", "安阳市", "鹤壁市", "新乡市", "焦作市", "濮阳市", "许昌市", "漯河市", "三门峡市", "南阳市", "商丘市", "信阳市", "周口市", "驻马店市", "济源市"],
    "河北省": ["石家庄市", "唐山市", "秦皇岛市", "邯郸市", "邢台市", "保定市", "张家口市", "承德市", "沧州市", "廊坊市", "衡水市"],
    "四川省": ["成都市", "自贡市", "攀枝花市", "泸州市", "德阳市", "绵阳市", "广元市", "遂宁市", "内江市", "乐山市", "南充市", "眉山市", "宜宾市", "广安市", "达州市", "雅安市", "巴中市", "资阳市", "阿坝藏族羌族自治州", "甘孜藏族自治州", "凉山彝族自治州"],
    "辽宁省": ["沈阳市", "大连市", "鞍山市", "抚顺市", "本溪市", "丹东市", "锦州市", "营口市", "阜新市", "辽阳市", "盘锦市", "铁岭市", "朝阳市", "葫芦岛市"],
    "湖北省": ["武汉市", "黄石市", "十堰市", "宜昌市", "襄阳市", "鄂州市", "荆门市", "孝感市", "荆州市", "黄冈市", "咸宁市", "随州市", "恩施土家族苗族自治州", "仙桃市", "潜江市", "天门市", "神农架林区"],
    "湖南省": ["长沙市", "株洲市", "湘潭市", "衡阳市", "邵阳市", "岳阳市", "常德市", "张家界市", "益阳市", "郴州市", "永州市", "怀化市", "娄底市", "湘西土家族苗族自治州"],
    "安徽省": ["合肥市", "芜湖市", "蚌埠市", "淮南市", "马鞍山市", "淮北市", "铜陵市", "安庆市", "黄山市", "滁州市", "阜阳市", "宿州市", "六安市", "亳州市", "池州市", "宣城市"],
    "陕西省": ["西安市", "铜川市", "宝鸡市", "咸阳市", "渭南市", "延安市", "汉中市", "榆林市", "安康市", "商洛市"],
    "福建省": ["福州市", "厦门市", "莆田市", "三明市", "泉州市", "漳州市", "南平市", "龙岩市", "宁德市"],
    "天津市": ["天津市"],
    "山西省": ["太原市", "大同市", "阳泉市", "长治市", "晋城市", "朔州市", "晋中市", "运城市", "忻州市", "临汾市", "吕梁市"],
    "江西省": ["南昌市", "景德镇市", "萍乡市", "九江市", "新余市", "鹰潭市", "赣州市", "吉安市", "宜春市", "抚州市", "上饶市"],
    "云南省": ["昆明市", "曲靖市", "玉溪市", "保山市", "昭通市", "丽江市", "普洱市", "临沧市", "楚雄彝族自治州", "红河哈尼族彝族自治州", "文山壮族苗族自治州", "西双版纳傣族自治州", "大理白族自治州", "德宏傣族景颇族自治州", "怒江傈僳族自治州", "迪庆藏族自治州"],
    "广西壮族自治区": ["南宁市", "柳州市", "桂林市", "梧州市", "北海市", "防城港市", "钦州市", "贵港市", "玉林市", "百色市", "贺州市", "河池市", "来宾市", "崇左市"],
    "黑龙江省": ["哈尔滨市", "齐齐哈尔市", "鸡西市", "鹤岗市", "双鸭山市", "大庆市", "伊春市", "佳木斯市", "七台河市", "牡丹江市", "黑河市", "绥化市", "大兴安岭地区"],
    "海南省": ["海口市", "三亚市", "三沙市", "儋州市", "五指山市", "琼海市", "文昌市", "万宁市", "东方市", "定安县", "屯昌县", "澄迈县", "临高县", "白沙黎族自治县", "昌江黎族自治县", "乐东黎族自治县", "陵水黎族自治县", "保亭黎族苗族自治县", "琼中黎族苗族自治县"],
    "内蒙古自治区": ["呼和浩特市", "包头市", "乌海市", "赤峰市", "通辽市", "鄂尔多斯市", "呼伦贝尔市", "巴彦淖尔市", "乌兰察布市", "兴安盟", "锡林郭勒盟", "阿拉善盟"],
    "宁夏回族自治区": ["银川市", "石嘴山市", "吴忠市", "固原市", "中卫市"],
    "新疆维吾尔自治区": ["乌鲁木齐市", "克拉玛依市", "吐鲁番市", "哈密市", "昌吉回族自治州", "博尔塔拉蒙古自治州", "巴音郭楞蒙古自治州", "阿克苏地区", "克孜勒苏柯尔克孜自治州", "喀什地区", "和田地区", "伊犁哈萨克自治州", "塔城地区", "阿勒泰地区", "石河子市", "阿拉尔市", "图木舒克市", "五家渠市", "北屯市", "铁门关市", "双河市", "可克达拉市", "昆玉市", "胡杨河市", "新星市", "白杨市"],
    "西藏自治区": ["拉萨市", "日喀则市", "昌都市", "林芝市", "山南市", "那曲市", "阿里地区"],
    "青海省": ["西宁市", "海东市", "海北藏族自治州", "黄南藏族自治州", "海南藏族自治州", "果洛藏族自治州", "玉树藏族自治州", "海西蒙古族藏族自治州"],
    "甘肃省": ["兰州市", "嘉峪关市", "金昌市", "白银市", "天水市", "武威市", "张掖市", "平凉市", "酒泉市", "庆阳市", "定西市", "陇南市", "临夏回族自治州", "甘南藏族自治州"],
    "贵州省": ["贵阳市", "六盘水市", "遵义市", "安顺市", "毕节市", "铜仁市", "黔西南布依族苗族自治州", "黔东南苗族侗族自治州", "黔南布依族苗族自治州"],
    "吉林省": ["长春市", "吉林市", "四平市", "辽源市", "通化市", "白山市", "松原市", "白州市", "延边朝鲜族自治州"],
    "重庆市": ["重庆市"]
}

# 生成知名服装品牌店铺名称
fashion_brands = [
    "阿迪达斯官方旗舰店", "耐克官方旗舰店", "优衣库官方旗舰店", "ZARA官方旗舰店", "H&M官方旗舰店",
    "GAP官方旗舰店", "COS官方旗舰店", "Massimo Dutti官方旗舰店", "Mango官方旗舰店", "Pull&Bear官方旗舰店",
    "Bershka官方旗舰店", "Stradivarius官方旗舰店", "ONLY官方旗舰店", "VERO MODA官方旗舰店", "太平鸟官方旗舰店",
    "江南布衣官方旗舰店", "播官方旗舰店", "秋水伊人官方旗舰店", "欧时力官方旗舰店", "韩都衣舍官方旗舰店",
    "森马官方旗舰店", "美特斯邦威官方旗舰店", "GXG官方旗舰店", "杰克琼斯官方旗舰店", "太平鸟女装官方旗舰店",
    "太平鸟男装官方旗舰店", "太平鸟童装官方旗舰店", "江南布衣女装官方旗舰店", "江南布衣男装官方旗舰店", "播女装官方旗舰店",
    "播男装官方旗舰店", "秋水伊人女装官方旗舰店", "欧时力女装官方旗舰店", "韩都衣舍女装官方旗舰店", "森马女装官方旗舰店",
    "森马男装官方旗舰店", "美特斯邦威男装官方旗舰店", "GXG男装官方旗舰店", "杰克琼斯男装官方旗舰店", "优衣库女装官方旗舰店",
    "优衣库男装官方旗舰店", "优衣库童装官方旗舰店", "ZARA女装官方旗舰店", "ZARA男装官方旗舰店", "ZARA童装官方旗舰店",
    "H&M女装官方旗舰店", "H&M男装官方旗舰店", "H&M童装官方旗舰店", "GAP女装官方旗舰店", "GAP男装官方旗舰店",
    "GAP童装官方旗舰店", "COS女装官方旗舰店", "Massimo Dutti女装官方旗舰店", "Massimo Dutti男装官方旗舰店", "Mango女装官方旗舰店",
    "Pull&Bear男装官方旗舰店", "Bershka女装官方旗舰店", "Stradivarius女装官方旗舰店", "ONLY女装官方旗舰店", "VERO MODA女装官方旗舰店"
]

# —— 大类->中类
TAXONOMY = {
    "女装": ["连衣裙", "半身裙", "上装", "下装", "外套", "卫衣", "T恤", "毛衣"],
    "男装": ["上装", "下装", "外套", "衬衫", "T恤", "卫衣"],
    "童装": ["上装", "下装", "外套", "套装"],
    "内衣": ["家居服"],
    "运动": ["运动外套", "运动裤", "运动T恤", "卫衣"]
}

# —— 中类->可用"款式名称"关键词池
STYLE_POOL = {
    "连衣裙": ["针织连衣裙", "收腰连衣裙", "衬衫连衣裙", "A字连衣裙"],
    "半身裙": ["伞裙", "包臀裙", "百褶裙"],
    "上装": ["休闲衬衫", "针织衫", "POLO衫"],
    "下装": ["牛仔裤", "短裤", "休闲裤"],
    "外套": ["风衣", "西装外套", "羽绒服"],
    "卫衣": ["连帽卫衣", "套头卫衣"],
    "T恤": ["短袖T恤", "长袖T恤"],
    "毛衣": ["羊毛衫", "开衫"],
    "衬衫": ["休闲衬衫", "条纹衬衫"],
    "套装": ["运动套装", "童装套装"],
    "运动外套": ["训练外套", "跑步外套"],
    "运动裤": ["运动长裤", "速干短裤"],
    "运动T恤": ["速干T恤", "运动T恤"],
    "家居服": ["家居服"]
}

# 名称后缀池
SUFFIX_POOL = ["春季款", "夏季款", "秋冬款", "经典款", "新款", "热卖款"]

def pick_taxonomy():
    big = random.choice(list(TAXONOMY.keys()))
    middle = random.choice(TAXONOMY[big])
    return big, middle

def build_style_name(middle):
    base = random.choice(STYLE_POOL[middle])
    return base + random.choice(SUFFIX_POOL)

# ------------------------------
# 1️⃣ 生成用户表 user_unique_compare
# ------------------------------
users = []
for i in range(1000):
    user_id = f"a{random.choice(['b', 'c', 'd', 'e', 'f'])}{random.randint(1000000000000000, 9999999999999999):016d}"
    users.append({
        "自增ID": i + 1,
        "全渠道用户ID": user_id,
        "用户昵称": fake.name()
    })
df_users = pd.DataFrame(users)
df_users.to_csv("user_unique_compare.csv", index=False, encoding="utf-8-sig")
print(f"Generated {len(df_users)} users")

# ------------------------------
# 2️⃣ 生成 SPU 表 spu_manages_feishu
# ------------------------------
spus = []
for i in range(200):
    spu_id = f"SPU{i:03d}"
    big, middle = pick_taxonomy()  # 大类+中类
    style_name = build_style_name(middle)

    sales_quantity = random.randint(0, 5000)
    return_quantity = random.randint(0, int(sales_quantity * 0.15))
    actual_return_quantity = random.randint(0, return_quantity)
    shipped_sales = random.randint(0, sales_quantity)
    shipped_amount = round(random.uniform(1000, 50000), 2)
    sales_amount = round(random.uniform(1000, 50000), 2)
    sales_cost = round(sales_amount * random.uniform(0.3, 0.7), 2)
    actual_return_amount = round(sales_amount * random.uniform(0.01, 0.15), 2)
    actual_return_cost = round(sales_cost * random.uniform(0.01, 0.15), 2)

    spus.append({
        "自增ID": i + 1,
        "款号": spu_id,
        "款式名称商品名称": style_name,                 # 与中类绑定
        "商品标签": random.choice(["新品", "热卖", "清仓", "爆款", "限量", "联名", "设计师款"]),
        "产品分类": big,                                # 大类
        "中类": middle,                                 # 二级类
        "退货率": round(return_quantity / max(sales_quantity, 1), 4),
        "销售数量": sales_quantity,
        "净销量": sales_quantity - return_quantity,
        "实发数量": shipped_sales,
        "实发金额": shipped_amount,
        "销售金额": sales_amount,
        "销售成本": sales_cost,
        "实发成本": round(shipped_amount * random.uniform(0.3, 0.7), 2),
        "销售毛利": round(sales_amount - sales_cost, 2),
        "退货数量": return_quantity,
        "实退数量": actual_return_quantity,
        "退货金额": round(sales_amount * random.uniform(0.01, 0.15), 2),
        "退货成本": round(sales_cost * random.uniform(0.01, 0.15), 2),
        "实退成本": actual_return_cost,
        "实退金额": actual_return_amount,
        "退货毛利": round((sales_amount - sales_cost) * random.uniform(0.01, 0.15), 3),
        "净销售额": round(sales_amount - actual_return_amount, 2),
        "净销售成本": round(sales_cost - actual_return_cost, 2),
        "净销售毛利": round((sales_amount - sales_cost) - (actual_return_amount - actual_return_cost), 2),
        "优惠金额": round(sales_amount * random.uniform(0.01, 0.1), 2),
        "运费收入": round(random.uniform(0, 50), 2),
        "运费支出": round(random.uniform(0, 30), 2),
        "基本金额": round(sales_amount * random.uniform(0.8, 1.2), 2),
        "已付金额": round(sales_amount * random.uniform(0.8, 1.0), 2),
        "实发退货率": round(actual_return_quantity / max(shipped_sales, 1), 4),
        "基本售价": round(random.uniform(50, 500), 2),
        "五类": random.choice(["A类", "B类", "C类", "D类", "E类", "未分组"]),
        "延续内容": random.choice(["延续款", "升级款", "改进款", "经典款", "无"]),
        "延续月份": random.choice(["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月","无"]),
        "年份": random.choice([2023, 2024, 2025]),
        "季节": random.choice(["春夏", "秋冬", "春季", "夏季", "秋季", "冬季"]),
        "商品状态": random.choice(["在售", "停售", "预售", "清仓", "下架"]),
        "折扣": round(random.uniform(0.5, 1.0), 2),
        "现货": random.randint(0, 1000),
        "货量": random.randint(0, 2000),
        "主仓": random.randint(0, 1500),
        "SKC库存": random.randint(0, 500),
        "净销售金额": round(sales_amount - actual_return_amount, 2),
        "设计师(人员)": fake.name(),
        "元素类型": random.choice(["简约", "复古", "时尚", "休闲", "商务", "运动"]),
        "上新波次": random.choice(["第一波", "第二波", "第三波", "第四波", "特别款"]),
        "销售顶峰": random.choice(["3月", "6月", "9月", "12月", "全年平销"]),
        "可售周期": random.choice(["3个月", "6个月", "1年", "长期"]),
        "小波段": random.choice(["A波", "B波", "C波", "D波", "E波"]),
        "超级直播": random.choice(["否", "是"]),
        "延续方向": random.choice(["延续", "改进", "创新", "停用"]),
        "延续结果": random.choice(["成功", "一般", "失败", "待评估"]),
        "复盘结论": random.choice(["好", "一般", "需改进", "优秀"]),
        "开售评级": random.choice(["A", "B", "C", "D", "E"])
    })
df_spus = pd.DataFrame(spus)
df_spus.to_csv("spu_manages_feishu.csv", index=False, encoding="utf-8-sig")
print(f"Generated {len(df_spus)} SPUs")

# ------------------------------
# 3️⃣ 生成 SKU 表 sku_data_base
# ------------------------------
colors = ["红色", "黑色", "白色", "蓝色", "灰色", "粉色", "米色", "绿色", "紫色", "黄色", "橙色", "棕色"]
sizes = ["XS", "S", "M", "L", "XL", "XXL", "XXXL", "均码"]
specifications = ["修身", "宽松", "标准", "加长", "短款"]
categories = ["女装", "男装", "鞋靴", "配饰", "内衣", "运动", "童装"]

skus = []
sku_id_counter = 1
for spu in spus:
    num_skus = random.randint(3, 5)
    base_color = random.choice(colors)
    for _ in range(num_skus):
        size = random.choice(sizes)
        specification = random.choice(specifications)
        base_sku = f"{spu['款号']}-{base_color[:2]}-{size}"
        color_spec = f"{base_color} {specification}"

        skus.append({
            "自增ID": sku_id_counter,
            "款式编码": spu["款号"],                       # 继承
            "商品编码": base_sku,
            "商品名称": spu["款式名称商品名称"],             # 继承
            "颜色及规格": color_spec,
            "颜色": base_color,
            "规格": specification,
            "基本售价": round(random.uniform(50, 500), 0),
            "市场吊牌价": round(random.uniform(100, 800), 0),
            "分类": spu["产品分类"],                       # 继承
            "商品属性": size,
            "创建时间": fake.date_time_between(start_date='-2y', end_date='now'),
            "季节": spu["季节"],                           # 继承
            "面料成份": random.choice(["棉", "涤纶", "丝", "麻", "羊毛", "混纺"])
        })
        sku_id_counter += 1

df_skus = pd.DataFrame(skus)
df_skus.to_csv("sku_data_base.csv", index=False, encoding="utf-8-sig")
print(f"Generated {len(df_skus)} SKUs")

# ------------------------------
# 4️⃣ 生成 SKU 销售统计表 new_sku_sales
# ------------------------------
sku_sales = []
for i, sku_item in enumerate(df_skus.to_dict('records')):
    # 生成一个"记录日期"(晚于统计日期)
    record_date = fake.date_time_between(start_date='-30d', end_date='now')
    # 再生成一个不晚于记录日期的"统计日期"
    # 计算从记录日期往前推30天的日期
    thirty_days_before_record = record_date.date() - timedelta(days=30)
    stat_date = fake.date_between(start_date=thirty_days_before_record, end_date=record_date.date())
    
    # "上线前三天"不晚于统计日期
    # 计算从统计日期往前推10天的日期，但不能早于当前日期往前推20天
    ten_days_before_stat = stat_date - timedelta(days=10)
    twenty_days_ago = date.today() - timedelta(days=20)
    # 确保上线前三天的日期不早于20天前，也不晚于统计日期
    online_minus3_start = max(ten_days_before_stat, twenty_days_ago)
    
    # 如果计算出的起始日期晚于结束日期(stat_date)，则强制将起始日期设为结束日期
    if online_minus3_start > stat_date:
        online_minus3 = stat_date
    else:
        online_minus3 = fake.date_between(start_date=online_minus3_start, end_date=stat_date)

    order_count = random.randint(0, 500)
    payment_count = random.randint(0, order_count)

    sku_sales.append({
        "自增ID": i + 1,
        "统计日期": stat_date.strftime('%Y-%m-%d'),
        "店铺名称": random.choice(fashion_brands),
        "商品ID": random.randint(100000, 999999),
        "商品名称": sku_item["商品名称"],
        "SKU ID": random.randint(100000, 999999),
        "SKU名称": sku_item["商品编码"],
        "加购件数": random.randint(0, order_count * 3),
        "下单件数": order_count,
        "下单买家数": random.randint(0, order_count),
        "下单金额": random.randint(0, 50000),
        "支付件数": payment_count,
        "支付买家数": random.randint(0, payment_count),
        "支付金额": random.randint(0, 40000),
        "款号": sku_item["款式编码"],
        "颜色": sku_item["颜色"],
        "分款号": f"SUB{random.randint(100, 999)}",
        "波段": random.choice(["A波", "B波", "C波", "D波"]),
        "链接": f"https://shop.example.com/product/{random.randint(10000, 99999)}",
        "上线前三天": online_minus3.strftime('%Y-%m-%d'),
        "记录日期": record_date,
        "商品编码": sku_item["商品编码"]
    })

df_sales = pd.DataFrame(sku_sales)
for r in sku_sales:
    if r["店铺名称"] not in fashion_brands:
        r["店铺名称"] = random.choice(fashion_brands)
df_sales = pd.DataFrame(sku_sales)
df_sales.to_csv("new_sku_sales.csv", index=False, encoding="utf-8-sig")
print(f"Generated {len(df_sales)} SKU sales records")


# ------------------------------
# 5️⃣ 生成订单表 erp_order
# ------------------------------

# 为每个用户预先分配固定省市
user_locations = {}
for user in users:
    province = random.choice(list(province_city_map.keys()))
    city = random.choice(province_city_map[province])
    user_locations[user["全渠道用户ID"]] = {"省份": province, "城市": city}

# 各订单状态允许的退款状态集合
ALLOWED_REFUNDS_BY_STATUS = {
    "待付款":   ["未申请退款"],
    "已取消":   ["未申请退款"],
    "已付款":   ["未申请退款", "申请退款", "退款中", "退款关闭"],
    "已发货":   ["未申请退款", "申请退款", "退款中", "退款关闭"],
    "已完成":   ["未申请退款", "成功退款", "退款关闭"]
}

orders = []
for i in range(5000):
    user = random.choice(users)
    sku_item = random.choice(skus)
    quantity = random.randint(1, 3)
    unit_price = float(sku_item["基本售价"])
    product_amount = round(unit_price * quantity, 2)

    # 金额：应付=商品金额(恒>0)，已付取决于状态
    payable_amount = max(product_amount, 0.01)

    # 下单时间不早于SKU创建时间
    order_time = fake.date_time_between(start_date='-180d', end_date='now')
    if sku_item["创建时间"] > order_time:
        order_time = sku_item["创建时间"] + timedelta(minutes=random.randint(5, 300))
    candidate_payment_date = order_time + timedelta(days=random.randint(0, 2))
    candidate_shipping_date = candidate_payment_date + timedelta(days=random.randint(1, 3))

    # 先抽主状态
    status = random.choices(
        ["待付款", "已付款", "已发货", "已完成", "已取消"],
        weights=[0.5, 2, 2.5, 5, 0.5],
        k=1
    )[0]

    # 根据主状态限制退款状态
    refund_status = random.choice(ALLOWED_REFUNDS_BY_STATUS[status])

    # 如果抽到成功退款但状态不为已完成，则抬升为已完成
    if refund_status == "成功退款" and status != "已完成":
        status = "已完成"

    # 金额与时间随状态赋值（并保证时间顺序）
    if status == "待付款":
        paid_amount = 0.00
        payment_date = None
        shipping_date = None
    elif status == "已取消":
        paid_amount = 0.00
        payment_date = None
        shipping_date = None
        refund_status = "未申请退款"
    elif status == "已付款":
        paid_amount = product_amount if random.random() > 0.05 else round(product_amount * random.uniform(0.8, 0.95), 2)
        payment_date = candidate_payment_date
        shipping_date = None
    elif status == "已发货":
        paid_amount = product_amount if random.random() > 0.05 else round(product_amount * random.uniform(0.8, 0.95), 2)
        payment_date = candidate_payment_date
        shipping_date = candidate_shipping_date
    else:  # 已完成
        paid_amount = product_amount if random.random() > 0.05 else round(product_amount * random.uniform(0.8, 0.95), 2)
        payment_date = candidate_payment_date
        shipping_date = candidate_shipping_date

    # 退款登记/实退数量与状态匹配
    if refund_status in ("未申请退款", "退款关闭"):
        registered_quantity = 0
        actual_refund_quantity = 0
    elif refund_status == "申请退款":
        registered_quantity = quantity
        actual_refund_quantity = 0
    elif refund_status == "退款中":
        registered_quantity = quantity
        actual_refund_quantity = random.choice([0] * 4 + [random.randint(1, quantity)])
    else:  # 成功退款
        registered_quantity = quantity
        actual_refund_quantity = random.randint(1, quantity)

    # 额外一致性约束：
    # - 付款/发货时间顺序
    if payment_date is not None:
        payment_date = max(payment_date, order_time)
    # - 待付款/已取消时，已付金额必须为0，退款登记/实退为0
    if shipping_date is not None and payment_date is not None:
        shipping_date = max(shipping_date, payment_date + timedelta(minutes=1))

    loc = user_locations[user["全渠道用户ID"]]

    orders.append({
        "自增ID": i + 1,
        "内部订单号": f"INT{20250000000 + i}",
        "线上订单号": f"ON{20250000000 + i}",
        "店铺名称": random.choice(fashion_brands),
        "全渠道用户ID": user["全渠道用户ID"],
        "发货日期": shipping_date,
        "付款日期": payment_date,
        "应付金额": round(payable_amount, 2),
        "已付金额": round(float(paid_amount), 2),
        "状态": status,
        "收货人": user["用户昵称"],
        "款号": sku_item["款式编码"],
        "商品编码": sku_item["商品编码"],
        "商品名称": sku_item["商品名称"],
        "颜色及规格": f"{sku_item['颜色']} {sku_item['规格']}",
        "下单时间": order_time,
        "省份": loc["省份"],
        "城市": loc["城市"],
        "平台站点": random.choice(["淘宝", "天猫", "京东", "抖音", "拼多多", "微信"]),
        "子订单编号": f"SUB{20250000000 + i}",
        "线上子订单编号": f"ONSUB{20250000000 + i}",
        "原始线上订单号": f"ORIG{20250000000 + i}",
        "数量": quantity,
        "商品单价": unit_price,
        "商品金额": product_amount,
        "原价": round(unit_price * random.uniform(1.1, 1.5), 2),
        "是否赠品": random.choice(["是", "否"]),
        "子订单状态": status,             # 跟主状态保持一致
        "退款状态": refund_status,
        "登记数量": registered_quantity,
        "实退数量": actual_refund_quantity
    })

df_orders = pd.DataFrame(orders)
df_orders.to_csv("erp_order.csv", index=False, encoding="utf-8-sig")
print(f"Generated {len(df_orders)} orders")


# ------------------------------
# 6️⃣ 强一致性校验断言（生成后快速自检）
# ------------------------------
# 基础金额约束
assert (df_orders["应付金额"] > 0).all()

# 状态-退款状态映射
status_to_refunds = df_orders.groupby("状态")["退款状态"].unique().to_dict()
# 逐行校验（避免极端意外）
for _, row in df_orders.iterrows():
    assert row["退款状态"] in ALLOWED_REFUNDS_BY_STATUS[row["状态"]]

# 待付款/已取消：已付=0，付款/发货时间为空，退款量=0
mask_np = df_orders["状态"].isin(["待付款", "已取消"])
assert (df_orders.loc[mask_np, "已付金额"] == 0).all()
assert df_orders.loc[mask_np, "付款日期"].isna().all()
assert df_orders.loc[mask_np, "发货日期"].isna().all()
assert (df_orders.loc[mask_np, ["登记数量", "实退数量"]].sum(axis=1) == 0).all()

# 已付款：有付款时间，无发货时间（按生成逻辑）；允许退款中/申请退款/关闭，但不允许成功退款
mask_paid = df_orders["状态"] == "已付款"
if mask_paid.any():
    assert df_orders.loc[mask_paid, "付款日期"].notna().all()
    assert df_orders.loc[mask_paid, "发货日期"].isna().all()
    assert (~df_orders.loc[mask_paid, "退款状态"].isin(["成功退款"])).all()

# 已发货/已完成：必须有付款时间；已发货/已完成有发货时间
mask_shipped = df_orders["状态"] == "已发货"
mask_done = df_orders["状态"] == "已完成"
if mask_shipped.any():
    assert df_orders.loc[mask_shipped, "付款日期"].notna().all()
    assert df_orders.loc[mask_shipped, "发货日期"].notna().all()
if mask_done.any():
    assert df_orders.loc[mask_done, "付款日期"].notna().all()
    assert df_orders.loc[mask_done, "发货日期"].notna().all()
    # 已完成可出现成功退款；若出现，实退数量>0
    mask_done_sr = mask_done & (df_orders["退款状态"] == "成功退款")
    if mask_done_sr.any():
        assert (df_orders.loc[mask_done_sr, "实退数量"] > 0).all()

# 时间顺序：付款 ≥ 下单，发货 ≥ 付款
if df_orders["付款日期"].notna().any():
    assert (df_orders.loc[df_orders["付款日期"].notna(), "付款日期"]
            >= df_orders.loc[df_orders["付款日期"].notna(), "下单时间"]).all()
if df_orders["发货日期"].notna().any():
    assert (df_orders.loc[df_orders["发货日期"].notna(), "发货日期"]
            >= df_orders.loc[df_orders["发货日期"].notna(), "付款日期"]).all()

print("\nData generation completed!")
print(f"Files generated:")
print(f"- user_unique_compare.csv: {len(df_users)} records")
print(f"- spu_manages_feishu.csv: {len(df_spus)} records") 
print(f"- sku_data_base.csv: {len(df_skus)} records")
print(f"- new_sku_sales.csv: {len(df_sales)} records")
print(f"- erp_order.csv: {len(df_orders)} records")