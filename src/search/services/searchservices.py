import os, urllib3,urllib.request
from bs4 import BeautifulSoup



class service_for_news():

    def scraping_cnn_brasil(self,html_content:str,news_number=30):
        
        soup = BeautifulSoup(html_content,"html.parser")


        ul_list = soup.find_all("li",{"class":"home__list__item"})

        news = []

        counter = 0

        max_news = len(ul_list) if news_number > len(ul_list) else news_number

        #getting a num of news from list
        while ( counter < max_news):

            news_title = ul_list[counter].h3.contents[0]
            news_url =ul_list[counter].a.get("href")
            news_date = ul_list[counter].span.text
            news_pic = ul_list[counter].img.get("src")

            news_content = {"title":news_title,"date":news_date,"url":news_url,"pic_url":news_pic}

            news.append(news_content)
            
            counter+=1


        return news


    def scraping_g1(self,html_content:str,news_number=30):
        soup = BeautifulSoup(html_content,"html.parser")

        ul_list = soup.find_all("li",{"class":"widget widget--card widget--info"})

        news = []

        counter = 0

        max_news = len(ul_list) if news_number > len(ul_list) else news_number

        #getting a num of news from list
        
        while ( counter < max_news):
            trash_words = {"videos"}

            for i in ul_list[counter].a:
                print(i)

            counter+=1





    def news_search_pages(self,term:str,site=""):
        urls={
            "cnn_brasil":{"url":"https://www.cnnbrasil.com.br/?s="+term+"&orderby=date&order=desc","func_name":"scraping_cnn_brasil"},
            "g1":{"url":"https://g1.globo.com/busca/?q="+term+"&order=recent&from=now-1w","func_name":"scraping_g1"}
        }

        if site == "":
            return urls
        
        else:
            return urls[site]


class service_for_forums():
    def __init__(self):
        self.available_forums = {"reddit":self.reddit_scraping}
    
    def reddit_scraping(self,html_content:str,num_posts=5):

        soup = BeautifulSoup(html_content,"html.parser")
        
        numbers = soup.find_all("span",{"class":"_vaFo96phV6L5Hltvwcox"})

        title = soup.find_all("h3",{"class":"_eYtD2XCVieq6emjKBH3m"})

        post_link = soup.find_all("a",{"class":"SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE"})

        post_dt = soup.find_all("span",{"data-testid":"post_timestamp"})

        post_subbreddit = soup.find_all(class_="_2mHuuvyV9doV3zwbZPtIPG _3Wz607wX-KXslTUjYvTZWi _3Wz607wX-KXslTUjYvTZWi")


        posts = []

        counter = 0

        counter_votes = 0

        while (counter < num_posts-1):
            
            post_time = post_dt[counter].text

            post_title = title[counter].contents[0]

            post_votes = numbers[counter_votes].contents[0]

            post_url = "https://www.reddit.com/"+post_link[counter].get("href") 

            post_data = {"title":post_title,"url":post_url,"votes":post_votes,"post_data":post_time}

            posts.append(post_data)

            counter+=1       
            counter_votes+=3


        return posts

    def forums_search_pages(self,forum,term:str):
        urls = {
            "reddit":"https://www.reddit.com/search/?q="+term+"&t=week&sort=top",
        }
        return urls[forum]



class service_control():
    def __init__(self) -> None:
        self.forums_service = service_for_forums()
        self.news_service = service_for_news()

    def get_all_forums_data_term(self,term:str):
        
        data = {}

        ## get reddit data
        try:
            url = self.forums_service.forums_search_pages("reddit",term=term)

            html_text = self.get_html_as_text(url)

            reddit_data = self.forums_service.reddit_scraping(html_content=html_text,num_posts=4)

            data["reddit"] = reddit_data 
            

        except ValueError:

            print(ValueError)
            
            return ValueError

        else:
            return data

    def get_html_as_text(self,url:str):
        try:
            http = urllib3.PoolManager()

            request = http.request("GET",url)

            if request.status != 200:
                raise TypeError(f" REQUEST FAILED WITH STATUS CODE: {request.status}")
            
            html_text = request.data
    
            return html_text
        
        except TypeError as error:
            print(error)
            return error

    def get_news_from_site_term(self,term:str):

        """
        RETURNS AN ARRAY WITH ALL NEWS FOUND DATA 
        """
        news_data = []

        # site infos
        news_search_page = self.news_service.news_search_pages(term)

        for site in news_search_page:
            
            all_site_news = []

            # get site html

            site_html = self.get_html_as_text(news_search_page[site]["url"])

            # #calling html scraping

            news_service_class = globals()["service_for_news"]()

            scraping_func = getattr(news_service_class,news_search_page[site]["func_name"])

            data = scraping_func(html_content=site_html)

            all_site_news.append(data)

            dic = {site:all_site_news}


            news_data.append(dic)

        
        return news_data



