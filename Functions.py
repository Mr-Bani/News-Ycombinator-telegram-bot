#in the name of God`
from urllib.request import urlopen
import urllib
import re

def get_html(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html

#urlopen("https://api.telegram.org/bot2014197859:AAH6bM-p_4y5OspBWe2mBHl141lZiTq6Bu0/sendMessage?chat_id=@News_Ycombinator_1&text={}")






def get_news():
    reg_title = "<a href=\"(.*?)\" class=\"storylink\".*?>(.*?)</a>"
    reg_points = "<span class=\".*?\" id=\".*?\">(.*?) points</span>"
    html1 = get_html("https://news.ycombinator.com/")
    html2=get_html("https://news.ycombinator.com/news?p=2")
    html3=get_html("https://news.ycombinator.com/news?p=3")
    html=html1+'\n'+html2+'\n'+html3
    Titles = re.findall(reg_title, html)
    Points=re.findall(reg_points,html)
    Points=[int(x) for x in Points]
    News=list(zip(Titles,Points))
    return (Titles,News)

Sent_News=[]
Titles=[]

while True:
    Tmp=get_news()
    if Titles!=Tmp[0]:
        for i in Tmp[1]:
            if i[1] > 250:
                if i[0] not in Sent_News:
                    Sent_News.append(i[0])
                    text = urllib.parse.quote("🔵#News" + "\n\n" + i[0][1] + "\n\nPoints: "+str(i[1])+ "\n\n\n"+i[0][0])
                    urlopen("https://api.telegram.org/bot2014197859:AAH6bM-p_4y5OspBWe2mBHl141lZiTq6Bu0/sendMessage?chat_id=@News_Ycombinator_1&text={}".format(text))

        Titles=Tmp[0]

    if len(Sent_News)>100:
        Sent_News.pop(0)