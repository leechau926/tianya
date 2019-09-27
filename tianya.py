#coding=utf-8
import requests
from bs4 import Tag
from bs4 import BeautifulSoup

def getHtml(url):
	page = requests.get(url)
	html =page.text
	return html

def getText(html):
	get_text = Tag.get_text
	soup = BeautifulSoup(html, 'html.parser')
	author_info = soup.find_all('div', class_='atl-info')
	listauthor = [x.get_text() for x in author_info]

	list_info = soup.find_all('div', class_='bbs-content')
	listtext = [x.get_text() for x in list_info]

	global i
	if i > 1:
		listtext = [""] + listtext

	for x in range(len(listauthor)):
		if "楼主" in listauthor[x]:
			with open('jingying.txt', 'a') as f:
				f.write(listtext[x].strip() + '\n')
				f.write('=======================fengexian====================\n')

if __name__=='__main__':
	for i in range(1,17):
		url = ("http://bbs.tianya.cn/post-develop-965639-%s.shtml" % str(i))
		html = getHtml(url)
		getText(html)
		print('page %d saved.' % i)
# ————————————————
# 版权声明：本文为CSDN博主「悦来客栈的老板」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq523176585/article/details/77836244
