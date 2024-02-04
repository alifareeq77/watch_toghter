# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer


class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"control_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        # Assume text_data is a JSON string like '{"value": "some_value"}'
        data = json.loads(text_data)
        value_to_send = data.get('control')

        # Send the value back to the client
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "control.message", "control": value_to_send}
        )

    async def control_message(self, event):
        control = event['control']
        await self.send(text_data=json.dumps({"control": control}))
