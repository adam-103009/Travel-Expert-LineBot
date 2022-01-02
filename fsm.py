from transitions.extensions import GraphMachine
from linebot import LineBotApi, WebhookParser
import os

from utils import get_url, send_text_message,send_button_message
from linebot.models import (
    MessageEvent,
    TextSendMessage,
    TemplateSendMessage,
    ButtonsTemplate,
    MessageTemplateAction,
    CarouselTemplate, 
    CarouselColumn,
    ImageCarouselTemplate,
    PostbackTemplateAction,
    ImageCarouselColumn
)
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
        title="選擇你想查詢的地區或輸入Fsm將顯示Fsm圖"
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
            template = ImageCarouselTemplate(
                 columns=[
                    ImageCarouselColumn(
                        image_url='https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2021/12/05/realtime/14696448.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=800&exp=3600',
                        action=PostbackTemplateAction(
                            label='基隆市',
                            text='基隆市',
                            data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://img.ltn.com.tw/Upload/news/600/2020/12/30/3397139_1_1.jpg',
                        action=PostbackTemplateAction(
                            label='新北市',
                            text = '新北市',
                            data='action=buy&itemid=2'
                        )
                    ),
                    ImageCarouselColumn(
                    image_url='https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2016/10/19/99/2734166.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=800&exp=3600',
                    action=PostbackTemplateAction(
                        label = '台北市',
                        text = '台北市',
                        data='action=buy&itemid=3'
                        )
                    ),
                    ImageCarouselColumn(
                    image_url='https://www.taiwan.net.tw/pic.ashx?qp=1/big_scenic_spots/pic_A12-00161_11.jpg&sizetype=3',
                    action=PostbackTemplateAction(
                        label = '桃園市',
                        text = '桃園市',
                        data='action=buy&itemid=4'
                        )
                    ),
                     ImageCarouselColumn(
                    image_url='https://www.mook.com.tw/images/upload/article/18052/A18052_1528096840_2.jpg',
                    action=PostbackTemplateAction(
                        label = '新竹縣/市',
                        text = '新竹縣/市',
                        data='action=buy&itemid=5'
                        )
                    ),
                    ImageCarouselColumn(
                    image_url='https://shire16.tw/wp-content/uploads/2015/05/8220120709165609-1.jpg',
                    action=PostbackTemplateAction(
                        label = '宜蘭縣/市',
                        text = '宜蘭縣/市',
                        data='action=buy&itemid=6'
                        )
                    ),
                    ImageCarouselColumn(
                    image_url='https://lh3.googleusercontent.com/proxy/0xS_j3uBWHxLuuspte2TAV8YFd3hxOuko2gR4yHGBilAQoAs5muwhCHFty3iBxO0Ttq32AlhIWaUYXqYL12kwg-IH-YtZHkuJOT4xQ',
                    action=PostbackTemplateAction(
                        label = '返回',
                        text = '返回',
                        data='action=buy&itemid=7'
                        )
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
            template = ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                    image_url='https://i0.wp.com/blog.kkday.com/wp-content/uploads/batch_shutterstock_1519764494.jpg?resize=900%2C600&quality=80&strip=all&ssl=1',
                    action=
                        PostbackTemplateAction(
                        label = '苗栗縣/市',
                        text ='苗栗縣/市',
                        data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                    image_url='https://www.taichung.gov.tw/media/402339/%E6%98%A5%E7%AF%80%E9%81%8A%E5%8F%B0%E4%B8%AD-%E8%A7%80%E6%97%85%E5%B1%80%E5%BB%BA%E8%AD%B0%E7%86%B1%E9%96%80%E8%A7%80%E5%85%89%E6%99%AF%E9%BB%9E.jpg?width=400',
                    action=
                        PostbackTemplateAction(
                        label = '台中市',
                        text = '台中市',
                        data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                    image_url='https://cc.tvbs.com.tw/img/program/upload/2018/06/04/20180604185637-442e65bd.jpg',
                    action=
                        PostbackTemplateAction(
                        label = '彰化縣/市',
                        text = '彰化縣/市',
                        data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                    image_url='https://margaret.tw/wp-content/uploads/nEO_IMG_P2340089.jpg',
                    action=
                        PostbackTemplateAction(
                        label = '南投縣/市',
                        text = '南投縣/市',
                        data='action=buy&itemid=1'
                        )
                    
                    ),
                    ImageCarouselColumn(
                    image_url='https://image.kkday.com/v2/image/get/w_960%2Cc_fit%2Cq_55%2Ct_webp/s1.kkday.com/product_103660/20200929105846_FbgHj/jpg',
                    action=
                        PostbackTemplateAction(
                        label = '雲林縣',
                        text = '雲林縣',
                        data='action=buy&itemid=1'
                        ) 
                    ),
                    ImageCarouselColumn(
                    image_url='https://lh3.googleusercontent.com/proxy/0xS_j3uBWHxLuuspte2TAV8YFd3hxOuko2gR4yHGBilAQoAs5muwhCHFty3iBxO0Ttq32AlhIWaUYXqYL12kwg-IH-YtZHkuJOT4xQ',
                    action=
                        PostbackTemplateAction(
                        label = '返回',
                        text = '返回',
                        data='action=buy&itemid=1'
                        )
                    )
                ]
            )
        )         
        line_bot_api.reply_message(event.reply_token,template_message)
        send_text_message(event.reply_token,"your choose:"+event.message.text)
    def on_enter_choose_city_South(self, event):
        print("I'm entering choose_city_South")
        channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
        line_bot_api = LineBotApi(channel_access_token)
        template_message = TemplateSendMessage(
            alt_text='carousel template',
            template = ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                    image_url='https://blog.tripbaa.com/wp-content/uploads/2018/01/4-4.jpg',
                    action=
                        PostbackTemplateAction(
                        label = '台南市',
                        text ='台南市',
                        data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                    image_url='https://static.taisounds.com/WebUpd/TaiSounds/society/kao.jpg',
                    action=
                        PostbackTemplateAction(
                        label = '高雄市',
                        text = '高雄市',
                        data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                    image_url='https://owlting-blog-media.s3.ap-northeast-1.amazonaws.com/wp-content/uploads/2020/03/26235802/shutterstock_1557680306.jpg',
                    action=
                        PostbackTemplateAction(
                        label = '屏東縣/市',
                        text = '屏東縣/市',
                        data='action=buy&itemid=1'
                        )

                    ),
                    ImageCarouselColumn(
                    image_url='https://nurseilife.cc/wp-content/uploads/2015-01-04-100952-3.jpg',
                    action=PostbackTemplateAction(
                        label = '嘉義縣/市',
                        text = '嘉義縣/市',
                        data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                    image_url='https://lh3.googleusercontent.com/proxy/0xS_j3uBWHxLuuspte2TAV8YFd3hxOuko2gR4yHGBilAQoAs5muwhCHFty3iBxO0Ttq32AlhIWaUYXqYL12kwg-IH-YtZHkuJOT4xQ',
                    action=
                        PostbackTemplateAction(
                        label = '返回',
                        text = '返回',
                        data='action=buy&itemid=1'
                        )
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
            template = ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                    image_url='https://im.marieclaire.com.tw/m800c533h100b0/assets/mc/202002/5E4ABDFA2F9F41581956602.jpeg',
                    action=
                        PostbackTemplateAction(
                        label = '花蓮縣/市',
                        text ='花蓮縣/市',
                        data='action=buy&itemid=7'
                        )
                    
                    ),
                    ImageCarouselColumn(
                    image_url='https://im.marieclaire.com.tw/m800c533h100b0/assets/mc/202003/5E80DFCA5AAE61585504202.jpeg',
                    action=
                        PostbackTemplateAction(
                        label = '台東縣/市',
                        text = '台東縣/市',
                        data='action=buy&itemid=7'
                        )
                    
                    ),
                    ImageCarouselColumn(
                    image_url='https://photo.travelking.com.tw/scenery/2F43B3A0-1495-4B96-A961-C08350DAF43F_d.jpg',
                    action=
                        PostbackTemplateAction(
                        label = '澎湖縣',
                        text = '澎湖縣',
                        data='action=buy&itemid=7'
                        )
                    
                    ),
                    ImageCarouselColumn(
                    image_url='https://image.kkday.com/v2/image/get/w_960%2Cc_fit%2Cq_55%2Ct_webp/s1.kkday.com/product_123118/20210923082907_q5z4b/jpg',
                    action=
                        PostbackTemplateAction(
                        label = '綠島',
                        text = '綠島',
                        data='action=buy&itemid=7'
                        )
                    
                    ),
                    ImageCarouselColumn(
                    image_url='https://i0.wp.com/blog.kkday.com/wp-content/uploads/batch_Taiwan_Orchid-Island-_AShutterstock_1542646931.jpg?fit=900%2C600&quality=80&strip=all&ssl=1',
                    action=
                        PostbackTemplateAction(
                        label = '蘭嶼',
                        text = '蘭嶼',
                        data='action=buy&itemid=7'
                        )
                    
                    ),
                    ImageCarouselColumn(
                    image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ7vDK8P0IH12JF3yCsjGu5MWJSXyKBDRnSj-JceoPOfyjqpcxPcHUjoQrpKvIs-muAPHs&usqp=CAU',
                    action=
                        PostbackTemplateAction(
                        label = '金門',
                        text = '金門',
                        data='action=buy&itemid=7'
                        )
                    
                    ),
                    ImageCarouselColumn(
                    image_url='https://www.gomaji.com/blog/wp-content/uploads/2020/11/104219017_717158279098466_2719060153688610261_n.jpg',
                    action=
                        PostbackTemplateAction(
                        label = '馬祖',
                        text = '馬祖',
                        data='action=buy&itemid=7'
                        )
                    
                    ),
                    ImageCarouselColumn(
                    image_url='https://lh3.googleusercontent.com/proxy/0xS_j3uBWHxLuuspte2TAV8YFd3hxOuko2gR4yHGBilAQoAs5muwhCHFty3iBxO0Ttq32AlhIWaUYXqYL12kwg-IH-YtZHkuJOT4xQ',
                    action=
                        PostbackTemplateAction(
                        label = '返回',
                        text = '返回'
                        )
                    
                    )
                ]
            )
        )         
        line_bot_api.reply_message(event.reply_token,template_message)
        send_text_message(event.reply_token,"your choose:"+event.message.text)

    def on_enter_Keelung_City(self,event):
        url="https://travel.ettoday.net/category/%E5%9F%BA%E9%9A%86/"
        res=get_url(url)
        send_text_message(event.reply_token,res)
    def on_enter_New_Taipei_City(self,event):
        url="https://travel.ettoday.net/category/%E6%96%B0%E5%8C%97/"
        res=get_url(url)
        send_text_message(event.reply_token,res)
    def on_enter_Taipei_City(self,event):
        url="https://travel.ettoday.net/category/%E5%8F%B0%E5%8C%97/"
        res=get_url(url)
        send_text_message(event.reply_token,res)
    def on_enter_Taoyuan_City(self,event):
        url="https://travel.ettoday.net/category/%E6%A1%83%E5%9C%92/"
        res=get_url(url)
        send_text_message(event.reply_token,res)
    def on_enter_Hsinchu(self,event):
        url="https://travel.ettoday.net/category/%E6%96%B0%E7%AB%B9/"
        res=get_url(url)
        send_text_message(event.reply_token,res)
    def on_enter_Miaoli(self,event):
        url="https://travel.ettoday.net/category/%E8%8B%97%E6%A0%97/"
        res=get_url(url)
        send_text_message(event.reply_token,res)
    def on_enter_Taichung_City(self,event):
        url="https://travel.ettoday.net/category/%E5%8F%B0%E4%B8%AD/"
        res=get_url(url)
        send_text_message(event.reply_token,res)
    def on_enter_Changhua(self,event):
        url="https://travel.ettoday.net/category/%E5%BD%B0%E5%8C%96/"
        res=get_url(url)
        send_text_message(event.reply_token,res) 
    def on_enter_Nantou(self,event):
        url="https://travel.ettoday.net/category/%E5%8D%97%E6%8A%95/"
        res=get_url(url)
        send_text_message(event.reply_token,res)    
    def on_enter_Yunlin_County(self,event):
        url="https://travel.ettoday.net/category/%E9%9B%B2%E6%9E%97/"
        res=get_url(url)
        send_text_message(event.reply_token,res)
    def on_enter_Chiayi(self,event):
        url="https://travel.ettoday.net/category/%E5%98%89%E7%BE%A9/"
        res=get_url(url)
        send_text_message(event.reply_token,res)
    def on_enter_Tainan_City(self,event):
        url="https://travel.ettoday.net/category/%E5%8F%B0%E5%8D%97/"
        res=get_url(url)
        send_text_message(event.reply_token,res)
    def on_enter_Kaohsiung_City(self,event):
        url="https://travel.ettoday.net/category/%E9%AB%98%E9%9B%84/"
        res=get_url(url)
        send_text_message(event.reply_token,res)
    def on_enter_Pingtung(self,event):
        url="https://travel.ettoday.net/category/%E5%B1%8F%E6%9D%B1/"
        res=get_url(url)
        send_text_message(event.reply_token,res)
    def on_enter_Yilan(self,event):
        url="https://travel.ettoday.net/category/%E5%AE%9C%E8%98%AD/"
        res=get_url(url)
        send_text_message(event.reply_token,res)
    def on_enter_Hualien(self,event):
        url="https://travel.ettoday.net/category/%E8%8A%B1%E8%93%AE/"
        res=get_url(url)
        send_text_message(event.reply_token,res) 
    def on_enter_Taitung(self,event):
        url="https://travel.ettoday.net/category/%E5%8F%B0%E6%9D%B1/"
        res=get_url(url)
        send_text_message(event.reply_token,res)  
    def on_enter_Penghu_County(self,event):
        url="https://travel.ettoday.net/category/%E6%BE%8E%E6%B9%96/"
        res=get_url(url)
        send_text_message(event.reply_token,res)
    def on_enter_Green_Island(self,event):
        url="https://travel.ettoday.net/category/%E7%B6%A0%E5%B3%B6/"
        res=get_url(url)
        send_text_message(event.reply_token,res)   
    def on_enter_Orchid_Island(self,event):
        url="https://travel.ettoday.net/category/%E8%98%AD%E5%B6%BC/"
        res=get_url(url)
        send_text_message(event.reply_token,res) 
    def on_enter_Kinmen_County(self,event):
        url="https://travel.ettoday.net/category/%E9%87%91%E9%96%80/"
        res=get_url(url)
        send_text_message(event.reply_token,res) 
    def on_enter_Matsu(self,event):
        url="https://travel.ettoday.net/category/%E9%A6%AC%E7%A5%96/"
        res=get_url(url)
        send_text_message(event.reply_token,res)
     