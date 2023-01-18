from bs4 import BeautifulSoup

from datetime import datetime, timedelta



class service_for_forum():
    def __init__(self):
        self.available_forums = {"reddit":self.reddit_scraping}
    
    def reddit_scraping(self,html_content:str,posts_array:list,num_posts=5):

        soup = BeautifulSoup(html_content,"html.parser")
        
        numbers = soup.find_all("span",{"class":"_vaFo96phV6L5Hltvwcox"})

        title = soup.find_all("h3",{"class":"_eYtD2XCVieq6emjKBH3m"})

        post_link = soup.find_all("a",{"class":"SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE"})

        post_dt = soup.find_all("span",{"data-testid":"post_timestamp"})


        counter = 0

        counter_votes = 0

        
        while (counter < num_posts-1):
            post_time = post_dt[counter].text

            post_title = title[counter].contents[0]

            post_votes = numbers[counter_votes].contents[0]

            post_url = "NO DATA"

            #post_url = "https://www.reddit.com/"+post_link[counter].get("href")
            post_url = None
            post_timestamp = None

            day = int("".join(s for s in post_time if s.isdigit()))

            timestamp_ago = timedelta(days=day,microseconds=0)

            aa = datetime.now() - timestamp_ago
            
            #2023-01-13 23:23:57.177675

            date_time = datetime.strptime(str(aa), '%Y-%m-%d %H:%M:%S.%f').timestamp()


            # return data
            post_data = {"title":post_title,"url":post_url,"votes":post_votes,"date":post_time,"timestamp":date_time,"type":"Forum"}

            posts_array.append(post_data)

            counter+=1       
            counter_votes+=3



    def forums_search_pages(self,forum,term:str):
        urls = {
            "reddit":"https://www.reddit.com/search/?q="+term+"&t=week&sort=top",
        }
        return urls[forum]


