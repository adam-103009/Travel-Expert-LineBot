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
            thumbnailImageUrl="https://cdn.hk01.com/di/media/images/2889837/org/4ef07fed4a8836f3ed6df68bbfc7d0c9.jpg/nAAal3F-2QSZICGJCFefX31f_bD3NTZhM-WgQjPloEI?v=w1920"
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
    res="輸入“返回”可回到地區選單\n旅遊資訊\n"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("h3", itemprop="headline")
    for title in titles:
        res='\n'+res+title.select_one("a").getText()+'\n'+title.select_one("a").get("href")+'\n'
    return res
"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
