import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import traceback
from selenium.common.exceptions import NoSuchElementException

# global variable the denotes the start of the tripadvisor url
trip_url = "https://www.tripadvisor.in"

def remove_non_ascii(text):
    return ''.join([i for i in text if ord(i)<128])


def parse_island():
	the_url="https://www.tripadvisor.in/Tourism-g189435-Syros_Cyclades_South_Aegean-Vacations.html"
	url = urllib2.urlopen(the_url)
	content = url.read()
	soup = BeautifulSoup(content)
	links = soup.findAll("span", class_="typeName")
	review_links={}
	for link in links:
		id= link.string
		href= link.parent['href']
		review_links[id]=trip_url+href

	#for key in review_links.keys():
	#	print str(key) +"::"+ str(review_links[key])

	hotels_urls=parse_hotels_2(review_links['Hotels'])
	print "found " + str(len(hotels_urls))  +" hotel pages \n \n"
	for url in hotels_urls:
		print url





def parse_hotels(hotels_url):
	print "WILL read " + str(hotels_url)
	url = urllib2.urlopen(hotels_url)
        content = url.read()
        soup = BeautifulSoup(content)
	hotel_links={}
	links = soup.findAll("a",class_="property_title")
	for link in links:
		name= remove_non_ascii(link.string)
		print link.string
		href= remove_non_ascii(str(link['href']))
		hotel_links[name]=href
	#for key in hotel_links.keys():
	#	print str(key) + " -- " + hotel_links[key] 
	return hotel_links


def parse_hotels_2(url):
	"""
	   reads the page and retrieves the links to the hotel pages
	   if more than one pages exist the Next button is clicked using Selenium
           and we continue to retrieve more results
	"""
	driver = webdriver.Firefox()
	driver.get(url)
	hotel_links=[]
	while True:
		try:
			# sleep to allow time for the page to load
			sleep(5)
			next = driver.find_element_by_link_text('Next')
			links = driver.find_elements_by_class_name('property_title')
			for link in links:
				#print link.get_attribute("href")
				hotel_links.append(link.get_attribute("href"))
			if next is None:
				print "finished!!"
				break
			next.click()
		except NoSuchElementException:
			print "finished crawling the hotels page!!"
			return hotel_links
		except:
			print "error"
			traceback.print_exc()
			break


def parse_one_hotel(url):
	pass




parse_island()
