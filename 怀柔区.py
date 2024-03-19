#2024.3.18 怀柔区
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.datasets import register_url

register_url("https://echarts-maps.github.io/echarts-china-counties-js/")

district = '怀柔区'  
geo = (
    Geo()
    .add_schema(maptype=district)
    .set_global_opts(title_opts=opts.TitleOpts(title=district))
)

geo.render('./output/怀柔区.html')
