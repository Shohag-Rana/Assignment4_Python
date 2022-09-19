
# Web Scraping Python Project

In this web scraping project we use python beautifulsoup package. we scrap data from the https://www.kayak.co.in/?ispredir=true this site. we scrap data from this site categories with city hotel and save into data base table all_city_hotel. then choose one hotel and extract all the link of hote and save into database single_city_hotel table. then choose one hotel from this second page and scrap all the image and save into database.


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




