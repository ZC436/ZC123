#2024 3 18 世界地图
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.faker import Faker

c = (
    Geo()
    .add_schema(maptype="world")
    .render("./output/世界地图.html")
)