import google.generativeai as client

import os
import httpx
from typing import List

class BadRequestError(Exception):
    pass

class OpenAIError(Exception):
    pass

class Content():
    def __init__(self, content: str | None = None):
        self.content = content

class Choice():
    def __init__(self, str: str | None = None):
        self.message = Content(str)

class Response():
    def __init__(self, response_str: str | None = None):
        self.choices = [Choice(response_str)]

class Completions():
    def create(self,
        messages,
        model: str | None = None) -> Response:
        try:
            content = messages[0]['content']
            print(f"Content: {content}")
            model = client.GenerativeModel(model_name="gemini-1.5-flash")
            response = model.generate_content(contents=content)
           
            # fix response
            resp_text = response.text.replace('```json\n', '').replace('```', '')
            print(f"Response: {response}")
            return Response(resp_text)
        except Exception as e:
            raise BadRequestError(f"Error: {e}")

class GeminiChat():
    def __init__(self,model: str | None = None):
        self.completions = Completions()

class OpenAI():
    def __init__(self, 
                model: str | None = None,
                http_client: httpx.Client | None = None,
                api_key: str | None = None,
                base_url: str | httpx.URL | None = None,
        ):
        # Initialize the Google Generative AI chat model
        self.isWrapper = True
        client.configure(api_key=os.environ.get('GEMINI_API_KEY')) 
        self.chat = GeminiChat(self)

