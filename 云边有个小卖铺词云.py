
from pyecharts import options as opts
from pyecharts.charts import WordCloud
import jieba
import jieba.posseg as pseg

#########创建csv文档#############

txt_filename = './data/47.txt'
result_filename= './output/云边有个小买铺词频-pseg.csv'


#读文本
txt_file = open(txt_filename, 'r', encoding='utf-8')
content = txt_file.read()
txt_file.close()
print('文件读取完成')


#分词
words = pseg.cut(content) # peseg.cut返回生成器
print('分词完成')

# 用字典统计每个人物名词的出现次数
word_dict = {}
print('正在统计所有词中……')
count = 0 # 用于记录已处理的名词数
for one in words: 
    # 为便于处理，用w记录本次循环检查的“词”，f记录对应的“词性”
    w = one.word 
    f = one.flag 
    if len(w) == 1:  # 忽略单字
        continue
    if 'nr' in f: # 如果该词的词性中包含'nr'，即这是个人物名词，……
        if w in word_dict.keys(): # 如果该词已经在词典中，……
            word_dict[w] = word_dict[w] + 1
        else: # 如果该词不在词典中，……
            word_dict[w] = 1


 # 打印进度
count = count + 1
count_quo = int(count/1000)
count_mod = count % 1000 # 取模，即做除法得到的余数
if count_mod == 0: # 每逢整千的数，打印一次进度
    print('---已处理词数（千）：' + str(count_quo))  # 打印进度信息

# 循环结束点

print()
print('统计完成')

# 把字典转成列表，并按原先“键值对”中的“值”从大到小排序
items_list = list(word_dict.items())
items_list.sort(key=lambda x:x[1], reverse=True)
print('排序完成')

# 根据用户需求，打印排名前列的词，同时把统计结果存入文件
total_num = len(items_list)
print('共有' + str(total_num) + '个可能的高频词。')
num = input('您想查看前多少个高频词？[10]:')
if not num.isdigit() or num == '':
    num = 10
else:
    num = int(num)

if num > total_num:
    num = total_num

result_file = open(result_filename, 'w')   
result_file.write('高频词,出现次数\n')
for i in range(num):
    word, cnt = items_list[i]
    message = str(i+1) + '. ' + word + '\t' + str(cnt)
    print(message)
    result_file.write(word + ',' + str(cnt) + '\n')
result_file.close()

print('已写入文件：' + result_filename)



############词云##################
src_filename = './output/云边有个小买铺词频-pseg.csv'
src_file = open(src_filename, 'r')
line_list = src_file.readlines()  #返回列表，文件中的一行是一个元素
src_file.close()

wordfreq_list = []  #用于保存元组(人物姓名,出现次数)
for line in line_list:
    line = line.strip()  #删除'\n'
    line_split = line.split(',')
    wordfreq_list.append((line_split[0],line_split[1]))

del wordfreq_list[0] #删除csv文件中的标题行
print('人物数量：' + str(len(wordfreq_list)))
##-------从文件中读出人物词频完成------------------

##===============================================
##-------生成词云---------------------------------
cloud = WordCloud()

# 设置词云图
cloud.add('', 
          wordfreq_list[0:90], #元组列表，词和词频
          shape='circle',# 轮廓形状：'circle','cardioid','diamond',                                选择词云的形状
                           # 'triangle-forward','triangle','pentagon','star'
          mask_image='./data/词云背景图-蝴蝶.jpg', # 轮廓图，第一次显示可能有问题，刷新即可
          is_draw_out_of_bound=False, #允许词云超出画布边界
          word_size_range=[15, 50], #字体大小范围
          textstyle_opts=opts.TextStyleOpts(font_family="华文行楷"),
          #字体：例如，微软雅黑，宋体，华文行楷，Arial
          )

# 设置标题
cloud.set_global_opts(title_opts=opts.TitleOpts(title="云边有个小卖铺词云"))
out_filename = './output/云边有个小卖铺词云.html'
cloud.render(out_filename)
print('生成结果文件：' + out_filename)
