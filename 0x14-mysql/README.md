# 0x14-mysql

Installing and configuring mysql on my web servers


## 0. Install MySQL
First things first, let’s get MySQL installed on both your `web-01` and `web-02` servers.

MySQL distribution must be `5.7.x`

Example:

```
ubuntu@229-web-01:~$ mysql --version
mysql  Ver 14.14 Distrib 5.7.25, for Linux (x86_64) using  EditLine wrapper
ubuntu@229-web-01:~$
```


## 1. Let us in!

In order for us to verify that your servers are properly configured, we need you to create a user and password for both MySQL databases which will allow the checker access to them.

* Create a MySQL user named holberton_user on both web-01 and web-02 with the host name set to localhost and the password projectcorrection280hbtn. This will allow us to access the replication status on both servers.
* Make sure that holberton_user has permission to check the primary/replica status of your databases.



Example:

``` 
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"
Enter password:
+-----------------------------------------------------------------+
| Grants for holberton_user@localhost                             |
+-----------------------------------------------------------------+
| GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' |
+-----------------------------------------------------------------+
ubuntu@229-web-01:~$
```


## 2. If only you could see what I've seen with your eyes

In order for you to set up replication, you’ll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.

* Create a database named tyrell_corp.
* Within the tyrell_corp database create a table named nexus6 and add at least one entry to it.
* Make sure that holberton_user has SELECT permissions on your table so that we can check that the table exists and is not empty.


```
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"
Enter password:
+----+-------+
| id | name  |
+----+-------+
|  1 | Leon  |
+----+-------+
ubuntu@229-web-01:~$
```




## 3. Quite an experience to live in fear, isn't it?

Before you get started with your primary-replica synchronization, you need one more thing in place. On your primary MySQL server (web-01), create a new user for the replica server.

* The name of the new user should be replica_user, with the host name set to %, and can have whatever password you’d like.
* replica_user must have the appropriate permissions to replicate your primary MySQL server.
* holberton_user will need SELECT privileges on the mysql.user table in order to check that replica_user was created with the correct permissions.


```
ubuntu@229-web-01:~$ mysql -uholberton_user -p -e 'SELECT user, Repl_slave_priv FROM mysql.user'
+------------------+-----------------+
| user             | Repl_slave_priv |
+------------------+-----------------+
| root             | Y               |
| mysql.session    | N               |
| mysql.sys        | N               |
| debian-sys-maint | Y               |
| holberton_user   | N               |
| replica_user     | Y               |
+------------------+-----------------+
ubuntu@229-web-01:~$
```



## 4. Setup a Primary-Replica infrastructure using MySQL



Having a replica member on for your MySQL database has 2 advantages:

Redundancy: If you lose one of the database servers, you will still have another working one and a copy of your data
Load distribution: You can split the read operations between the 2 servers, reducing the load on the primary member and improving query response speed


Requirements:
* MySQL primary must be hosted on web-01 - do not use the bind-address, just comment out this parameter
* MySQL replica must be hosted on web-02
* Setup replication for the MySQL database named tyrell_corp
* Provide your MySQL primary configuration as answer file(my.cnf or mysqld.cnf) with the name 4-mysql_configuration_primary
* Provide your MySQL replica configuration as an answer file with the name 4-mysql_configuration_replica

**Files** - `4-mysql_configuration_primary`, `4-mysql_configuration_replica`
