import os
from requests_html import HTMLSession
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
            actions = btn
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
def get_url():
    session = HTMLSession()
    url = "https://www.youtube.com/results?search_query=台中景點"
    response = session.get(url)
    response.html.render(sleep=1, keep_page = True, scrolldown = 0)
    res="輸入“返回”可回到地區選單\n旅遊資訊"
    c=5
    link=[]
    for links in response.html.find('a#video-title'):
        if c==0:
            break
        c-=1
        link.append(next(iter(links.absolute_links)))
    for i in range(len(link)):
        res=res+link[i]+'\n'
    return res
"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
