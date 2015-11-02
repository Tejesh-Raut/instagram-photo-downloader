
import sys
import urllib.request
import getpass
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


##############################################################################################
###########     uncomment the lines below  if you are using chrome as wbdriver   #############
######                           and comment next block                                #######
##############################################################################################

print ("Give the path for chromedriver  as eg.")
print (" for windows if chromedriver.exe  is in <folderpath> then path '<folderpath>/chromedriver' ")

#path_to_chromedriver_by_read = input("Give the path for chromedrier ")
path_to_chromedriver ='/Users/Gangesh/Downloads/Programs/chromedriver'
driver = webdriver.Chrome(executable_path = path_to_chromedriver)
##############################################################################################

###########     uncomment the lines below  if you are using Firefox as wbdriver   #############
######                           and comment prevoius block                            #######
##############################################################################################
#driver = webdriver.Firefox()
##############################################################################################
url = "https://instagram.com/"
driver.implicitly_wait(10) # seconds
driver.get(url)
elem01 = driver.find_element_by_css_selector('input[name=\"username\"]')
elem02 = driver.find_element_by_css_selector('input[name=\"password\"]')
print ("login to your instagram account")
login_name = input("username: ")
password = getpass.getpass('password: ')
elem01.send_keys(login_name)
elem02.send_keys(password)
elem02.send_keys(Keys.RETURN)
username = input("Enter the instagram's username of interested person :",)
driver.implicitly_wait(10)
elem0 = driver.find_element_by_css_selector('input[placeholder=\"Search\"]')
elem0.send_keys(username)
elem03 = driver.find_elements_by_class_name("-cx-PRIVATE-Search__resultTitleText")
name = elem03[0].text
url = "https://instagram.com/" + name
driver.get(url)
assert "Sorry, this page isn't available." not in driver.page_source
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
		home = driver.find_element_by_class_name("-cx-PRIVATE-Navigation__menuLink").get_attribute('href')
		driver.get(home)
		logout_url = driver.find_element_by_class_name("-cx-PRIVATE-Navigation__menuLink").get_attribute('href')
		driver.get(logout_url)
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