#2024.3.18   作业二 2017海底捞门店数量
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Map
data ={
"广东省":37,
"山东省":20,
"河南省":27,
"四川省":6,                          
"河北省":11,
"湖南省":6,
"安徽省":9,
"湖北省":14,
"浙江省":20,
"广西壮族自治区":5,
"云南省":6,
"江西省":2,  
"辽宁省":6,
"福建省":15,
"陕西省":23,
"黑龙江省":2,
"山西省":2,
"贵州省":2,
"吉林省":2,
"甘肃省":2,
"上海市":22,
"台湾省":6,
"北京市":30,
"天津市":8,
"海南省":3,
"香港特别行政区":2,
"宁夏回族自治区":3,
"江苏省":45
}
map_data = list(data.items()) 

c = (
    Map()
    .add("2017年海底捞门店数量", 
         data_pair=map_data, 
         maptype="china",
         is_map_symbol_show=False, # 不描点             
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2017年海底捞门店数量分级设色图"),
        visualmap_opts=opts.VisualMapOpts(min_=0, max_=45, is_piecewise=True),
    )
)

c.render('./output/2017年海底捞门店数量.html')