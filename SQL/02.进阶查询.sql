
-- 数据的准备
	-- 创建数据库
	create database python_test charset=utf8;

	-- 使用数据库
	use python_test;

	-- 显示当前使用的数据库
	select database();

	-- 创建数据表 students classes
	-- students表
	create table students(
	    id int unsigned primary key auto_increment not null,
	    name varchar(20) default '',
	    age tinyint unsigned default 0,
	    height decimal(5,2),
	    gender enum('男','女','中性','保密') default '保密',
	    cls_id int unsigned default 0,
	    is_delete bit default 0
	);

	-- classes表
	create table classes (
	    id int unsigned auto_increment primary key not null,
	    name varchar(30) not null
	);

-- 表 students：
+----+-----------+------+--------+--------+--------+-----------+
| id | name      | age  | height | gender | cls_id | is_delete |
+----+-----------+------+--------+--------+--------+-----------+
|  1 | 小明      |   18 | 180.00 | 女     |      1 |           |
|  2 | 小月月    |   18 | 180.00 | 女     |      2 |          |
|  3 | 彭于晏    |   29 | 185.00 | 男     |      1 |           |
|  4 | 刘德华    |   59 | 175.00 | 男     |      2 |          |
|  5 | 黄蓉      |   38 | 160.00 | 女     |      1 |           |
|  6 | 凤姐      |   28 | 150.00 | 保密   |      2 |          |
|  7 | 王祖贤    |   18 | 172.00 | 女     |      1 |          |
|  8 | 周杰伦    |   36 |   NULL | 男     |      1 |           |
|  9 | 程坤      |   27 | 181.00 | 男     |      2 |           |
| 10 | 刘亦菲    |   25 | 166.00 | 女     |      2 |           |
| 11 | 金星      |   33 | 162.00 | 中性   |      3 |          |
+----+-----------+------+--------+--------+--------+-----------+


-- 基本查询
	-- 1.查询所有字段
	-- select * from 表名
	select * from students
	select * from classes

	-- 2.查询指定字段
	-- select 列1，列2... from 表名
	select name,age from students;

	-- 3.使用as为字段起别名
	-- select 字段 [as 别名],字段2 [as 别名]... from 表名;
	select name as 姓名,age as 年龄 from students;

	-- 3.使用as为表起别名
	-- select 别名.字段,别名.字段... from 表名 as 别名；
	select students.name,students.age from students；
	select s.name,s.age from students as s;
	-- 错误的，select students.name,students.age from students as s 

	-- 4.消除重复行
	-- distinct 字段  针对某一个字段
	select distinct gender from students;

-- 条件查询

	-- 1.比较运算符
	-- > >= < <= = !=
		select * from students where age>18;
		select * from students where age<=18;
		select name,gender from students where age!=18;

		-- 查找班级年龄最大,身高最高的学生
		select * from students where (height,age) = (select max(height),max(age) from students);

	-- 2.逻辑运算符
	-- and or not
	-- 优先级：()>not>and>or
		-- 18到28之间的所有学生
		select * from students where age>18 and age<28;

		-- 不在此范围(18岁以上的女性)的学生有：
		-- select * from students where not age>18 or gender!=2;等同于
		select * from students where not (age>18 and gender=2);

		-- 年龄不小于等于18的女性学生有：
		select * from students where not age<=18 and gender=2;

	-- 模糊查询
		-- 1.like
		-- % 表示0个或多个
		-- _ 表示1个
			-- 查询姓名中以“小”开始的名字
			select * from students where name like "小%";

			-- 查询姓名中有"小"的所有名字
			select * from students where name like "%小%";

			-- 查询是两个字的所有名字
			select name from students where name like "__";

			-- 查询至少有两个字的名字
			select name from students where name like "__%";


		-- 2.rlike 正则
			-- 查询以“周”开始的名字
			select name from students where name rlike "^周.*";

			-- 查询以“周”开始，以“伦”结尾的名字
			select name from students where name rlike "^周.*伦$";


	-- 范围查询
		-- 1.in(1,3,8) 表示在一个非连续的范围内
		-- 查询年龄为18、34的姓名 
		select name from students where age in (18,34);

		-- 2.not in(1,3,8)  表示不在一个非连续的范围内
		-- 查询年龄不在18、34的姓名
		select name from students where age not in (18,34);

		-- 3.between ... and ... 表示在一个连续的范围内(包括两端)
		-- 查询年龄在18至34之间的姓名 
		select name,age from students where age between 18 and 34;

		-- 4.not between ... and ... 表示不在一个连续的范围内
		-- 查询年龄不在18至34之间的姓名
		select name from students where age not between 18 and 34;
		-- 错误的 select name from students where age not (between 18 and 34);


	-- 空判断
		-- 1.is null 判空
		-- 查询身高为空的信息
		select * from students where height is null;

		-- 2.is not null 不为空
		-- 查询身高不为空的信息
		select * from students where height is not null;

-- 排序

	-- order by 字段
	-- asc 从小到大排列，即升序 ，默认项
	-- desc 从大到小排列，即降序
	-- 缺省该字段，默认主键从小到大排序

	-- 查询年龄在18至34岁之间的男性，按照年龄从小到大排序；
	select * from students where age between 18 and 34 and gender=1 order by age;
	select * from students where (age between 18 and 34) and gender=1 order by age;  #也正确，加括号后，可读性更强

	-- 查询年龄在18至34之间的女性，身高从高到低排序
	select * from students where age between 18 and 34 and gender=2 order by height desc;

	-- order by 字段1，字段2 以第1字段排序，数值相同时，按第2字段排序，还相同，则按主键从小到大排序
	-- 查询年龄在18至34岁之间的女性，身高从高到低排序，如果身高相同则按年龄从小到大排序；
	select * from students where (age between 18 and 34) and gender=2 order by height desc,age asc;

	-- 按照年龄从小到大排序，身高从高到低排序；
	select * from students order by age asc,height desc;

-- 聚合函数
	-- 1.count() 总数
	-- 查询有多少男性
	select count(*) as "男性人数" from students where gender=1;

	-- 2.max(字段)  字段中的最大值
		-- 查询最大的年龄
		select max(age) as "最大年龄" from students;

		-- 查询女性中的最高身高
		select max(height) from students where gender=2;

	-- 3.min(字段)  字段中的最小值

	-- 4.sum(字段) 字段求和
	-- 计算所有人的年龄总和
	select sum(age) from students;

	-- 5.avg(字段)  求字段的平均值
	-- 计算平均年龄
	select avg(age) from students;
	select sum(age)/count(*) from students;  #select 后可跟表达式

	-- 5.round(字段,num)  保留字段几位小数，默认四舍五入，另在实际过程中避免存储上的误差，应避免存小数，可采用倍数成整数的方法
	-- 计算男性的平均年龄，保留2位小数
	select round(avg(age),2) from students where gender=1;

-- 分组
	 -- 1.group by 字段 #相当于将原始数据表按照字段分别分组,随后的操作对象是分组后的数据(注意分组组间的”主键“,group by 字段)
	 -- 通常，分组和聚合配合着使用方才有意义
		 -- 计算每种性别中的人数
		 select gender,count(*) from students group by gender;
		 -- 错误的，select name,count(*) from students group by gender; 
		 -- 原因在于：对于分组后的4组数据中，每组中select后的字段值应该为一行(因为每组的gender只有一行，最终会有4行)，而对应的name有多个，有歧义，因而会报错

	 -- 2.group_concat(...) # 操作对象是group by后的分组数据
	 -- 查询同种性别中的姓名
	 select gender,group_concat(name,height) from students group by gender;
	+--------+---------------------------------------------------------------------------+
	| gender | group_concat(name,height)                                                 |
	+--------+---------------------------------------------------------------------------+
	| 男     | 彭于晏185.00,刘德华175.00,程坤181.00                                      |
	| 女     | 小明180.00,小月月180.00,黄蓉160.00,王祖贤172.00,刘亦菲166.00              |
	| 中性   | 金星162.00                                                                |
	| 保密   | 凤姐150.00                                                                |
	+--------+---------------------------------------------------------------------------+
	4 rows in set (0.00 sec)


	 select gender,group_concat(name,' age: ',age,' id: ',id) from students group by gender;
	+--------+--------------------------------------------------------------------------------------------------------------------+
	| gender | group_concat(name,' age: ',age,' id: ',id)                                                                         |
	+--------+--------------------------------------------------------------------------------------------------------------------+
	| 男     | 彭于晏 age: 29 id: 3,刘德华 age: 59 id: 4,周杰伦 age: 36 id: 8,程坤 age: 27 id: 9                                  |
	| 女     | 小明 age: 18 id: 1,小月月 age: 18 id: 2,黄蓉 age: 38 id: 5,王祖贤 age: 18 id: 7,刘亦菲 age: 25 id: 10              |
	| 中性   | 金星 age: 33 id: 11                                                                                                |
	| 保密   | 凤姐 age: 28 id: 6                                                                                                 |
	+--------+--------------------------------------------------------------------------------------------------------------------+
	4 rows in set (0.00 sec)

	 -- 3.having
	 -- having 的操作对象是group by后的”逻辑“子数据表，而where 的操作对象是最初的数据表
		 -- 查询不同性别中平均年龄超过30岁的姓名
		 select gender,group_concat(name) from students group by gender having avg(age)>30;
		+--------+--------------------------------------+
		| gender | group_concat(name)                   |
		+--------+--------------------------------------+
		| 男     | 彭于晏,刘德华,周杰伦,程坤            |
		| 中性   | 金星                                 |
		+--------+--------------------------------------+
		2 rows in set (0.00 sec)

		 -- 查询每种性别中的人数多于2个的信息 -- 操作对象是"逻辑"子数据表
		 select gender,group_concat(name) from students group by gender having count(*)>2;
		+--------+---------------------------------------------+
		| gender | group_concat(name)                          |
		+--------+---------------------------------------------+
		| 男     | 彭于晏,刘德华,周杰伦,程坤                   |
		| 女     | 小明,小月月,黄蓉,王祖贤,刘亦菲              |
		+--------+---------------------------------------------+
		2 rows in set (0.00 sec)



	-- 分组后的表可以看作以下形式
	------------------------------------------------
		| gende | id | name | height | is_del | cls_id |
		|       | 1  | 小明 | 188.00 |  0    |   1     |
		|	男	| 3  | 张三 | 175.00 |  0    |   1     |
		|       | 2  | 周杰 | 170.00 |  0    |   2     |


		| gende | id | name | height | is_del | cls_id |
		|       | 1  | 静香 | 180.00 |  0    |   2     |
		|	女	| 3  | 小花 | 176.00 |  0    |   1     |
		|       | 2  | 金星 | 175.00 |  0    |   2     |

	-- 错误的，select name,count(*) from students group by gender;  
	-- 原因在于：对于分组后的4组数据中，每组中select后的字段值应该为一行(因为每组的gender只有一行，最终会有4行)，而对应的name有多个，有歧义，因而会报错
	
	-- 计算不同性别的平均身高
	-- 聚合函数的操作对象也是"逻辑"子数据表
	select gender,avg(height) from students group by gender;


-- 分页
	-- 1.limit count
	-- 查询女性中的前5个数据；
	select * from students where gender=2 limit 5;

	-- 2.limit start,count  #start 下标从0开始，而enum()下标从1开始
	-- 计算方式 limit （第N页-1)*每页的个数,每页的个数
		-- 显示女性，且每页显示4个，显示第3页
		select * from students where gender=2 limit 8,4;
		--错误的 select * from students where gender=2 limit(3-1)*4,4  不能带表达式

		-- 显示女性，且每页显示4个，从第10个开始显示 -- limit start,count  # start下标从0开始
		select * from students where gender=2 limit 9,4;

-- 连接查询
	-- 1.inner join ...on 内连接，取交集部分  即先笛卡尔积-->根据条件筛选记录
	-- select ... from 表A inner join 表B on...
		-- 查询有对应班级信息的学生及其班级信息
		select * from students inner join classes on students.cls_id=classes.id;

		-- 按要求显示姓名、班级  显示指定列
		select students.*,classes.name from students inner join classes on students.cls_id=classes.id;
		select classes.name,students.id,students.name from students inner join classes on students.cls_id=classes.id;

		-- 为数据表起别名后，所有的数据表名都要使用简写
		select c.name,s.id,s.name from students as s inner join classes as c on s.cls_id=c.id;

		-- 查询有班级信息的学生及其班级信息，并按照班级进行排序
		select c.name,s.name,s.id from students as s inner join classes as c on s.cls_id=c.id order by s.cls_id;

		-- 查询有班级信息的学生及其班级信息，并按照班级排序、id降序排列
		select c.name,s.name,s.id from students as s inner join classes as c on s.cls_id=c.id order by s.cls_id,s.id desc;

	-- 2.left join ...on 左连接 以左表为基准，以右表内容向其填充，无匹配项时置为null
	-- 查询没有班级信息的学生信息
	select * from students as s left join classes as c on s.cls_id=c.id having c.id is null;  # having，操作对象是逻辑子表,同group by

	-- 3.right join ...on 右连接
	-- 将两数据表调换即成左连接，用left join完成

-- 自关联
	-- 省级联动  http://demo.lanrenzhijia.com/2014/city0605/
	-- 将省、市、县三张表中的数据放在同一表中，其中，市的pid是省的aid(市隶属于省),县的pid是市的aid(县隶属于市)
	-- 一张表通过as别名的方式，可认为其为多张表，可进行表与表之间内连接、左连接等查询

	-- areas表如下：
	mysql> select * from areas limit 4,3;
	+--------+--------------+--------+
	| aid    | atitle       | pid    |
	+--------+--------------+--------+
	| 110103 | 朝阳区       | 110100 |
	| 110104 | 丰台区       | 110100 |
	| 110105 | 石景山区     | 110100 |
	+--------+--------------+--------+
	3 rows in set (0.00 sec)

	-- 查询有哪些省
	select * from areas where pid is null;

	-- 查询出河南省有哪些市
	select * from areas as province inner join areas as city on province.aid=city.pid having province.atitle="河南省";

	-- 查询出新乡市有哪些县
	select * from areas as province inner join areas as city on province.aid=city.pid having province.atitle="新乡市";

-- 子查询
	-- 当查询语句中有未知变量时，需要进一步查询获知该值，这就是子查询

	-- 标量子查询，子查询返回的结果是一个数据(一行一列)
	-- 查询最高的男生信息
	select * from students where height = (select max(height) from students);

	-- 行子查询，返回的结果是一行(一行多列)
	-- 查找班级年龄最大,身高最高的学生
	select * from students where (height,age) = (select max(height),max(age) from students);

	-- 列子查询，返回的结果是一列(一列多行)
	-- 在课程表中查询被学生选择的课程名
	select name from classes where id in (select cls_id from students);

	-- 表子查询，返回的结果是多行多列
	-- 对于子查询的结果可以将其as后作表看待，其实行、列子查询也可以如此操作
	-- 查询goods表中每类商品价格最贵的商品信息
	select * from goods inner join (select cate_id,max(price) as max_price from goods group by cate_id) 
	as goods_new on goods.cate_id=goods_new.cate_id and goods.price=goods_new.max_price;


-- 数据库的设计
	-- 范式
	-- 1.第一范式：原子性，即列不能再分成其它列
	-- 2.第二范式：表中必须有主键；其它列必须完全依赖于主键，不能部分依赖主键；
	-- 3.第三范式：非主键列必须直接完全依赖于主键，不能传递依赖于主键；

	-- ER模型  怎样定义实体及其间的关系
	-- E-Entry:实体    Relationship:关系
	-- 1.实体A对实体B为1对1，则在表A或表B中创建一个字段，存储另一表的主键值；
	-- 2.实体A对实体B为1对多，则在表B中创建一个字段，存储表A的主键值
	-- 3.实体A对实体B为多对多，则新建一张表C，这个表只有两个字段，分别存储表A与表B的主键值；











