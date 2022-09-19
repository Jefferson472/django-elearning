import json

from django.utils import timezone

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    """Aceita qualquer conexão e envia qualquer mensagem para o WebSocket"""
    async def connect(self):
        self.user = self.scope['user']
        self.id = self.scope['url_route']['kwargs']['course_id']
        self.room_group_name = 'chat_%s' % self.id # cria o grupo com base no id do curso
        # associa-se ao grupo da sala
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept() # aceita qualquer conexão. Podemos rejeitar com self.close()

    async def disconnect(self, close_code):
        # sai do grupo da sala
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # recebe uma mensagem do WebSocket
    async def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        now = timezone.now()

        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': self.user.username,
                'datetime': now.isoformat(),
            }
        )
        
    # recebe uma mensagem do grupo da sala
    async def chat_message(self, event):
        # envia a mensagem para o grupo da sala
        await self.send(text_data=json.dumps(event))
