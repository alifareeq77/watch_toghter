from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'vid/vid.html', {})


def chat_test(request, room_name):
    return render(request, 'vid/test.html', {"room_name": room_name})
