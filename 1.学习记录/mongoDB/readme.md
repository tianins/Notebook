## MongoDB使用相关教程

#### 基于python构建MongoDB数据库

1. 安装MongoDB

   ```
   官方安装教程
   https://www.mongodb.com/zh-cn/docs/manual/tutorial/install-mongodb-on-ubuntu/
   
   https://blog.csdn.net/lion_no_back/article/details/128513143
                           
   原文链接：https://blog.csdn.net/yutu75/article/details/110941936
   
   新建环境
   conda create -n MongoDB python=3.10 -y
   安装MongoDB
   pip install pymongo
   ```

   安装数据库报错

   ```
   The following packages have unmet dependencies:
    mongodb-org-mongos : Depends: libssl1.1 (>= 1.1.1) but it is not installable
    mongodb-org-server : Depends: libssl1.1 (>= 1.1.1) but it is not installable
    mongodb-org-shell : Depends: libssl1.1 (>= 1.1.1) but it is not installable
   E: Unable to correct problems, you have held broken packages.
   
   sudo apt-get install libssl1.1
   提示找不到
   解决办法：
   手动下载
   wget http://archive.ubuntu.com/ubuntu/pool/main/o/openssl/libssl1.1_1.1.0g-2ubuntu4_amd64.deb
   sudo dpkg -i ./libssl1.1_1.1.0g-2ubuntu4_amd64.deb
   rm -i libssl1.1_1.1.0g-2ubuntu4_amd64.deb
   
   参考教程
   https://askubuntu.com/questions/1403619/mongodb-install-fails-on-ubuntu-22-04-depends-on-libssl1-1-but-it-is-not-insta
   ```

   无法从浏览器访问

   ```
   提示
   It looks like you are trying to access MongoDB over HTTP on the native driver port.
   后面再研究吧
   ```

   

2. 数据库基本操作

   ```python
   from pymongo import MongoClient
   
   cars = [ {'name': 'Audi', 'price': 52642},
       {'name': 'Mercedes', 'price': 57127},
       {'name': 'Skoda', 'price': 9000},
       {'name': 'Volvo', 'price': 29000},
       {'name': 'Bentley', 'price': 350000},
       {'name': 'Citroen', 'price': 21000},
       {'name': 'Hummer', 'price': 41400},
       {'name': 'Volkswagen', 'price': 21600} ]
   
   mydict = { "name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com" }
   
   # MongoClient用于和Mongo的通信，传递MongoClient主机名和端口号
   client = MongoClient('mongodb://localhost:27017/')
   
   
   # 获取对testdb2的数据库的引用
   db = client["testdb2"]
   mycars = db["cars"]
   mysites = db["sites"]
   
   # 数据插入
   
   # 使用insert_many()方法，将文档插入cars集合，集合会自动创建
   # x = mycars.insert_many(cars)
   # print(x.inserted_ids)
   # # 使用insert_one(mydict),插入一条数据
   # x = mysites.insert_one(mydict)
   # # 如果在插入文档时没有指定_id,MongoDB 会为每个文档添加一个唯一的 id。
   # print(x.inserted_id)
   
   
   # 数据查询
   
   # 查询一条数据
   # x = mycars.find_one()
   # print(x)
   
   # 查询所有数据
   # 使用find()方法选择集合或者视图中的文档，返回所选文档。游标是对查询结果集的引用
   # cars = db.cars.find()
   # # 使用for循环遍历结果集
   # for car in cars:
   #     print('{0} {1}'.format(car['name'], 
   #         car['price']))
   
   # 查询指定字段的数据，需要返回的字段设置为1
   # for x in mycars.find({},{'name':1}):
   #     print(x)
       
   # 根据指定条件查询
   # myquery = {"name":"Volvo"}
   # 以下实例用于读取 name 字段中第一个字母为 "R" 的数据
   # myquery = { "name": { "$regex": "^A" } }  #正则表达式
   # myquery = { "price": { "$gt":90000} }  # 查询价格大于90000的
   # for x in mycars.find(myquery):
   #     print(x)
   
   # 返回指定条数记录
   # for x in mycars.find({},{'name':1}).limit(3):
   #     print(x)
   
   
   # 修改数据
   # 修改一条
   # myquery = { "name": "Bentley"}
   # newvalues = { "$set": { "name":"Bentley2"} }
   # # mycars.update_one(myquery,newvalues)
   
   # # 修改多条
   # mycars.update_one(myquery,newvalues)
   
   # for i in mycars.find({'name':{ "$regex": "^B" }}):
   #     print(i)
       
   # 删除数据
   # 删除一条
   # myquery = {'name':"Bentley2"} 
   # mycars.delete_one(myquery)
   # for i in mycars.find():
   #     print(i)
   # 删除多条
   # myquery = {'name':"Audi"}   
   # mycars.delete_many(myquery)
   # for i in mycars.find():
   #     print(i)
   # 删除所有文档
   # x = mycars.delete_many({})
   # print(x.deleted_count, "个文档已删除")
   # # 删除集合
   # cars.drop()
   # print(db.list_collection_names())
   
   
   # 打印数据库中的集合
   # print(db.list_collection_names())
   
   
   ```

   ```
   注意: 在 MongoDB 中，数据库只有在内容插入后才会创建! 就是说，数据库创建后要创建集合(数据表)并插入一个文档(记录)，数据库才会真正创建。
   ```

   

   ```
   命令行
   mongo
   查询所有数据库
   show_dbs 
   使用数据库
   use testdb
   查询集合
   db.cars.find()
   ```

   

```
https://blog.csdn.net/abments/article/details/138275899
```

