## 常用命令

1. 后台运行

   ```
   # 创建一个新的窗口
   screen -S test
    
   # 进入窗口后 执行文件
   python test.py
    
   # 退出当前窗口
   ctrl+a+d   （方法1：保留当前窗口）
   screen -d  （方法2：保留当前窗口）
   exit       （方法3：退出程序，并关闭窗口）
    
   # 查看窗口
   screen -ls
    
   # 重新连接窗口
   screen -r id或窗口名称
    
   # 示例：
   screen -r 344 
   screen -r test
   ```

   参考链接

   https://blog.csdn.net/Pan_peter/article/details/128875714

2. ```
   tar
   tar -cvf 打包文件.tar 文件/目录
   tar命令实现将文件/目录打包为.tar压缩包。
   -c 创建压缩包
   -v 显示操作过程
   -f 指定输出文件名
   示例:tar -cvf backup.tar dir1 dir2
   tar -cvfz 打包文件.tar.gz 文件/目录
   使用gzip压缩tar包,产生.tar.gz文件。
   -z 使用gzip压缩算法
   tar -cjf 打包文件.tar.bz2 文件/目录
   使用bzip2压缩tar包,产生.tar.bz2文件。
   -j 使用bzip2压缩算法
   tar -xvf 包名.tar
   解压tar包,-x解压。
   tar -xzf 包名.tar.gz
   解压gz格式的tar包。
   tar -xjf 包名.tar.bz2
   解压bz2格式的tar包。
   tar -tf 包名.tar
   查看tar包内容,-t列出。
   tar -rf 新包名.tar 已有包名.tar
   向已经存在的tar包中添加文件。
   
   
   tar -xvf 文件.tar -C 指定目录
   ```

3. 