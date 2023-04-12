"""
author: alexixu 
created at: 2023/4/12
"""

import asyncio

import tornado.web

from alex_nlp.serving.text2img_handler import DALL2_Handler


class DemoHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, Alex NLP")


def make_app():
    return tornado.web.Application([
        (r"/demo", DemoHandler),
        (r"/dall", DALL2_Handler)
    ])


async def main():
    app = make_app()
    app.listen(8000)
    await asyncio.Event().wait()


if __name__ == "__main__":
    print("start server")
    asyncio.run(main())
