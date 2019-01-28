
-- 视图
	-- 通俗的讲，视图就是一条SELECT语句执行后返回的结果集
	-- 视图是对若干张基本表的引用，一张虚表，查询语句执行的结果，不存储具体的数据（基本表数据发生了改变，视图也会跟着改变）
	-- 视图只用于进行查询，不进行修改相关的任何操作

	-- 视图作用：
	-- 对数据库重构，却不影响程序的运行
	-- 提高了安全性能，可以对不同的用户
	-- 让数据更加清晰


	--1.定义视图
	-- create view 视图名 as select语句；
	-- 对于视图而言，字段名不能重复
	-- 对于select语句查询多表的结果可以有重复，但将其创建为视图v_goods_info后，视其为逻辑上的一张表，表的字段名不允许重复
	create view v_goods_info as select g.*,c.name as cate_name,b.name as brand_name from goods as g left join
	goods_cates as c on g.cate_id=c.id left join goods_brands as b on g.brand_id=b.id;

	-- 2.查看视图结构
	-- desc 视图名
	desc v_goods_info;

	-- 3.删除视图
	-- 类比于 drop table 表名
	-- drop view 视图名
	drop view v_goods_info;

-- 事务
	-- 完成某件事需要执行多条SQL语句，而且要么全部完成，要么一条也不执行，此时就需要事务，其保证了数据的完整一致性

	下面举一个银行应用是解释事务必要性的一个经典例子。假如一个银行的数据库有两张表：支票表（checking）和储蓄表（savings）。
	 现在要从用户Jane的支票账户转移200美元到她的储蓄账户，那么至少需要三个步骤：
		1.检查支票账户的余额高于或者等于200美元。
		2.从支票账户余额中减去200美元。
		3.在储蓄帐户余额中增加200美元。

	-- 现在可以用start transaction;或begin;语句开始一个事务：
		-- 要么使用commit提交将修改的数据持久保存
		-- 要么使用rollback回滚所有的修改，事务SQL的样本如下：

		1.start transaction;
		2.select balance from checking where customer_id=10233276;
		3.update checking set balance=balance-200 where customer_id=10233276;
		4.update savings set balance=balance+200 where customer_id=10233276;
		5.commit;

	-- 1.事务的四大特性：(ACID)
		-- 1.原子性 Atomicity
		-- 一个事务必须被视为一个不可分割的最小工作单元，整个事务中的所有操作要么全部提交成功，要么全部失败回滚.对于一个事务来说，不可能只执行其中的一部分操作，即原子性
		-- 要么三个步骤全部完成，要么一件也不做

		-- 2.一致性 Consistency
		-- 数据库总是从一个一致性的状态转换到另一个一致性的状态
		-- 在上述例子中，一致性确保即使在执行第三、四条语句之间时系统崩溃，支票账户中也不会损失200美元，因为事务最终没有提交，所以事务中所做的修改也不会保存到数据库中

		-- 3.隔离性 Isolation
		-- 通常来说，一个事务所做的修改在最终提交以前，对其他事务是不可见的
		-- 在前面的例子中，当执行完第三条语句、第四条语句还未开始时，此时有另外的一个账户汇总程序开始运行，则其看到支票帐户的余额并没有被减去200美元

		-- 4.持久性 Durability
		-- 一旦事务提交，则其所做的修改会永久保存到数据库
		-- 此时即使系统崩溃，修改的数据也不会丢失


		-- 注意：
		-- 在MySQL客户端中，默认开启事务，只是单句成事务，可以显示开启；在python中，默认开启事务，因为需要在修改数据库数据时，显示commit提交事务；
		-- 对于隔离性而言，可以理解为：某用户A操作某数据时，对其进行了加锁操作，在没有commit或rollback解锁前，其它用户B对同一数据的修改会被阻塞；
		-- 用户对数据的修改，在commit前只对自己可见-隔离性；
		-- 修改数据的命令会自动的触发事务，包括insert、update、delete

	-- 2.开启事务
		-- 开启事务后执行修改命令，变更会维护到本地缓存中，而不维护到物理表中
		-- 加锁、只对自己可见
		-- begin; 或 start transaction;
		begin;  或者 
		start transaction;

	-- 3.提交或回滚事务
		commit;  # 提交事务
		rollback;  # 回滚事务


-- 索引
	-- 加快查询的速度，引入索引，其包含着对数据表中某字段的所有记录的引用指针；
	-- 对于数据表中的主键，数据库默认创建了索引

	-- 1.查看索引
	-- show index from 表名；
	show index from goods;

	-- 2.创建索引
	-- create index 索引名 on 表名(字段名(长度))；
	-- 如果指定字段是字符串，需要指定长度，建议长度与定义字段时长度一致
	-- 如果字段类型不是字符串，可以缺省长度
	create index cate_name on goods_cates(name(40));

	-- 3.删除索引
	-- drop index 索引名 on 表名；
	drop index cate_name on goods_cates;

	-- 注意：
	-- 建立太多的索引会影响更新和插入数据的速度，因为修改数据时，不仅要修改数据本身，还要更新索引文件
	-- 对于经常需要查询、数据量大的字段建议建立索引；
	-- 对于经常需要更新、数据量小、不经常使用的字段不建议建立索引；


-- 账户管理(了解)
	-- 为保证数据库的安全，创建用户时，为其分配合理的操作权限；
	-- 根据账户所具有的权限的不同，MySQL的账户可以分为以下几种
		-- 服务实例级：可对任意数据库进行任意操作；
		-- 数据库级别：对特定数据库进行任意操作；
		-- 数据表级别：对特定表进行所有操作；
		-- 字段级别：对某些表的特定字段进行操作；
		-- 存储级别：对存储程序进行增、改、查等操作
	-- 进行账户操作时，需要使用root账户登录，这个账户拥有最高的实例级权限
	-- 通常都使用数据库级操作权限

	-- 1.查看所有用户
		-- 所有用户及其权限信息存储在mysql数据库中的user表中，desc user;查看表结构,其中：
			-- Host:表示允许访问的主机
			-- User:表示用户名
			-- authentication_string:表示加密后的用户密码
		select host,user,authentication_string from user;

	-- 2.创建账户&授权
		-- 2.1 以root身份登录
		mysql -uroot -p

		-- 2.2 创建账户并授予所有权限
		-- 创建一个laowang的账号，密码为123456，只能通过本地访问, 并且只能对jing_dong数据库中的所有表进行读操作
		grant select on jing_dong.* to 'laowang'@'localhost' identified by '123456';

		-- 创建一个laoli的账号，密码为12345678，可以任意电脑进行远程访问, 并且对jing_dong数据库中的所有表拥有所有权限
		grant all privileges on jing_dong.* to "laoli"@"%" identified by "12345678"

		-- 说明：
			-- 可以操作python数据库的所有表，方式为:jing_dong.*
			-- 访问主机通常使用 百分号% 表示此账户可以使用任何ip的主机登录访问此数据库
			-- 访问主机可以设置成 localhost或具体的ip，表示只允许本机或特定主机访问
		-- 2.3 确认用户有哪些权限
		show grants for laowang@"localhost";

		-- 2.4 退出root登录
		quit;

	-- 3.修改权限
		-- 3.1 修改用户的权限
		-- grant 权限名称 on 数据库 to 账户@主机 with grant option;
		-- 修改laowang的权限为允许本地登陆，查询和插入jing_dong的所有数据表
		grant select,insert on jing_dong.* to laowang@"localhost" with grant option;
		flush privileges;  # 刷新权限

		-- 3.2 修改用户密码
		-- 修改user表中的authentication_string字段，注意密码要进行加密-password()
		-- update user set authentication_string=password('新密码') where user='用户名';
		-- password('新密码') 用以对密码进行加密操作
		update user set authentication_string=password('123') where user='laowang';
		flush privileges;  # 刷新权限

	-- 4.删除用户
		-- 删除mysql数据库的user表中的数据
		delete from user where user="laowang";
		flush privileges;  # 刷新权限

	-- 5.远程登陆（谨慎使用）
	-- 禁用，防止暴力破解数据库，可远程ssh至服务器，再进行sql有关操作
		-- 5.1 修改mysqld.cnf配置文件，注释绑定本地127.0.0.1
		-- 重启mysql
		mysql -u用户 -p密码 -P端口 -h远程IP地址


-- 主从同步
	-- 主从同步使得数据可以从一个数据库服务器复制到其他服务器上，在复制数据时，一个服务器充当主服务器（master），其余的服务器充当从服务器（slave），如此可以
	-- 1.读写分开，提升效率：在主服务器上执行写入和更新，在从服务器上向外提供读功能，可以动态地调整从服务器的数量，从而调整整个数据库的性能
	-- 2.数据备份，保证案例：从服务器上备份而不破坏主服务器相应数据

	-- Mysql服务器之间的主从同步是基于二进制日志机制，主服务器使用二进制日志来记录数据库的变动情况，从服务器通过读取和执行该日志文件来保持和主服务器的数据一致
	-- 从服务器可以通过配置文件同步主服务器

	-- 主服务器：
		-- 开启二进制日志
		-- 配置唯一的server-id
		-- 获得master二进制日志文件名其及位置
		-- 创建一个用于slave和master通信的从服务器账号

	-- 从服务器
		-- 配置唯一的server-id
		-- 使用master分配的用户账号读取master二进制日志
		-- 启用slave服务

	-- 具体实现如下：
	-- 主服务器：192.168.95.133
	-- 从服务器：192.168.95.137

	-- 1.修改主服务器mysql配置文件
	-- 找到主数据库的配置文件my.cnf(或者my.ini)，我的在/etc/mysql/my.cnf,在[mysqld]部分插入如下两行：
	[mysqld]
	log-bin=mysql-bin #开启二进制日志
	server-id=1 #设置server-id

	-- 2.重启mysql,创建用于同步的从服务器账号
	-- 2.1进入mysql会话，创建账号并授权：用户:repl 密码:slavepass
	mysql> CREATE USER 'repl'@'192.168.95.137' IDENTIFIED BY 'slavepass';#创建用户
	mysql> GRANT REPLICATION SLAVE ON *.* TO 'repl'@'192.168.95.137';#分配权限
	mysql>flush privileges;   #刷新权限

	-- 3.查看master状态，记录二进制文件名(mysql-bin.000003)和位置(527)：
	mysql> show master status;
	+------------------+----------+--------------+------------------+-------------------+
	| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
	+------------------+----------+--------------+------------------+-------------------+
	| mysql-bin.000003 |      527 |              |                  |                   |
	+------------------+----------+--------------+------------------+-------------------+
	1 row in set (0.00 sec)

	-- 4.修改从服务器mysql配置文件
	[mysqld]
	server-id=2 #设置server-id，必须唯一，区别于主服务器server-id

	-- 5.重启mysql，打开mysql会话，执行同步SQL语句(需要主服务器主机名，登陆凭据，二进制文件的名称和位置)：
	mysql> CHANGE MASTER TO
    ->     MASTER_HOST='192.168.95.133',
    ->     MASTER_USER='repl',
    ->     MASTER_PASSWORD='slavepass',
    ->     MASTER_LOG_FILE='mysql-bin.000003',
    ->     MASTER_LOG_POS=527;

    -- 6.启动slave同步进程
    mysql>start slave;

    -- 7.查看slave状态
    -- 当看到Slave_IO_Running和Slave_SQL_Running,都Yes时，表示同步成功
   	mysql>show slave status \G
   	*************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 192.168.95.133
                  Master_User: repl
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: mysql-bin.000003
          Read_Master_Log_Pos: 527
               Relay_Log_File: mysqld-relay-bin.000002
                Relay_Log_Pos: 457
        Relay_Master_Log_File: mysql-bin.000003
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
              Replicate_Do_DB: 
          Replicate_Ignore_DB: 

    -- 注意：1.master开启二进制日志后默认记录所有库所有表的操作，可通过配置来指定只记录指定的数据库甚至指定的表的操作，具体在mysql配置文件的[mysqld]可添加修改如下选项：
    # 不同步哪些数据库  
	binlog-ignore-db = mysql  
	binlog-ignore-db = test  
	binlog-ignore-db = information_schema  
	  
	# 只同步哪些数据库，除此之外，其他不同步  
	binlog-do-db = game  
	
	-- 2.当出现Slave_IO_Running: NO错误时，如果是克隆关系的多台主机时，由于mysql中的uuid是唯一标识的，而克隆的uuid是相同的，只需修改一下uuid使其各不相同后重启即可
	-- 置在：auto.cnf中修改uuid
	auto.cnf文件一般在  ./var/lib/mysql/auto.cnf , 如果没有那就用linux 查询命令找：find -name auto.cnf


