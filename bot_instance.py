import twitch
import logging
import twitch.helix as helix
import twitch.chat as chat
import webhook
import time

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
        self.buf.append(message.sender + "\t" + ":" + "\t" + message.text + "\n")

    def stop_bot(self):
        file = open(self.channel+ time.strftime('%Y-%m-%d', time.localtime(time.time())) +".txt", "w", encoding='utf-8')
        file.write(''.join(self.buf))
        self.buf.clear()

    def start_bot(self):
        self.chat.subscribe(self.handle_message)

