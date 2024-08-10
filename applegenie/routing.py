from django.urls import re_path

from applegenie import consumers

# websocket_urlpatterns = [
#     re_path(r"ws/chat/(?P<room_name>\w+)/$", QuestionAndAnswerChatConsumer.as_asgi()),
# ]
websocket_urlpatterns = [
    re_path(r'ws/chat/$', consumers.ChatConsumer.as_asgi()),
]