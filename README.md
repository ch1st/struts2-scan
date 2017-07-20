# struts2-scan
概述：
 批量扫描目标是否存在各个版本Struts2漏洞<br>
 目前支持对s2-045,s2-016的批量检测<br>
 基于python3.x版本开发<br>
 检测成功后会程序运行目录处生成success_016/045.txt文件<br/>
# requirement
    pip install requests
# Usage
    python scan.py -f hosts.txt
    Or
    python scan.py -u http://www.xxx.com/index.action
# Result
    
    ![url检测](url.jpg)
