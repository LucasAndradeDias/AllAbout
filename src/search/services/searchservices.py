import os, urllib3,urllib.request
from bs4 import BeautifulSoup


class service_web_scraping():
    
    def get_html_title(self,html_content:str):

        soap = BeautifulSoup(html_content,"html.parser")



        divs = soap.find

        print(divs)

        return divs



    def download_page(self,term):


        urls = self.get_pages_to_search(term=term)

        http = urllib3.PoolManager(num_pools=len(urls))

        html_titles = {}


        for url in urls:

            #request = http.request("GET",url=url)
            urllib.request.urlretrieve(url=url,filename="t.html")

            # divs = self.get_html_title(request.data)




            # html_titles[url] = title

        
        return html_titles


    def get_pages_to_search(self,term:str):
        urls = {
            "https://www.reddit.com/search/?q="+term+"&t=week&sort=top",
        }
        return urls

