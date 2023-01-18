#### import local libs
from .service_for_news import service_for_news


from .service_for_forum import service_for_forum

from .tools import tools


class service_control():
    def __init__(self) -> None:
        self.forums_service = service_for_forum()
        self.news_service = service_for_news()

    def search_forum_term(self,term:str):
        
        posts_array = []

        ## get reddit data
        try:
            url = self.forums_service.forums_search_pages("reddit",term=term)

            html_text = tools().get_html_as_text(url)

            self.forums_service.reddit_scraping(html_content=html_text,num_posts=4,posts_array=posts_array)


        except ValueError as error:

            print(error)
            
            return error

        else:
            return posts_array

    def search_news_term(self,term:str):

        """
        RETURNS AN ARRAY WITH ALL NEWS FOUND DATA 
        """
        news_data = []

        try:
            # site infos
            news_search_page = self.news_service.news_search_pages(term)

            for site in news_search_page:
                

                # get site html

                site_html =  tools().get_html_as_text(news_search_page[site]["url"])

                # #calling html scraping

                news_service_class = globals()["service_for_news"]()

                scraping_func = getattr(news_service_class,news_search_page[site]["func_name"])

                scraping_func(html_content=site_html,news_array=news_data)

        except TypeError as error:

            return error
        
        else:
        
            return news_data



