import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)

        return response.content

    def load_json(self):
        results = self.get_response_body()
        results_json = json.loads(results)
        
        return results_json