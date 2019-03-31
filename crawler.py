# 20100206
# Azan Bin Zahid


from bs4 import BeautifulSoup
import requests
import os
import urllib.parse

sites  = [	
			"https://ieee.lums.edu.pk" , 
			"http://dascon.com.pk" ,
			"https://giftentials.wordpress.com/" , 
			"https://www.samsung.com/", 
			"http://www.carameltechstudios.com/",
			"https://www.syedfaaizhussain.com/",
			"http://learnyouahaskell.com/",
			"Select to enter your own url"
		]

for idx, site in enumerate(sites):
	print (idx, ". ", site)

user = input("Select choice or Enter new URL : ")


if (int(user) < len(sites)-1):
	site = sites[int(user)]
else:
	site = input("Enter proper url as described in above options: ")	


# naming
COUNT = 0
def increment():
    global COUNT
    COUNT = COUNT+1
    return str(COUNT)


urlSet = set();

def crawl(url):
	if (url not in urlSet and '#' not in url and "mailto" not in url):
		urlSet.add(url)
		try:
			req = requests.get(url)
			req.raise_for_status()
			soup = BeautifulSoup(req.text, 'html.parser')
			
			#file writing with 1 2 3 ..
			Html_file= open(increment() + ".html","w", encoding="utf-8")
			Html_file.write(req.text)
			Html_file.close()
			
			#if written succefully
			print ("Downloading: " + url)

			#inside page
			for x in soup.find_all('a', href=True):
				x = x['href']
				x = urllib.parse.urljoin(url, x)
				#abc.com/*
				if (x[0:len(site)]==site):
					crawl(x)
	

	
		except requests.exceptions.HTTPError as err:
			pass
		except:
			pass
		

crawl(site)
# print (urlSet)


