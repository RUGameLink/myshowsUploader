from selenium import webdriver
from bs4 import BeautifulSoup as BS
import time

def video_parser(i,*params):
	video_id = "http://www.youtube.com/watch?v=" + i.get("data-context-item-id", "")
	title = i.find("a", "yt-uix-tile-link").text
	duration = i.find("span", "video-time").contents[0].text
	views = i.find("ul", "yt-lockup-meta-info").contents[0].text
	#views_num = "".join([i for i in views if i.isdigit()])
	date = i.find("ul", "yt-lockup-meta-info").contents[1].text
	img = i.find("img")
	thumbnail = "http:" + img.get("src", "") if img else ""
	if "usual" in params:
		return "* {0} // {1} // {2} // {3}\n".format(title, duration, views, date)
	elif  "dokuwiki" in params:
		return "  * [[{0}|{1}]]  //длит: {2}//\n".format(video_id, title, duration)
	elif  "dokuwikifull" in params:
		return "  * {{{{{3}?nolink&100|}}}}[[{0}|{1}]]  //длит: {2}//\n".format(video_id, title, duration, thumbnail)