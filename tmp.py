# coding:utf-8 
import re

def emoji_print(rawstring):
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


s = u'【买】<span class="emoji emoji1f604"></span>过滤掉了'
print emoji_print(s)


