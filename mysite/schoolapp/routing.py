from django.urls import path, re_path
from . import views
from . import chat_handler
import logging

logger = logging.getLogger(__name__)


websocket_urlpatterns = [
    re_path(r"^ws/schoolapp/(?P<room_name>\w+)/$", chat_handler.ChatUser.as_asgi()),
]

logger.info("WebSocket URL patterns defined.")