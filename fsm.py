from transitions.extensions import GraphMachine
from linebot import LineBotApi, WebhookParser
import os
from requests_html import HTMLSession

from utils import send_text_message,send_button_message
from linebot.models import (
    MessageEvent,
    TextSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    MessageTemplateAction,
    CarouselTemplate, 
    CarouselColumn,
)
session = HTMLSession()
url = "https://www.youtube.com/results?search_query=台中景點"
response = session.get(url)
response.html.render(sleep=1, keep_page = True, scrolldown = 0)
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_choose_city_North(self, event):
        return event.message.text == "北部" 
    def is_going_to_choose_city_Middle(self, event):
        return event.message.text == "中部" 
    def is_going_to_choose_city_South(self, event):
        return event.message.text == "南部" 
    def is_going_to_choose_city_East(self, event):
        return event.message.text == "東部/離島" 
    def is_going_to_choose_area(self,event):
        return event.message.text == "返回"
    def is_going_to_Keelung_City(self,event):
        return event.message.text == "基隆市"
    def is_going_to_New_Taipei_City(self,event):
        return event.message.text == "新北市"
    def is_going_to_Taipei_City(self,event):
        return event.message.text == "台北市"
    def is_going_to_Taoyuan_City(self,event):
        return event.message.text == "桃園市"
    def is_going_to_Hsinchu(self,event):
        return event.message.text == "新竹縣/市"
    def is_going_to_Miaoli(self,event):
        return event.message.text == "苗栗縣/市"  
    def is_going_to_Taichung_City(self,event):
        return event.message.text == "台中市"
    def is_going_to_Changhua(self,event):
        return event.message.text == "彰化縣/市"  
    def is_going_to_Nantou(self,event):
        return event.message.text == "南投縣/市"      
    def is_going_to_Yunlin_County(self,event):
        return event.message.text == "雲林縣"
    def is_going_to_Chiayi(self,event):
        return event.message.text == "嘉義縣/市"    
    def is_going_to_Tainan_City(self,event):
        return event.message.text == "台南市"
    def is_going_to_Kaohsiung_City(self,event):
        return event.message.text == "高雄市"
    def is_going_to_Pingtung(self,event):
        return event.message.text == "屏東縣/市"
    def is_going_to_Yilan(self,event):
        return event.message.text == "宜蘭縣/市"      
    def is_going_to_Hualien(self,event):
        return event.message.text == "花蓮縣/市" 
    def is_going_to_Taitung(self,event):
        return event.message.text == "台東縣/市"     
    def is_going_to_Penghu_County(self,event):
        return event.message.text == "澎湖縣"
    def is_going_to_Green_Island(self,event):
        return event.message.text == "綠島"    
    def is_going_to_Orchid_Island(self,event):
        return event.message.text == "蘭嶼"   
    def is_going_to_Kinmen_County(self,event):
        return event.message.text == "金門"  
    def is_going_to_Matsu(self,event):
        return event.message.text == "馬祖"   

    
    def on_enter_choose_area(self,event):
        #send_text_message(event.reply_token,"rechoose city")
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
    def on_enter_choose_city_North(self, event):
        print("I'm entering choose_city_North")
        #self.turn_to_initial(event)
        channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
        line_bot_api = LineBotApi(channel_access_token)
        template_message = TemplateSendMessage(
            alt_text='carousel template',
            template = CarouselTemplate(
                columns=[
                    CarouselColumn(
                    title="基隆市",
                    text="查詢基隆市旅遊資訊",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text ='基隆市'
                        )
                    ]
                    ),
                    CarouselColumn(
                    title="新北市",
                    text="查詢新北市旅遊資訊",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text = '新北市'
                        )
                    ]
                    ),
                    CarouselColumn(
                    title="台北市",
                    text="查詢台北市旅遊資訊",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text = '台北市'
                        )
                    ]
                    ),
                    CarouselColumn(
                    title="桃園市",
                    text="查詢桃園市旅遊資訊",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text = '桃園市'
                        )
                    ]
                    ),
                    CarouselColumn(
                    title="新竹縣/市",
                    text="查詢新竹縣/市旅遊資訊",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text = '新竹縣/市'
                        )
                    ]
                    ),
                    CarouselColumn(
                    title="宜蘭縣/市",
                    text="查詢宜蘭縣/市旅遊資訊",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text = '宜蘭縣/市'
                        )
                    ]
                    ),
                    CarouselColumn(
                    title="重新選擇地區",
                    text="北、中、南、東、離島",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text = '返回'
                        )
                    ]
                    )
                ]
            )
        )         
        line_bot_api.reply_message(event.reply_token,template_message)
    def on_enter_choose_city_Middle(self, event):
        print("I'm entering choose_city_Middle")
        channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
        line_bot_api = LineBotApi(channel_access_token)
        template_message = TemplateSendMessage(
            alt_text='carousel template',
            template = CarouselTemplate(
                columns=[
                    CarouselColumn(
                    title="苗栗縣/市",
                    text="查詢苗栗縣/市旅遊資訊",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text ='苗栗縣/市'
                        )
                    ]
                    ),
                    CarouselColumn(
                    title="台中市",
                    text="查詢台中市旅遊資訊",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text = '台中市'
                        )
                    ]
                    ),
                    CarouselColumn(
                    title="彰化縣/市",
                    text="查詢彰化縣/市旅遊資訊",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text = '彰化縣/市'
                        )
                    ]
                    ),
                    CarouselColumn(
                    title="南投縣/市",
                    text="查詢南投縣/市旅遊資訊",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text = '南投縣/市'
                        )
                    ]
                    ),
                    CarouselColumn(
                    title="雲林縣",
                    text="查詢雲林縣旅遊資訊",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text = '雲林縣'
                        )
                    ]
                    ),
                    CarouselColumn(
                    title="重新選擇地區",
                    text="北、中、南、東、離島",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text = '返回'
                        )
                    ]
                    )
                ]
            )
        )         
        line_bot_api.reply_message(event.reply_token,template_message)
        send_text_message(event.reply_token,"your choose:"+event.message.text)
    def on_enter_choose_city_South(self, event):
        print("I'm entering choose_city_South")
        self.turn_to_initial(event)
        channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
        line_bot_api = LineBotApi(channel_access_token)
        template_message = TemplateSendMessage(
            alt_text='carousel template',
            template = CarouselTemplate(
                columns=[
                    CarouselColumn(
                    title="台南市",
                    text="查詢台南市旅遊資訊",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text ='台南市'
                        )
                    ]
                    ),
                    CarouselColumn(
                    title="高雄市",
                    text="查詢高雄市旅遊資訊",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text = '高雄市'
                        )
                    ]
                    ),
                    CarouselColumn(
                    title="屏東縣/市",
                    text="查詢屏東縣/市旅遊資訊",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text = '屏東縣/市'
                        )
                    ]
                    ),
                    CarouselColumn(
                    title="嘉義縣/市",
                    text="查詢嘉義縣/市旅遊資訊",
                    actions=[MessageTemplateAction(
                        label = '確認',
                        text = '嘉義縣/市'
                        )
                    ]
                    ),
                    CarouselColumn(
                    title="重新選擇地區",
                    text="北、中、南、東、離島",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text = '返回'
                        )
                    ]
                    )
                ]
            )
        )         
        line_bot_api.reply_message(event.reply_token,template_message)
        send_text_message(event.reply_token,"your choose:"+event.message.text)
    def on_enter_choose_city_East(self, event):
        print("I'm entering choose_city_East")
        channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
        line_bot_api = LineBotApi(channel_access_token)
        template_message = TemplateSendMessage(
            alt_text='carousel template',
            template = CarouselTemplate(
                columns=[
                    CarouselColumn(
                    title="花蓮縣/市",
                    text="查詢花蓮縣/市旅遊資訊",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text ='花蓮縣/市'
                        )
                    ]
                    ),
                    CarouselColumn(
                    title="台東縣/市",
                    text="查詢台東縣/市旅遊資訊",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text = '台東縣/市'
                        )
                    ]
                    ),
                    CarouselColumn(
                    title="澎湖縣",
                    text="查詢澎湖縣旅遊資訊",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text = '澎湖縣'
                        )
                    ]
                    ),
                    CarouselColumn(
                    title="綠島",
                    text="查詢綠島旅遊資訊",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text = '綠島'
                        )
                    ]
                    ),
                    CarouselColumn(
                    title="蘭嶼",
                    text="查詢蘭嶼旅遊資訊",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text = '蘭嶼'
                        )
                    ]
                    ),
                    CarouselColumn(
                    title="金門",
                    text="查詢金門旅遊資訊",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text = '金門'
                        )
                    ]
                    ),
                    CarouselColumn(
                    title="馬祖",
                    text="查詢馬祖旅遊資訊",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text = '馬祖'
                        )
                    ]
                    ),
                    CarouselColumn(
                    title="重新選擇地區",
                    text="北、中、南、東、離島",
                    actions=[
                        MessageTemplateAction(
                        label = '確認',
                        text = '返回'
                        )
                    ]
                    )
                ]
            )
        )         
        line_bot_api.reply_message(event.reply_token,template_message)
        send_text_message(event.reply_token,"your choose:"+event.message.text)

    def on_enter_Keelung_City(self,event):
        send_text_message(event.reply_token,"輸入“返回”可回到地區選單\n旅遊資訊:"+event.message.text)
    def on_enter_New_Taipei_City(self,event):
        send_text_message(event.reply_token,"輸入“返回”可回到地區選單\n旅遊資訊:"+event.message.text)
    def on_enter_Taipei_City(self,event):
        send_text_message(event.reply_token,"輸入“返回”可回到地區選單\n旅遊資訊:"+event.message.text)
    def on_enter_Taoyuan_City(self,event):
        send_text_message(event.reply_token,"輸入“返回”可回到地區選單\n旅遊資訊:"+event.message.text)
    def on_enter_Hsinchu(self,event):
        send_text_message(event.reply_token,"輸入“返回”可回到地區選單\n旅遊資訊:"+event.message.text)
    def on_enter_Miaoli(self,event):
        send_text_message(event.reply_token,"輸入“返回”可回到地區選單\n旅遊資訊:"+event.message.text)
    def on_enter_Taichung_City(self,event):
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
        print(res)
        send_text_message(event.reply_token,res)
    def on_enter_Changhua(self,event):
        send_text_message(event.reply_token,"輸入“返回”可回到地區選單\n旅遊資訊:"+event.message.text) 
    def on_enter_Nantou(self,event):
        send_text_message(event.reply_token,"輸入“返回”可回到地區選單\n旅遊資訊:"+event.message.text)    
    def on_enter_Yunlin_County(self,event):
        send_text_message(event.reply_token,"輸入“返回”可回到地區選單\n旅遊資訊:"+event.message.text)
    def on_enter_Chiayi(self,event):
        send_text_message(event.reply_token,"輸入“返回”可回到地區選單\n旅遊資訊:"+event.message.text)
    def on_enter_Tainan_City(self,event):
        send_text_message(event.reply_token,"輸入“返回”可回到地區選單\n旅遊資訊:"+event.message.text)
    def on_enter_Kaohsiung_City(self,event):
        send_text_message(event.reply_token,"輸入“返回”可回到地區選單\n旅遊資訊:"+event.message.text)
    def on_enter_Pingtung(self,event):
        send_text_message(event.reply_token,"輸入“返回”可回到地區選單\n旅遊資訊:"+event.message.text)
    def on_enter_Yilan(self,event):
        send_text_message(event.reply_token,"輸入“返回”可回到地區選單\n旅遊資訊:"+event.message.text)
    def on_enter_Hualien(self,event):
        send_text_message(event.reply_token,"輸入“返回”可回到地區選單\n旅遊資訊:"+event.message.text) 
    def on_enter_Taitung(self,event):
        send_text_message(event.reply_token,"輸入“返回”可回到地區選單\n旅遊資訊:"+event.message.text)  
    def on_enter_Penghu_County(self,event):
        send_text_message(event.reply_token,"輸入“返回”可回到地區選單\n旅遊資訊:"+event.message.text)
    def on_enter_Green_Island(self,event):
        send_text_message(event.reply_token,"輸入“返回”可回到地區選單\n旅遊資訊:"+event.message.text)   
    def on_enter_Orchid_Island(self,event):
        send_text_message(event.reply_token,"輸入“返回”可回到地區選單\n旅遊資訊:"+event.message.text) 
    def on_enter_Kinmen_County(self,event):
        send_text_message(event.reply_token,"輸入“返回”可回到地區選單\n旅遊資訊:"+event.message.text) 
    def on_enter_Matsu(self,event):
        send_text_message(event.reply_token,"輸入“返回”可回到地區選單\n旅遊資訊:"+event.message.text)
    