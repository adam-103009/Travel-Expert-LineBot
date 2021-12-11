import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message,send_button_message
from linebot.models import (
    MessageEvent,
    TextSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    MessageTemplateAction
)

load_dotenv()


machine = TocMachine(
    states=["choose_area", "choose_city_North","choose_city_East","choose_city_South","choose_city_Middle","Keelung_City","New_Taipei_City","Taipei_City","Taoyuan_City",
            "Hsinchu","Miaoli","Taichung_City","Changhua","Nantou","Yunlin_County","Chiayi","Tainan_City","Kaohsiung_City","Pingtung","Yilan","Hualien",
            "Taitung","Penghu_County","Green_Island","Orchid_Island","Kinmen_County","Matsu"],
    transitions=[
        {
            "trigger": "advance",
            "source": "choose_area",
            "dest": "choose_city_North",
            "conditions": "is_going_to_choose_city_North",
        },
        {
            "trigger": "advance",
            "source": "choose_area",
            "dest": "choose_city_Middle",
            "conditions": "is_going_to_choose_city_Middle",
        },
        {
            "trigger": "advance",
            "source": "choose_area",
            "dest": "choose_city_South",
            "conditions": "is_going_to_choose_city_South",
        },
        {
            "trigger": "advance",
            "source": "choose_area",
            "dest": "choose_city_East",
            "conditions": "is_going_to_choose_city_East",
        },
        {
            "trigger": "advance",
            "source": "choose_city_North",
            "dest": "Keelung_City",
            "conditions": "is_going_to_Keelung_City",
        },
        {
            "trigger": "advance",
            "source": "choose_city_North",
            "dest": "New_Taipei_City",
            "conditions": "is_going_to_New_Taipei_City",
        },
        {
            "trigger": "advance",
            "source": "choose_city_North",
            "dest": "Taipei_City",
            "conditions": "is_going_to_Taipei_City",
        },
        {
            "trigger": "advance",
            "source": "choose_city_North",
            "dest": "Taoyuan_City",
            "conditions": "is_going_to_Taoyuan_City",
        },
        {
            "trigger": "advance",
            "source": "choose_city_North",
            "dest": "Hsinchu",
            "conditions": "is_going_to_Hsinchu",
        },
        {
            "trigger": "advance",
            "source": "choose_city_Middle",
            "dest": "Miaoli",
            "conditions": "is_going_to_Miaoli",
        },
        {
            "trigger": "advance",
            "source": "choose_city_Middle",
            "dest": "Taichung_City",
            "conditions": "is_going_to_Taichung_City",
        },
        {
            "trigger": "advance",
            "source": "choose_city_Middle",
            "dest": "Changhua",
            "conditions": "is_going_to_Changhua",
        },
        {
            "trigger": "advance",
            "source": "choose_city_Middle",
            "dest": "Nantou",
            "conditions": "is_going_to_Nantou",
        },
        {
            "trigger": "advance",
            "source": "choose_city_Middle",
            "dest": "Yunlin_County",
            "conditions": "is_going_to_Yunlin_County",
        },
        {
            "trigger": "advance",
            "source": "choose_city_South",
            "dest": "Chiayi",
            "conditions": "is_going_to_Chiayi",
        },
        {
            "trigger": "advance",
            "source": "choose_city_South",
            "dest": "Tainan_City",
            "conditions": "is_going_to_Tainan_City",
        },
        {
            "trigger": "advance",
            "source": "choose_city_South",
            "dest": "Kaohsiung_City",
            "conditions": "is_going_to_Kaohsiung_City",
        },
        {
            "trigger": "advance",
            "source": "choose_city_South",
            "dest": "Pingtung",
            "conditions": "is_going_to_Pingtung",
        },
        {
            "trigger": "advance",
            "source": "choose_city_North",
            "dest": "Yilan",
            "conditions": "is_going_to_Yilan",
        },
        {
            "trigger": "advance",
            "source": "choose_city_East",
            "dest": "Hualien",
            "conditions": "is_going_to_Hualien",
        },
        {
            "trigger": "advance",
            "source": "choose_city_East",
            "dest": "Taitung",
            "conditions": "is_going_to_Taitung",
        },
        {
            "trigger": "advance",
            "source": "choose_city_East",
            "dest": "Penghu_County",
            "conditions": "is_going_to_Penghu_County",
        },
        {
            "trigger": "advance",
            "source": "choose_city_East",
            "dest": "Green_Island",
            "conditions": "is_going_to_Green_Island",
        },
        {
            "trigger": "advance",
            "source": "choose_city_East",
            "dest": "Orchid_Island",
            "conditions": "is_going_to_Orchid_Island",
        },
        {
            "trigger": "advance",
            "source": "choose_city_East",
            "dest": "Kinmen_County",
            "conditions": "is_going_to_Kinmen_County",
        },
        {
            "trigger": "advance",
            "source": "choose_city_East",
            "dest": "Matsu",
            "conditions": "is_going_to_Matsu",
        },
        {"trigger": "advance",
         "source": ["choose_city_North","choose_city_East","choose_city_South","choose_city_Middle"], 
         "dest": "choose_area",
         "conditions": "is_going_to_choose_area"
        }
        
    ],
    initial="choose_area",
    auto_transitions=False,
    show_conditions=True,
)

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


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

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

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


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
        print("\nFSM STATE:"+machine.state)
        print("REQUEST BODY: \n"+body)
        response = machine.advance(event)
        if response == False:
            if machine.state=="choose_area":
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

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
