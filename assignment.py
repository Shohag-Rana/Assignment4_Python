import mysql.connector
import requests
import json
from bs4 import BeautifulSoup

# Mysql database operation 

#establishing the connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root123456",
  database = "kayakHotelDB",
)
#Creating a cursor object using the cursor() method
cursor = mydb.cursor()
# Database Create queries
'''
    #create a database name kayakHotelDB
    cursor.execute("CREATE DATABASE kayakHotelDB")  

    #Creating table as per requirement
    cursor.execute("CREATE TABLE Hotels_All_City (city_name VARCHAR(255), city_hotel_id VARCHAR(255), hrf_link VARCHAR(255))")

    #Creating table for storing single city hotel data
    cursor.execute("CREATE TABLE Single_City_Hotel_List (hotel_name VARCHAR(255), hotel_id VARCHAR(255), hrf_link VARCHAR(255))")

    #Creating table for storing hotel image details
    cursor.execute("CREATE TABLE Hotel_With_Image_Details (hotel_id VARCHAR(255), hotel_name VARCHAR(255), image_link VARCHAR(255), label VARCHAR(255))")

'''

# find hotel id
def find_hotel_id(href):
    id = ""
    length = len(href)
    for i in range(0, length-1):
        if(href[i] >= '0' and href[i] <= '9'):
            id += href[i]
    return id

# first page operation and find out the city name, city hotel id, and hotel link 
# all the hotel links by the city
soup = BeautifulSoup(requests.get("https://www.kayak.co.in/?ispredir=true").text, features='html.parser')
hotels_links_by_city = []
elems = soup.find_all("div", {"class": "P_Ok-wrapper"}) #this div contains city name and cars, flights, hotels link  
for elem in elems:
    city_name = elem.find("h3", 'P_Ok-title') # Extract the city name 
    city_name = city_name.getText()
    carFlightHotels_links = elem.find_all("a", href=True)
    for link in carFlightHotels_links:
        find_hotel = (link['href']).find('hotel') # Find out the hotel link only.
        if (find_hotel != -1):
            hotels_links_by_city.append("https://www.kayak.co.in"+link['href'])
            city_hotel_Id= find_hotel_id(link['href'])
            city_name = city_name
            city_hotel_link = "https://www.kayak.co.in" + link['href']
            # insert city hotel information into databases
            sql = "INSERT INTO Hotels_All_City (city_name, city_hotel_id, hrf_link) VALUES (%s, %s, %s)"
            val = (city_name, city_hotel_Id, city_hotel_link)
            cursor.execute(sql, val)
            mydb.commit()

# second page operation 
# Find out all the hotel includes in a city (Ex - In this Program we select London City's Hotel)
hotels_in_single_city = []
soup = BeautifulSoup(requests.get(hotels_links_by_city[3]).text, features='html.parser')
all_hotels = soup.find_all("a",  "soom-name") # Extract all the hotel's in London City
for hotel in all_hotels:
    hotel_name = hotel.getText()
    href = "https://www.kayak.co.in" + str(hotel['href'])
    if not hotel_name:
        hotel_name = "Others Hotel"
    if href is not None:
        hotels_in_single_city.append(href)
        hotelId= find_hotel_id(href)
        hotel_name = hotel_name
        hotel_link = href
        #  insert city hotel information into databases
        sql = "INSERT INTO Single_City_Hotel_List (hotel_name, hotel_id, hrf_link) VALUES (%s, %s, %s)"
        val = (hotel_name, hotelId, hotel_link)
        cursor.execute(sql, val)
        mydb.commit()

# Third page operation and extract image of the hotel and store into database 
# hotel details and scrap images from hotel "London-Hotels-citizenM-Tower-of-London"
soup = BeautifulSoup(requests.get(hotels_in_single_city[2]).text, features='html.parser')
scripts = soup.find_all('script')
index = 1
for script in scripts:
    if script.attrs.get("type") == "application/ld+json": #This script holds all the image link, description
        contents = json.loads(script.contents[0])
        if "photo" in contents:
            for content in contents['photo']:
                if "contentUrl" in content:
                    hotel_id = find_hotel_id(hotels_in_single_city[2])
                    hotel_name = "London-Hotels-citizenM-Tower-of-London"
                    image_number = index
                    image_sourse =  content['contentUrl']
                    label =  content['description']
                    index = index + 1
                    sql = "INSERT INTO Hotel_With_Image_Details (hotel_id, hotel_name, image_link, label) VALUES (%s, %s, %s, %s)"
                    val = (hotel_id, hotel_name, image_sourse, label)
                    cursor.execute(sql, val)
                    mydb.commit()