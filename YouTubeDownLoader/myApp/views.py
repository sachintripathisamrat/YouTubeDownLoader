import os
from django.template import Context, loader
from pytube import YouTube
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')


def add(request):
    link = request.GET.get('youtubeLink', '')

    yt = YouTube(link)
    streams = yt.streams.filter(progressive=True, file_extension='mp4')

    download_links = [
        f'<a href="{stream.url}" download>Download {stream.resolution}</a>' for stream in streams
    ]

    download_options = '<br>'.join(download_links)

    return render(request, 'download_options.html', {'download_options': download_options})