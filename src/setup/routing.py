from channels.auth import AuthMiddlewareStack # identifica o usuário que está enviando a mensagem
from channels.routing import ProtocolTypeRouter, URLRouter

import apps.chat.routing as chat_routing


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat_routing.websocket_urlpatterns
        )
    )
})
