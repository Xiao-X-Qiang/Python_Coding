-- 链接数据库
	mysql -uroot -p
	mysql -uroot -proot

	-- 退出数据库
	exit/quit/ctro+d

	-- 数据库语句以分号；结尾
	-- 查看所有的数据库
	show databases;

	-- 显示时间
	select now();

	-- 显示数据库版本
	select version();


-- 数据库相关操作

    -- 1.创建数据库
    -- create database 数据库名 charset=utf8;
    create database python04new charset=utf8;
    
    -- 2.查看当前使用的数据库
    select database();

    -- 3.使用数据库
    -- use 数据库的名字
    use python04new;

    -- 4.删除数据库
    -- drop database 数据库名;
    drop database python04;

   	-- 5.查看创建数据库的语句
    -- show crate database ....
    show create database python04;

    -- 6.备份单个数据库及恢复数据库
    	-- 备份数据库
	    -- 命令行下：mysqldump -uroot -p 数据库1名>xxx.sql
	    -- 将数据库中的表结构及数据导出至xxx.sql文件中
	    mysqldump -uroot -p jing_dong >jd.sql

	    -- 恢复数据库
	    -- mysql下新建数据库2,然后命令行模式下导入数据库中的表结构及其数据
	    mysql -uroot -p jing_dong_back <jd.sql

	-- 备份所有的数据库及恢复数据库 推荐
		-- 备份所有数据库
		-- 命令行下：
		mysqldump -uroot -p --all-databases --lock-all-tables > ~/master_db.sql
			-- -u:用户名
			-- -p:密码
			-- --all-databases:导出所有数据库
			-- --lock-all-tables:执行操作时锁住所有表，防止操作时有数据修改
			-- ~/master_db.sql：导出数据库的文件位置

		-- 恢复所有的数据库
		-- 命令行下：
		mysql –uroot –p < master_db.sql



-- 数据表结构的操作

	-- 1.创建表结构
    -- auto_increment表示自动增长
    -- not null 表示不能为空
    -- primary key 表示主键
    -- default 默认值
    -- create table 数据表名字 (字段 类型 约束[, 字段 类型 约束]);


		create table students(
	        id int unsigned not null auto_increment primary key,
	        name varchar(30),
	        age tinyint unsigned default 0,
	        high decimal(5,2),
	        gender enum("男", "女", "中性", "保密") default "保密",
	        cls_id int unsigned
	    );

		create table classes(
	        id int unsigned not null auto_increment primary key,
	        name varchar(30)
	    );

	-- 2.查看表结构
	-- desc 数据表的名字;
	desc student;

	-- 3.查看表的创建语句
	-- show create table 表名字;
	show create table students;

	-- 4.修改表结构
	    -- 1.修改表-添加字段
	    -- alter table 表名 add 列名 类型;
	    alter table students add birthday datetime;

	    -- 1.1 修改表-添加外键
	    -- 表A的外键字段1，字段1与字段2数据类型必须一致，同时字段1的内容必须是字段2的内容-数据一致
	    -- alter table 表1 add foreign key (字段1) references 表2(字段2);
	    alter table students add foreign key (cls_id) references classes(id);
	 
	    -- 2.1  修改表-修改字段：不重命名版
	    -- alter table 表名 modify 列名 类型及约束;
	    alter table students modify birthday date;

	    -- 2.2 修改表-修改字段：重命名版
	    -- alter table 表名 change 原名 新名 类型及约束;
	    alter table students change birthday birth date default "2000-01-01";

	    -- 3.修改表-删除字段
	    -- alter table 表名 drop 列名;
	    alter table students drop high;

	    -- 3.1 修改表-删除外键
	    -- alter table 表名 drop foreign key 外键名；
	    alter table students drop foreign key xxx;

	    	-- 获取外键名称
	    	-- 需要先获取外键约束名称,该名称系统会自动生成,可以通过查看表创建语句来获取名称
	    	-- 会显示CONSTRAINT `students_ibfk_1` FOREIGN KEY (`cls_id`) REFERENCES `classes`...，则students_ibfk_1是外键名称
	    	show create table students;  
	    	


    -- 5.删除表
    -- drop table 表名;
    -- drop database 数据库;
    drop table xxxxx;


-- 数据表数据操作---增删改查(curd)

    -- 1.增加
	    -- 1.全列插入
	    -- insert [into] 表名 values(...)
	    -- 主键字段 可以用 0  null   default 来占位
	    -- 非主键字段，对于默认值，只能使用default来占位
	    +--------+-------------------------------------+------+-----+------------+----------------+
	    | Field  | Type                                | Null | Key | Default    | Extra          |
	    +--------+-------------------------------------+------+-----+------------+----------------+
	    | id     | int(10) unsigned                    | NO   | PRI | NULL       | auto_increment |
	    | name   | varchar(30)                         | YES  |     | NULL       |                |
	    | age    | tinyint(3) unsigned                 | YES  |     | 0          |                |
	    | gender | enum('男','女','中性','保密')       | YES  |     | 保密       |                |
	    | cls_id | int(10) unsigned                    | YES  |     | NULL       |                |
	    | birth  | date                                | YES  |     | 2000-01-01 |                |
	    +--------+-------------------------------------+------+-----+------------+----------------+
		    -- 向students表插入 一个学生信息（一行一行数据插入，用values）
		    insert into students values(0, "小李飞刀", 20, "女", 1, "1990-01-01");
		    insert into students values(null, "小李飞刀", 20, "女", 1, "1990-01-01");
		    insert into students values(default, "小李飞刀", 20, "女", 1, "1990-01-01");

		    -- 枚举中 的 下标从1 开始 1---“男” 2--->"女"....
	        insert into students values(default, "小李飞刀", 20, 1, 1, "1990-02-01");	

	    -- 2.部分插入（一行一行数据插入，用values）
        -- insert into 表名(列1,...) values(值1,...)
        insert into students (name, gender) values ("小乔", 2);

    	-- 3.多行插入（一行一行数据插入，用values）
    	insert into students (name, gender) values ("大乔", 2),("貂蝉", 2);
        insert into students values(default, "西施", 20, "女", 1, "1990-01-01"), (default, "王昭君", 20, "女", 1, "1990-01-01");

        -- 4.列插入（一列一列数据插入，不用values）
        insert into goods_cates1(name) (select cate_name from goods group by cate_name);  #一列列插入
        insert into goods_cates1(name,price) (select cate_name,price from goods);  #一列列插入

    -- 2.修改
     -- update 表名 set 列1=值1,列2=值2... where 条件;
        update students set gender=1; -- 全部都改
        update students set gender=1 where name="小李飞刀"; -- 只要name是小李飞刀的 全部的修改
        update students set gender=1 where id=3; -- 只要id为3的 进行修改
        update students set age=22, gender=1 where id=3; -- 只要id为3的 进行修改

    -- 3.基本查询
    	-- 1.查询所有列
        -- select * from 表名;
        select * from students;

        -- 2.查询指定列
        -- select 列1,列2,... from 表名;
        select name,gender from students;

        ---3.定条件查询
        select * from students where name="小李飞刀"; -- 查询 name为小李飞刀的所有信息
        select * from students where id>3; -- 查询 name为小李飞刀的所有信息

        -- 4.可以使用as为列或表指定别名
        -- select 字段[as 别名] , 字段[as 别名] from 数据表 where ....;
        select name as 姓名,gender as 性别 from students;

        -- 5.字段的顺序
        select id as 序号, gender as 性别, name as 姓名 from students;
	

    -- 4.删除  删除记录
        -- 1.物理删除
        -- delete from 表名 where 条件
        delete from students; -- 整个数据表中的所有数据全部删除
        delete from students where name="小李飞刀";  #删除记录

        -- 2.逻辑删除  推荐
        -- 用一个字段来表示 这条信息是否已经不能再使用了
        -- 给students表添加一个is_delete字段 bit 类型
        alter table students add is_delete bit default 0;
        update students set is_delete=1 where id=6;
 
