from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})

@login_required
def chat(request):
    return TemplateResponse(request, "chat/single_chat.html")