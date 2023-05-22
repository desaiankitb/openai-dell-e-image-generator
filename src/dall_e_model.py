import requests
from PIL import Image
import openai

class DallEModel:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_image(self, keywords):
        prompt = 'Generate an image for representing the following keywords togather: ' + ', '.join(keywords)
        # prompt = "Generate a thumbnail for the instagram reel talking about chatGPT and DALL-E-2"
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
            # size="16:9"
        )
        image_url = response['data'][0]['url']

        image = Image.open(requests.get(image_url, stream=True).raw)
        return image