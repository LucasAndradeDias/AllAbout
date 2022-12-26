import os, urllib3
from bs4 import BeautifulSoup


class service_web_scraping():
    
    def get_html_title(self,html_content:str):

        soap = BeautifulSoup(html_content,"html.parser")

        return soap.title



    def download_page(self,term):


        urls = self.get_pages_to_search(term=term)

        http = urllib3.PoolManager(num_pools=len(urls))

        html_titles = {}


        for url in urls:

            request = http.request("GET",url=url)

            title = self.get_html_title(request.data)

            html_titles[url] = title

        
        return html_titles


    def get_pages_to_search(self,term:str):
        urls = {
            "https://news.google.com/search?q="+term+"&hl=pt-BR&gl=BR&ceid=BR%3Apt-419",
            "https://www.reddit.com/search/?q="+term
        }
        return urls

