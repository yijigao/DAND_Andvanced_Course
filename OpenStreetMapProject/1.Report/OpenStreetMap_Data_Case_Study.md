# 1. 数据来源
成都市, 四川省, 中华人民共和国 
* https://www.openstreetmap.org/relation/2110264 
* https://mapzen.com/data/metro-extracts/your-extracts/23b263c2550d 
这是我目前所在的城市，我希望通过此次分析对这个城市有更深刻的了解：）
# 2. 地图中发现的问题
当我从地图数据中取出一个小样本进行小测试时，发现地图数据有如下问题：
1. 邮编数据有问题，部分邮编显示为028，这是成都的区号，不是邮编
2. 部分街道名称过于简化，如St, Rd; 中英文名称混用，如“人民南路四段 - Renminnanlu 4 Duan”；还有些英文名称混用了中文拼音。
3. 不一致的城市名，该地图数据的addr:city数据应该都是成都，然而出现了“{'k': 'addr:city', 'v': '双流县华阳镇'}”镇的名称的情况
4. 门牌号显示不规范，如有的显示“16”而有的显示“16号”
## 2.1 处理邮编数据
使用audit_postcodes.py进行处理，将以028开头的邮编转成成都邮编610000
```commandline
def audit_postcode(postcode):
    # 如果邮编是‘028’，将其转为成都市邮编‘610000'
    
    if postcode.startswith('028'):
        return '610000'
    else:
        return postcode
```
## 2.2 处理街道问题
使用audit_street_name.py进行处理
* 对于St,Rd等过于简化街道名，将对应名称补全称，即“St => Street; Rd => Street”
* 对于中英混用的街道名，只保留中文名称，如“人民南路四段 - Renminnanlu 4 Duan => 人民南路四段”
* 对于英文名称混用中文拼英的，将其转为英文名称，如“jie”=> "Street"

audit_street_name.py
```commandline
street_type_re = re.compile(r'[路段街号道巷]$', re.IGNORECASE) # 匹配最后一个汉字为“路段街号道巷”之一的街道名
street_type_en_re = re.compile(r'\b\S+\.?$', re.IGNORECASE) # 匹配英文街道名空格后面的单词


expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",
            "Trail", "Parkway", "Commons", "段", "街","路","号","巷","道","West","East","North","South"]


mapping = {"St":"Street",
           "St.":"Street",
           "st.":"Street",
           " st":" Street",
           "Rd":"Road",
           "Rd.":"Road",
           "Ave":"Avenue",
           "Ave.":"Avenue",
           "jie": "Street",
           "Jie": "Street"
            }


def audit_street_type(street_types, street_name):
    # 分别对英文和中文街道名进行处理
    m = street_type_re.search(street_name)
    n = street_type_en_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)
    else:
        if n:
            street_type = n.group()
            if street_type not in expected:
                street_types[street_type].add(street_name)


def update_name(name, mapping):
    for key in mapping:
        # 对于有中英文混杂的名字，用“，”或“-”隔开，我们取中文名称
        if "," in name:
            name = name.split(",")[0]
            if name.endswith(key):
                return name.replace(key, mapping[key])
        if "-" in name:
            return name.split(" - ")[0]
        elif name.endswith(key):
            return name.replace(key, mapping[key])
```
## 2.3 处理城市名称
使用audit_city.py 处理
将所有异常显示的城市名字改为成都
```commandline
def audit_city(city_name):
    # 如果city_name不是是‘成都市’，将其转为‘成都市’
    if city_name != "成都市":
        return '成都市'
    else:
        return city_name
```
## 2.4 处理门牌号
使用audit_housenumber.py处理
统一显示“xx号”
```commandline
def audit_housenumber(house_number):
    """
    如果是数字的话，那就在后面加上“号”
    """
    try:
        if int(house_number):
            return house_number + "号"
    except ValueError:
        return house_number
```
# 3.数据概述
这部分包含了地图数据的基本概要
## 3.1 清理数据并导入数据库
代码详见data_clean.py
## 3.2 数据大小
```commandline
Chengdu.osm ......... 129 MB
charlotte.db .......... 69.9 MB
nodes.csv ............. 53.5 MB
nodes_tags.csv ........ 0.97 MB
ways.csv .............. 3.28 MB
ways_tags.csv ......... 3.96 MB
ways_nodes.cv ......... 17.6 MB
```
## 3.3 节点数量
```commandline
SELECT COUNT(*) FROM nodes;
```
673425
## 3.4 途径数量
```commandline
SELECT COUNT(*) FROM ways;
``` 
56855
## 3.5 唯一用户的数量
```commandline
SELECT COUNT(DISTINCT(e.uid))
FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways) e;
```
651
## 3.6 前10名贡献者
```commandline
SELECT e.user, COUNT(*) as num
FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e
GROUP BY e.user
ORDER BY num DESC
LIMIT 10;
```
output:
```commandline
                0       1
0          ff5722  140129
1       katpatuka  106103
2            巴山夜雨   61942
3     AntiEntropy   31173
4         hanchao   28023
5          Nautic   27621
6  geodreieck4711   23458
7         jamesks   19831
8        7thgrade   15423
9      guanchzhou   13383
```
## 3.7 仅参与一次发布数据的唯一用户数量
```commandline
SELECT COUNT(*)
FROM
(SELECT e.user, COUNT(*) as num
FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e
GROUP BY e.user
HAVING num=1) u;
```
126
# 4.关于数据集的其他想法
## 4.1 贡献者统计和游戏化建议
### 4.1.1 贡献者统计结果
前2名贡献者贡献了大多数数据，而有近20%用户仅参与一次贡献，由此可以推测用户参与积极性不够高
### 4.1.2 改进或分析数据建议
+ 为了提高贡献者积极提供数据，可以采取奖励措施
  - 好处：用户贡献积极性提高，数据更新更充分且及时。
  - 预期的问题： 数据获取成本提高，并且用户可能并不买单
  
+ 对于数据质量，可以为用户提供模板，并且设置一套对于数据分析有利的数据格式规范
   - 好处：数据更干净，节省清理时间；数据更准确可信
   - 预期的问题：用户需要遵守格式规范，这可能带来一定的学习难度，可能降低用户的贡献积极性

## 4.2 其他的探索
### 4.2.1 公共设施数量前10
```commandline
SELECT value, COUNT(*) as num
FROM nodes_tags
WHERE key='amenity'
GROUP BY value
ORDER BY num DESC
LIMIT 10;
```
output:
```commandline
                  0    1
0        restaurant  181
1           toilets   81
2              fuel   73
3           parking   70
4              cafe   64
5              bank   63
6            school   60
7          hospital   46
8   bicycle_parking   30
9  place_of_worship   28
```
### 4.2.2 最大的宗教
```commandline
SELECT nodes_tags.value, COUNT(*) as num
FROM nodes_tags
JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE
value='place_of_worship') i
ON nodes_tags.id=i.id
WHERE nodes_tags.key='religion'
GROUP BY nodes_tags.value
ORDER BY num DESC
LIMIT 1;
```
output:
```commandline
buddhist  13
```
### 4.2.3 最受欢迎的美食
```commandline
SELECT nodes_tags.value, COUNT(*) as num
FROM nodes_tags
JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value='restaurant')
i
ON nodes_tags.id=i.id
WHERE nodes_tags.key='cuisine'
GROUP BY nodes_tags.value
ORDER BY num DESC
LIMIT 10;
```
```commandline
                               0   1
0                        chinese  12
1                       regional   4
2                          asian   2
3                       barbecue   2
4                       japanese   2
5                            BBQ   1
6                         burger   1
7  burger;italian_pizza;american   1
8                  chinese;local   1
9                chinese;noodles   1
```
# 5. 结论
尽管我对这份数据进行了部分清理，这里面仍有不少细节还需要继续处理，可以想象数据非常需要耐心和细心。在处理数据过程中，也提醒我，在参与贡献数据的时候，应当尽量避免去带入“脏数据”。