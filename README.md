# Real Estate Listings Web Scraper

I developed this program to web-scrape real estate websites and provide the user with up-to-date listing information based on user-entered parameters. The user can select the website to search (three options are currently available), enter the city, the type of property, and the minimum and maximum price to search for. The program will then browse the chosen web page, get information for each listing such as price, address, and description (it varies from site to site), and send all this data to a text file. A screenshot of the search results is taken as well. 

The code was written in Python along with Selenium. In this project, I used the prototype design pattern to create scrapers that slightly differ per website. I also used the facade design pattern to hide complexity and simplify the main function of the program.

## Class Diagram:
![alt text](UMLDiagram.png)
