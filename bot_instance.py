import twitch
import logging
import twitch.helix as helix
import twitch.chat as chat
# import webhook
import time
import os

class bot_instance:
    def __init__(self, channel):#api:webhook.api):
        self.channel = channel
        # self.api = api
        # self._id = self.api.user_id(channel) #la6kj4pn3vzfdvvkfrg8y5eqvbuxjk   qxhcdwsgg5m3qm7or17f3lo51soznk
        # self.api.sub_streamchange(self._id)

        self.helix=twitch.Helix(client_id='hqiwd4o8a3mf6l7t7l0xge8qt7ksob', use_cache=True)
        self.chat = twitch.Chat(channel=channel,
                       nickname='bot',
                       oauth='oauth:la6kj4pn3vzfdvvkfrg8y5eqvbuxjk',
                       helix=self.helix)
        self.buf = []
            
    def handle_message(self, message: twitch.chat.Message) -> None:
        # "[{timestamp[relative]}] <{commenter[display_name]}> {message[body]}",
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))
        self.buf.append(f'[{now_time}] <{message.sender}> {message.text}\n')

    def stop_bot(self):
        now_time = time.strftime("%Y-%m-%d-%H%M", time.localtime(time.time()))
        print(f'[{now_time}]writing {self.channel}..')

        target_dir = os.path.join('result', self.channel)
        with open(os.path.join(target_dir, f'{now_time}.tsv'), "w", encoding='utf-8') as f:
            f.writelines(self.buf)
        self.buf.clear()

    def start_bot(self):
        self.chat.subscribe(self.handle_message)

