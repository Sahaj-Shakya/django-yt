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

            response = requests.get(base_url, params=params)
            if response.status_code == 200:
                data = response.json()

                channels = []
                for item in data.get('items', []):
                    channel = {
                        'title': item['snippet']['title'],
                        'description': item['snippet']['description'],
                        'channel_id': item['id']['channelId'],
                        'thumbnail_url': item['snippet']['thumbnails']['default']['url']
                    }
                    channels.append(channel)
                return render(request, 'channels.html', {'channels': channels})
            else:
                return render(request, 'error.html', {'message': 'Failed to fetch channels'})