import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    """Aceita qualquer conexão e envia qualquer mensagem para o WebSocket"""
    def connect(self):
        self.accept() # aceita qualquer conexão. Podemos rejeitar com self.close()

    def disconnect(self, close_code):
        pass

    # recebe uma mensagem do WebSocket
    def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # envia a mensagem para o websocket
        self.send(text_data=json.dumps({'message': message}))
