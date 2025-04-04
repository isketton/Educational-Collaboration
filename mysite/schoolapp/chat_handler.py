import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatUser(AsyncWebsocketConsumer):
    async def connect(self):
        # check for auth
       # if not self.scope["user"].is_authenticated:
        #    await self.close(code=403, reason="Not Auth")
        #    return
        # get room_name parameter from route that opened connection
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        # create channels group name
        self.room_group_name = "chat_%s" % self.room_name
        
        # join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        
        await self.accept()
        
    async def disconnect(self, close_code):
        # leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
    
    # receive channel from websocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        # access username
        username = self.scope["user"].username 

        # send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message, "username": username}
        )
    
    # receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        
        # send message to Websocket
        await self.send(text_data=json.dumps({"message": message}))