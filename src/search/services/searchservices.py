import os, urllib3,urllib.request
from bs4 import BeautifulSoup




class service_web_scraping():
    
    def get_reddit_scraping(self,html_content:str):

        soap = BeautifulSoup(html_content,"html.parser")

        divs = soap.find_all(class_="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE")

        posts = {"reddit_posts":{}}



        for div in divs:
            posts["reddit_posts"][div.h3.contents[0]] = {"url": "https://www.reddit.com"+div.get("href")}


        with open("reddit.html","w",encoding='utf-8') as file:

            file.write(str(divs))

        return posts



    def control_scraping(self,term):


        urls = self.get_pages_to_search(term=term)

        http = urllib3.PoolManager(num_pools=len(urls))

        html_titles = {}

        for url in urls:

            request = http.request("GET",url=url)

            divs = self.get_reddit_scraping(request.data)

            html_titles = divs

        
        return html_titles


    def get_pages_to_search(self,term:str):
        urls = {
            "https://www.reddit.com/search/?q="+term+"&t=week&sort=top",
        }
        return urls

