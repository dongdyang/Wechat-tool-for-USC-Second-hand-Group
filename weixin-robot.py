#!/usr/bin/env python
# coding: utf-8
#

from wxbot import *
import re


class MyWXBot(WXBot):
    
    def handle_msg_all(self, msg):
        try:        
            gid1 = '' 
            gid2 = ''
            group_name1 = u'USC 二手市场'
            group_name2 = u'USC 二手市场 二群'
            group_msg_id = 3
            for group in self.group_list:
                if group['NickName'] == group_name1:
                    gid1 = group['UserName']
                if group['NickName'] == group_name2:
                    gid2 = group['UserName']
      
            msg_head = msg['user']['name']

            msg_cont = msg.get('content')['data']

            name = ''

            def emoji(rawstring):
            # 提取所有表情html
            # 替换所有表情
                flag = True
                while flag:
                    start = rawstring.find('<span')
                    end = rawstring.find('></span>')
                    if start < 0 or end < 0:
                        flag = False
                        break
                    emojistr = rawstring[start : end + 8]
                    try:
                        emojicode = re.search(' emoji(.+?)\"', emojistr).group(1)
                        emoji = chr(int(emojicode, 16))
                    except:
                        emoji = ""
                    rawstring = rawstring.replace(emojistr, emoji)
                return rawstring


            if msg['content']['type'] == 0:
                if msg_head == group_name1:
                    name = msg['content']['user']['name']
                    name = emoji(name)
                    if msg_cont.find(u'收') != -1 or msg_cont.find(u'出') !=-1 or msg_cont.find(u'买') != -1  or msg_cont.find(u'卖') != -1:
                        msg_cont = emoji(msg_cont)
                        print msg_cont
                        self.send_msg_by_uid(name + " : " + msg_cont, gid2)
                if msg_head == group_name2:
                    name = msg['content']['user']['name']
                    name = emoji(name)
                    if msg_cont.find(u'收') != -1 or msg_cont.find(u'出') !=-1 or msg_cont.find(u'买') != -1  or msg_cont.find(u'卖') != -1:
                        msg_cont = emoji(msg_cont)
                        print msg_cont
                        self.send_msg_by_uid(name + " : " + msg_cont, gid1) 
           
            msg_id = msg['msg_id']

            if msg['content']['type'] == 3:
                if msg_head == group_name1:
                    name = msg['content']['user']['name']
                    name = emoji(name)
                    self.get_msg_img(msg_id) 
                    self.send_msg_by_uid(name + u"   的图", gid2)
                    self.send_img_msg_by_uid('./temp/img_'+str(msg_id)+'.jpg', gid2)
                if msg_head == group_name2:
                    name = msg['content']['user']['name']
                    name = emoji(name)
                    self.get_msg_img(msg_id) 
                    self.send_msg_by_uid(name + u"   的图", gid1)
                    self.send_img_msg_by_uid('./temp/img_'+str(msg_id)+'.jpg', gid1)
        except: 
            time.sleep(5)

def main():

    bot = MyWXBot()
    bot.DEBUG = True
    bot.conf['qr'] = 'tty'
    bot.run()


if __name__ == '__main__':
    main()
