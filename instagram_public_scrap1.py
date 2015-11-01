#from bs4 import BeautifulSoup
import sys
import urllib.request
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

path_to_chromedriver ='/Users/Gangesh/Downloads/Programs/chromedriver'
driver = webdriver.Chrome(executable_path = path_to_chromedriver)


username = input("Enter the instagram's username of interested person :",)
url = "https://instagram.com/" + username


driver.get(url)
print (url)
elem1 = []
elem1 = driver.find_elements_by_class_name("-cx-PRIVATE-Photo__image")
i = 0
j = 0
for span in elem1:
	src = elem1[i].get_attribute('src')
	i=i+1
	j=j+1
	urllib.request.urlretrieve(src, (username+"_insta_" + str(j) + ".jpg"))

check= True

while check == True:
	try:
		elem2 = driver.find_element_by_class_name("-cx-PRIVATE-AutoloadingPostsGrid__moreLink")
		
	except NoSuchElementException:
		check = False
		print("files have been downloaded")
		sys.exit(1)

	if check == True:
		next_href = elem2.get_attribute('href')
		print (next_href)
		#next_url = 'https//instagram.com'+next_href
		driver.get(next_href)
		elem1 = []
		elem1 = driver.find_elements_by_class_name("-cx-PRIVATE-Photo__image")
		i = 0
		for span in elem1:
			src = elem1[i].get_attribute('src')
			i=i+1
			j= j+1
			urllib.request.urlretrieve(src, (username+"_insta_" + str(j) + ".jpg"))
	else:
		check = False


sys.exit(0)