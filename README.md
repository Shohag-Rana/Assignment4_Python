
# Web Scraping Python Project

In this web scraping project we use python beautifulsoup package. we scrap data from the https://www.kayak.co.in/?ispredir=true this site. we scrap data from this site categories with city hotel and save into data base table all_city_hotel. then choose one city hotel from all_city_hotel and extract all the link of hotel and save into database single_city_hotel table. then choose one hotel from single_city_hotel and scrap all the image and save into database.


## Technology and Tools

 - Programming Language: Python
 - Database: MySQL


## Author

- [Shohag Rana](https://github.com/Shohag-Rana)


## Installation

 - mkdir my-project
 - cd my-project
 - pip install beautifulsoup4
 - pip install requests
 - python -m pip install mysql-connector-python 
 - Phpmyadmin localhost
 
 ## SQL Queries

 - import mysql.connector
 - mydb = mysql.connector.connect(host="localhost",user="root",password="root123456")
 - mycursor = mydb.cursor()
 - cursor.execute("CREATE DATABASE kayakHotelDB") 
 - cursor.execute("CREATE TABLE Hotels_All_City (city_name VARCHAR(255), city_hotel_id VARCHAR(255), hrf_link VARCHAR(255))")
 - cursor.execute("CREATE TABLE Single_City_Hotel_List (hotel_name VARCHAR(255), hotel_id VARCHAR(255), hrf_link VARCHAR(255))")
 - cursor.execute("CREATE TABLE Hotel_With_Image_Details (hotel_id VARCHAR(255), hotel_name VARCHAR(255), image_link VARCHAR(255), label VARCHAR(255))")


## Github Deployment Command

create a new repository on the command line

```bash
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Shohag-Rana/Assignment4_Python.git
git push -u origin main
```
push an existing repository from the command line

```bash
git remote add origin https://github.com/Shohag-Rana/Assignment4_Python.git
git branch -M main
git push -u origin main
```

## Feature of this Project

- Scrap the data from given site and store it into data
- Scrap the image from the javascript json file

## Conculation
 - In this web scraping project we use python programming language and it's packages beautifulsoup4, requests and MySQL databases. the image data extract from the javascript json file. Hope that all is ok.


