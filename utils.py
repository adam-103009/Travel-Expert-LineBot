import os
from linebot import LineBotApi, WebhookParser
from linebot.models import (
    MessageEvent,
    TextSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    MessageTemplateAction,
    CarouselTemplate,
    CarouselColumn,
    ImageSendMessage
)
import requests
from bs4 import BeautifulSoup
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_button_message(reply_token, title, text, btn):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='button template',
        template = ButtonsTemplate(
            title = title,
            text = text,
            actions = btn,
            thumbnail_image_url="https://lh3.googleusercontent.com/proxy/cbC-pT9oRgfisa75Z_JA3FOBwzxrEJEMt1ElrtQD4LXSNaePPyjRAjyIjAQoKt0Laalke0kjUySo_kwloJyy1aap3cLcrZL9lUUbRTnf6C5f6b61LL5FTl8ZS5NLZI8aBg"
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"
def send_carousel_button_message(reply_token, title, text, btn):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='carousel template',
        template = CarouselTemplate(
            column=[
                CarouselColumn(
                title=title,
                text=text,
                actions=btn
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"
def send_image_message(reply_token, url):
    line_bot_api = LineBotApi(channel_access_token)
    message = ImageSendMessage(
        original_content_url = url,
        preview_image_url = url
    )
    line_bot_api.reply_message(reply_token, message)
def get_url(url):
    res="輸入“返回”可回到地區選單\n\n旅遊資訊\n"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("h3", itemprop="headline")
    for title in titles:
        res=res+title.select_one("a").getText()+'\n'+title.select_one("a").get("href")+'\n\n'
    return res
"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
