import google.generativeai as client

import os
import httpx
from typing import List

class Choice():
    def __init__(self, str: str | None = None):
        self.message = str
        
class Response():
    def __init__(self, response_str: str | None = None):
        self.choice = [Choice(response_str)]

class Completions():
    def __init__(self):
        pass
    def create(self,
        messages: str | None = None,
        model: str | None = None):
        content = messages[0]['content']
        model = self.client.GenerativeModel(model_name=self.model)
        response = model.generate_content(contents=content)
        # fix response
        resp_text = response.text.replace('```json\n', '').replace('```', '')

        return Response()

class GeminiChat():
    def __init__(self):
        pass
    def completions(self) -> Completions:
        return Completions(self._client)

class OpenAI():
    def __init__(self, 
                model: str | None = None,
                http_client: httpx.Client | None = None,
                api_key: str | None = None,
                base_url: str | httpx.URL | None = None,
        ):
        super().__init__()
        # Initialize the Google Generative AI chat model
        client.configure(api_key=os.environ.get('GEMINI_API_KEY')) 
        self.model = model
        self.chat = client.Chat()

    