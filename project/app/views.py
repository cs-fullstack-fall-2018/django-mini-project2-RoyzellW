from django.shortcuts import render
from .models import MusicSheet


def index(request):
    music_library = MusicSheet.objects.all
    context = {'music_library': music_library}
    return render(request, 'app/basic.html', context)