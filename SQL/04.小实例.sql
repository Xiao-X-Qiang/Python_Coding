
-- 准备数据

	-- 创建 "京东" 数据库
	create database jing_dong charset=utf8;

	-- 使用 "京东" 数据库
	use jing_dong;

	-- 创建一个商品goods数据表
	create table goods(
	    id int unsigned primary key auto_increment not null,
	    name varchar(150) not null,
	    cate_name varchar(40) not null,
	    brand_name varchar(40) not null,
	    price decimal(10,3) not null default 0,
	    is_show bit not null default 1,
	    is_saleoff bit not null default 0
	);

	-- 向goods表中插入数据
	-- 非主键字段，对于默认值，不能使用null、0，只能使用default
	insert into goods values(0,'r510vc 15.6英寸笔记本','笔记本','华硕','3399',default,default); 
	insert into goods values(0,'y400n 14.0英寸笔记本电脑','笔记本','联想','4999',default,default);
	insert into goods values(0,'g150th 15.6英寸游戏本','游戏本','雷神','8499',default,default); 
	insert into goods values(0,'x550cc 15.6英寸笔记本','笔记本','华硕','2799',default,default);


-- 强化练习
	
	-- 查询类型cate_name为 '超极本' 的商品名称、价格
	select name,price from goods where cate_name = '超级本';

	-- 显示商品的种类
	select cate_name from goods group by cate_name;
	select distinct cate_name from goods;

	-- 求所有电脑产品的平均价格,并且保留两位小数,实际过程中，不要使用小数
	select round(avg(price),2) as avg_price from goods;

	-- 显示每种商品的平均价格
	select cate_name,avg(price) from goods group by cate_name;

	-- 查询每种类型的商品中 最贵、最便宜、平均价、数量
	select cate_name,max(price),min(price),avg(price),count(*) from goods group by cate_name;

	-- 查询每种类型中最贵的电脑信息
	select * from goods inner join 
		    (
		        select
		        cate_name, 
		        max(price) as max_price, 
		        min(price) as min_price, 
		        avg(price) as avg_price, 
		        count(*) from goods group by cate_name
		    ) as goods_new_info 
		on goods.cate_name=goods_new_info.cate_name and goods.price=goods_new_info.max_price;


create table customers(
id int unsigned auto_increment not null primary key,
name varchar(40) not null,
address varchar(100),
tel varchar(40),
passwd varchar(100)
);



