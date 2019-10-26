import twitch
import twitch.helix as helix
from datetime import timedelta
from bot_instance import bot_instance
# from flask import Flask, request
import requests
import json
# import webhook
import threading
from time import sleep
import os


# app = Flask(__name__)
# api = Api(app)

# helix_api = twitch.Helix('hqiwd4o8a3mf6l7t7l0xge8qt7ksob', use_cache=True, cache_duration=timedelta(minutes=1))

bots = []
channels = ["hanryang1125", "yapyap30", "handongsuk", "saddummy", "lol_ambition", 'yumyumyu77', 'tmxk319', 'woowakgood', 'pacific18815', 'zilioner', 'ddahyoni', 'flurry1985',
        'jinu6734', 'nokduro', 'a34016042', '2chamcham2', 'looksam', 'dogwellfish', 'nanajam777', 'faker', 'rkdwl12', 'ajehr', 'silphtv', 'playhearthstonekr', 'obm1025', 'so_urf',
        'lucia94', 'rhdgurwns', 'rudbeckia7', 'lol_wolf', 'sal_gu', 'alenenwooptv', 'naseongkim', 'teaminven', 'kimdoe', 'jungtaejune', 'pjs9073', 'collet11', 'nanayango3o', 'kangqui',
        'wkgml', 'moogrr1121', 'kss7749', 'kumiokmii', 'dkwl025', 'rooftopcat99', 'sonycast_', 'tranth', 'buzzbean11', 'ses836', 'sizer0346', 'h902103', 'boowoonim', 'cherrypach', 'playoverwatch_kr',
        'dragon3652', 'kimdduddi', 'kanetv8', '9ambler', 'rbhr', 'newmasca', 'lol_madlife', 'heavyrainism', 'beyou0728', 'zzamtiger0310', 'xkwhd', 'hejin0_0', '109ace', 'dawnhs', 'ok_ja', 'juyoung1114',
        'overwatchleague_kr', 'jmjdoc', 'nobugi', 'harroman', 'bighead003', 's1032204', 'bgirl_0', 'pakusyo', 'sah_hyang', 'mirage720', 'crazzycat', 'yd0821', 'ma_mwa', 'chonana1', 'rkdthdus930', 'pubgkorea', 
        'kanjang7', 'portialyn', 'yuwol', 'mister903', 'broodling2', 'wltn4765', 'dda_ju', 'bbb99', 'dlxowns45', 'hatsalsal', 'game2eye', 'scsc95', 'leehunnyeo', 'yugyungwoo', 'taesangyun', 'pikra10', 'drlee_kor',
        'tvcrank', 'luck22222', 'funzinnu', 'wlswnwlswn', 'gabrielcro', 'akdlfnadl10', 'baedony', 'charming_jo', 'nadotv86', 'tkdtn307', 'yuhwanp', 'jubssal',
        't1_teddy', 'wpghd321', 'ca_ramel', 'runray_', 'penyo_', 'dingseption', 'ras_sama', 'deserteagle2012', 'cwn222', 'wpckor', 'lovelyyeon', 'ddolking555',
        'i_am_bloooo', 'suxkingiscoming', 'dua3362', 'd_obby', 'kasushilollol', 'lol_peanut', 'lruhon5', 'clid', 'zoodasa', 'liok0485', 'bbonge_', '3sunset3', 'thdlqslek', 'sasin_god', 
        'yuri_joa', 'bang', 'falgwang', 'megthomatho', 'e_saem', 'miracle0o0', 'genius_mad', 'sabin1', 'sooflower', 'sjko3', 'uzuhama', 'rainblue37', 'hosu0904',
        'mbcmlt3', 'rbwls1245', 'lol_khan', 'selly55', 'h0270', 'coppag2', 'runner0608', 'kiyulking', 'rea37', 'smartcrow', 'mirdayo', 'bulmyeol_tv', 'cbrace', 'queenmico', 'jojokgo1',
        'magenta62', 'godbokihs', 'maruemon1019', 'thebeatnam', 'rockid1818', 'gutterlife', 'coolguy0', 'bonnysurang', 'flowervin', 'baddalcho', 'jungjil', 'starcraft_kr', 'remguri',
        'd2kyun', 'leechunhyang', 'chunmuk2', 'pudu2000', 'rngudwnswkd', 'erenjjing', 'reniehour', 'berry0314', 'junyoopy', 'goldpeople', 'frog135', 'madkof_kof', 'hj0514', 
        'xyzzyshift', 'nrmtzv', 'mambo3337', 'rnlgus128', 'bjshaco', 'aram4519', 'ansansniper', 'eclipia', 'dlaqkf5676', 'dalto_ov', 'team_spiritzero', 'yoonroot', 'qcnb123', '0hega', 'aba4647', 'uskki']

# webhook_api = webhook.api("hqiwd4o8a3mf6l7t7l0xge8qt7ksob", 'neo5shztmgipdeblmmudm85jezms6u')

for i in channels:
    bots.append(bot_instance(i))
    target_dir = os.path.join('result', i)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

for i in bots:
    i.start_bot()

def push_buf():
    for i in bots:
        i.stop_bot()
    
threading.Timer(60*60*12, push_buf).start()

# class streamChangeCallback(Resource):
#     def get(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('hub.challenge', required=True)
#         args = parser.parse_args()
#         result = args['hub.challenge']
#         print(result)
#         return 
        
#     # else :
#     #     if request.form['data']:
#     #         print("start bot")
#     #         bots[channels.index(result['data'][0]['username'])].start_bot()
#     #     else :
#     #         print("stop bot")
    #         bots[channels.index(result['data'][0]['username'])].stop_bot()

# api.add_resource(streamChangeCallback, '/streamChangeCallback')

# if __name__ == '__main__':
#     app.run(debug=True)