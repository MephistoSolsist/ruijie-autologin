from login import login
from mail import mail
import time

def main():
    res = login()
    content = ""
    if eval(res.text)['result']=="success":
        ip = res.headers['Set-Cookie'].split(";")[2].split(",")[2]
        user = res.headers['Set-Cookie'].split(";")[2].split(",")[3][:-1]
        time_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        content = "校园网重连成功\n"+"ip:"+ip+"\nuser:"+user+"\ntime:"+time_str
    else:
        content = "校园网重连失败\n"+"错误信息:"+eval(res.text)["message"]
    print(res.text)
    mail(content)

if __name__ == '__main__':
    main()