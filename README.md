### 写在前面

使用 Scrapy 爬取长沙市楼盘信息。将楼盘位置在地图上标记。通过 web 在前端展示。

### Some Info

技术栈：

- 框架 Scrapy
- 数据库 MangoDB
- 后端 Flask
- 地图 百度/腾讯
- 可视化工具：

数据格式（json）：

1. base_info    基本信息

- name	楼盘名字
- address    地址
- tel    联系电话
- average_price    均价
- update    信息更新日期
- tag    标签
- start_date    开盘时间

---



- end_desc    交房时间
- start_desc     开盘描述
- decoration_status    装修状况
- pre_sale_license    预售许可证
- region_plate    区域板块
- property_rights_years    产权年限
- proj_feature    项目特色

2. property_Info    物业信息

- company    物业公司
- category    物业类别
- costs    物业费

3. building_plan    建筑规划

- developer    开发商
- type    建筑类型
- parking_space    车位
- building_area    建筑面积
- area    占地面积
- households    规划户数
- volume_rate    容积率
- greening_rate    绿化率

4. project_desc    项目简介

- info    简介

5. surrounding    周边配套

- s_business    周边商业
- s_park    周边公园
- s_hospital    周边医院
- s_school    周边学校

6. community    小区配套

- info    基本信息

7. traffic_condition    交通状况

- info     基本情况