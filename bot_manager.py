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
channels = ["bobross", "watsoncomedy"]

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
    threading.Timer(60*60*8, push_buf).start()

push_buf()

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
