"""
author: alexixu 
created at: 2023/4/12
"""

import os

import openai
from tornado.escape import json_decode
from tornado.web import RequestHandler

openai.api_key = os.getenv("OPENAI_API_KEY")


class DALL2_Handler(RequestHandler):
    def post(self):
        json_obj = json_decode(self.request.body)

        prompt = json_obj["prompt"]
        height = json_obj.get("height", 1024)
        width = json_obj.get("width", 1024)

        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size=f"{height}x{width}"
        )

        image_url = response['data'][0]['url']

        return image_url
