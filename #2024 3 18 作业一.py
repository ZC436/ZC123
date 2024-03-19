#2024 3 18 中国地图


from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.faker import Faker

c = (
    Geo()
    .add_schema(maptype="china")
    .render("./output/中国地图.html")
)
