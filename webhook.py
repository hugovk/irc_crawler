import requests
import json

class api():
    def __init__(self, client_id, client_secret):
        self.header = {}
        self.url = 'https://api.twitch.tv/helix/'
        self.client_id = client_id
        self.client_secret = client_secret
        self.bearer = self.get_accesstoken()

    def get_accesstoken(self):
        url = "https://id.twitch.tv/oauth2/token?" + "client_id=" + self.client_id + "&client_secret=" + self.client_secret + "&grant_type=client_credentials"
        response = requests.post(url)
        data = response.json()
        print(data)
        return data['access_token']
    
    def user_id(self, channel):
        url = self.url + 'users'
        param = {'login':channel}
        header = {}
        header['Authorization'] = "Bearer "  + self.bearer
        response = requests.get(url=url, params=param, headers=header)
        resjson = response.json()
        return resjson['data'][0]['id']
    
    def get_sub(self):
        url = self.url + 'webhooks/subscriptions'
        header = {}
        header['Authorization'] = "Bearer " + self.bearer
        response = requests.get(url=url, headers=header)
        data = response.json()

    def sub_streamchange(self, _id):
        url = self.url + 'webhooks/hub'
        header = self.header
        header['Client_ID'] = self.client_id
        data = {}
        data['hub.mode'] = 'subscribe'
        data['hub.topic'] = 'https://api.twitch.tv/helix/streams?user_id=' + _id
        data['hub.callback'] = 'http://1a351f72.ngrok.io:5000/streamChangeCallback'
        data['hub.lease_seconds'] = 86400
        response = requests.post(url, data=data, headers=header)
        data = response.json()
        print(data)
        
