import json
import asyncio
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class MyConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"control_{self.room_name}"

        # Add the consumer to the group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Remove the consumer from the group when disconnecting
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)

        # Handle different types of messages
        if data['type'] == 'updateVideoState':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'update_video_state',
                    'data': data['data']
                }
            )

    async def update_video_state(self, event):
        # Send the video state back to the client
        await self.send_json({
            'type': 'updateVideoState',
            'data': event['data']
        })
