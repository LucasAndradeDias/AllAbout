import urllib3


class tools():
    def __init__(self) -> None:
        pass


    def get_html_as_text(self,url:str):
        try:
            http = urllib3.PoolManager()

            request = http.request("GET",url)

            if request.status != 200:
                raise TypeError(f" Request to url '{url}' failed with status code: {request.status}")
            
            html_text = request.data

            return html_text
        
        except TypeError as error:

            raise error

