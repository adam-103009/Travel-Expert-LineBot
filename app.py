import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from machine import create_machine

from fsm import TocMachine
from utils import send_image_message, send_text_message,send_button_message
from linebot.models import (
    MessageEvent,
    TextSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    MessageTemplateAction
)

load_dotenv()
machines = {}



app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body:"+body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        if event.source.user_id not in machines:
            machines[event.source.user_id] = create_machine()
        response = machines[event.source.user_id].advance(event)
        if response == False:
            if event.message.text.lower()=='fsm':
                send_image_message(event.reply_token,'https://travel-expert-libebot.herokuapp.com/show-fsm')
            if machines[event.source.user_id].state=="choose_area":
                title="選擇你想查詢的地區"
                text="北、中、南、東"
                btn = [
                    MessageTemplateAction(
                        label = '北部',
                        text ='北部'
                    ),
                    MessageTemplateAction(
                        label = '中部',
                        text = '中部'
                    ),
                    MessageTemplateAction(
                        label = '南部',
                        text = '南部'
                    ),
                    MessageTemplateAction(
                        label = '東部/離島',
                        text = '東部/離島'
                    ),
                ]
                send_button_message(event.reply_token, title, text, btn)
            elif (machines[event.source.user_id].state=="choose_city_North" or machines[event.source.user_id].state=="choose_city_East" or 
                machines[event.source.user_id].state=="choose_city_Middle"or machines[event.source.user_id].state=="choose_city_South"):
                send_text_message(event.reply_token,"請選擇想要查詢的城市\n或者輸入想查詢的城市名稱\n輸入「返回」可回到地區選擇選單")



    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
