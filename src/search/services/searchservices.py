import os, urllib3,urllib.request
from bs4 import BeautifulSoup




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


        print(post_subbreddit)
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
        
    def get_all_forums_data(self,term:str):
        
        data = {}

        ## get reddit data
        try:
            url = self.forums_search_pages("reddit",term=term)

            html_text = self.get_html_as_text(url)

            reddit_data = self.reddit_scraping(html_content=html_text,num_posts=4)

            data["reddit"] = reddit_data 
            

        except ValueError:

            print(ValueError)
            
            return ValueError

        else:
            return data

            





