#!/usr/bin/python3

import emailTool
import sys

complaint_email_addr = {
    "ky":'kyfw@12306.cn',
    "hy":'hyfw@12306.cn',
    "xb":'xbfw@13306.cn'
}

cfg = {
    'Host':'smtp.163.com',
    'From':sys.argv[1],
    'PW':sys.argv[2],
    'To':sys.argv[3],
    'subject':'my dream',
    'content':'I think this is my problem.\n'
}
tool = emailTool.emailTool(cfg)
#tool.sendDelay(10)
tool.sendcyc(5*4*60,5,cfg['content'])
