from bs4 import BeautifulSoup

from datetime import datetime




class service_for_news():
    def __init__(self) -> None:
        pass

    def scraping_cnn_brasil(self,html_content:str,news_array:list,news_number=30,):
        try:
        
            soup = BeautifulSoup(html_content,"html.parser")

            ul_list = soup.find_all("li",{"class":"home__list__item"})

            counter = 0

            max_news = len(ul_list) if news_number > len(ul_list) else news_number

            #getting a num of news from list
            while ( counter < max_news):

                news_title = ul_list[counter].h3.contents[0]
                news_url =ul_list[counter].a.get("href")
                news_date_str = ul_list[counter].span.text
                news_pic = ul_list[counter].img.get("src")

                date_time = datetime.strptime(news_date_str, ' %d/%m/%Y às %H:%M ').timestamp()
                
                news_content = {"title":news_title,"timestamp":date_time,"url":news_url,"pic_url":news_pic,"date":news_date_str,"source":"Cnn Brasil","Type":"news"}

                news_array.append(news_content)
                
                counter+=1

        except TypeError as error:

            return error


    def news_search_pages(self,term:str,site=""):
        urls={
            "cnn_brasil":{"url":"https://www.cnnbrasil.com.br/?s="+term+"&orderby=date&order=desc","func_name":"scraping_cnn_brasil"},
        }

        if site == "":
            return urls
        
        else:
            return urls[site]

