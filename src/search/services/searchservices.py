import os

class service_web_scraping():
    

    def download_page(url):
        os.system(f'start cmd /c "curl www.google.com"')
        return True


    def set_pages_to_search(term:str):
        urls = {
            "https://www.globo.com/busca/?q="+term+"&order=relevant&species=not%C3%ADcias",
            "https://news.google.com/search?q="+term+"&hl=pt-BR&gl=BR&ceid=BR%3Apt-419"
        }