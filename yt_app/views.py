from django.shortcuts import render
import requests

def home_view(request):
    return render(request, 'home.html')


def get_channels(request, channel_name):
    channel_name = 'searchquery'
    if request.method == 'POST':
        if 'search' in request.POST:
            
            API_KEY = 'AIzaSyCIP1h0feeNX6iJYwFolhHvAu7tnRWmZgw'
            base_url = 'https://www.googleapis.com/youtube/v3/search'
            params = {
                'key': API_KEY,
                'q': channel_name,
                'type': 'channel',
                'part': 'snippet',
                'maxResults': 10
            }

