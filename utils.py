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
            thumbnailImageUrl='https://cdn.xxl.thumbs.canstockphoto.com.tw/%E5%BB%BA%E7%AF%89%E7%89%A9-%E5%9C%B0%E5%9C%96-%E5%82%B3%E7%B5%B1-%E4%BA%9E%E6%B4%B2%E4%BA%BA-%E5%8F%B0%E7%81%A3-%E5%8D%A1%E9%80%9A-%E7%BE%8E%E5%B7%A5%E5%90%91%E9%87%8F_csp50402860.jpg'
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
