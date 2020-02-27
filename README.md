### 写在前面

使用 Scrapy 爬取长沙市楼盘信息。将楼盘位置在地图上标记。通过 web 在前端展示。

爬取地址：http://m.loupan.com/cs/

### Some Info

技术栈：

- 框架 Scrapy

- 数据库 MangoDB

数据格式（json）：

1. header   描述信息

- name	楼盘名字
- address    地址
- tel    联系电话
- average_price    均价
- update    信息更新日期
- tag    标签
- start_date    开盘时间


2. base_info    基本信息

- end_desc    交房时间
- start_desc     开盘描述
- title    标题
- decoration_status    装修状况
- pre_sale_license    预售许可证
- region_plate    区域板块
- property_rights_years    产权年限
- proj_feature    项目特色

3. property_Info    物业信息

- company    物业公司
- category    物业类别
- costs    物业费

4. building_plan    建筑规划

- developer    开发商
- type    建筑类型
- parking_space    车位
- building_area    建筑面积
- area    占地面积
- households    规划户数
- volume_rate    容积率
- greening_rate    绿化率

5. project_desc    项目简介

- info    简介

6. surrounding    周边配套

- s_business    周边商业
- s_park    周边公园
- s_hospital    周边医院
- s_school    周边学校

7. community    小区配套

- info    基本信息

8. traffic_condition    交通状况

- info     基本情况

9. href    详情链接

---



### Scrapy 部分

通过对网页的分析很容易了解到：[页面列表](http://m.loupan.com/cs/loupan/) 的加载技术是ajax实现的。所以，我们不妨找出 ajax 的请求链接。

在鼠标往下翻到底部时，发现有个加载更多的提示，继续往下滑，页面加载更多的列表。同时，在开发者工具的 Network 中可以看见类似这样的请求：

![image-20200227001740113](image-20200227001740113.png)

显然，请求地址应该是类似这样的：http://m.loupan.com/cs/loupan/p6/ 。即 p6 代表第六页。而且返回的数据中包含了 next_page ，故当我们编写爬虫时，并不一定要自己来构造 url 了，可以直接提取出 next_page 作为我们的下一个地址。不过，仔细观察，你会发现，这里是没有 p1 的。这意味着第一页返回的数据并不是 json 数据。所以对我们对第一页的 response 处理时就不能像下面这样：

```python
import json
data = json.loads(response.text)
```

而是直接使用选择器进行提取：

```
next_info += response.css('div.list > div.item > a::attr(href)').getall()
```

`next_info` 为每个楼盘的详情页。

对于 ajax 的请求，则先进行 json 解析：

```pyth
data = json.loads(response.text)
next_page = data['next_page']
href = Selector(text=data['list_item']).css('a::attr(href)').getall()
```

---

