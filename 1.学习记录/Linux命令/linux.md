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