from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
import app.routing

application = ProtocolTypeRouter ({
    # Nanti Balik Lagi
    "websocket": AuthMiddlewareStack(
        URLRouter(
            app.routing.websocket_urlpatterns
        )
    )
})