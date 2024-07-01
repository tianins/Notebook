## 常见问题

1. #### python路径

   在文件夹中找不到文件

   ```
   报错提示：
   from api_main import router as main_router
   ModuleNotFoundError: No module named 'api_main'
   有几个可能的原因:
   1.api和api_main文件不在同一目录下, Python会使用sys.path自动搜索路径找不到。
   2.路径问题,运行时的当前目录和api_main.py文件实际位置不一致。
   ```

   解决办法

   ```
   1.将api_main.py移动到api目录下
   2.在运行脚本前改变工作目录到research_report目录下:
       import os
       os.chdir('/path/to/research_report')
   3.添加api路径到sys.path:
   	import sys
       import os
       sys.path.append(os.path.dirname(__file__))
   
       from api_main import router
   4.使用相对导入(有效):
   	from .api_main import router
   ```

   

   

2. 