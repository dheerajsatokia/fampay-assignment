import datetime
import requests
import logging

from youtube.models import VideoDetail, ApiKey

logger = logging.getLogger()


def add_latest_video():
    """
    Description : Cron job to async add 25 videos every 10 second
    """
    for api_key in ApiKey.objects.all():
        if not api_key.status and api_key.updatedAt + datetime.timedelta(hours=2) < datetime.datetime.now():
            api_key.status = True

    youtube_data = []

    api_key_obj = ApiKey.objects.filter(status=True).first()

    try:
        search_url = 'https://www.googleapis.com/youtube/v3/search'

        params = {
            'part': 'snippet',
            'q': 'cricket',
            'maxResults': 25,
            'key': api_key_obj.secret
        }

        youtube_data = (requests.get(search_url, params=params)).json()
    except:
        logger.warning('api key limit exceed')
        api_key_obj.status = False
        api_key_obj.updatedAt = datetime.datetime.now()

    for video in youtube_data['items']:

        try:
            snippet = video['snippet']
            thumbnail = snippet['thumbnails']

            VideoDetail.objects.create(
                title=snippet['title'],
                description=snippet['description'],
                publishedAt=snippet['publishedAt'],
                default_thumbnail=thumbnail['default']['url'],
                medium_thumbnail=thumbnail['medium']['url'],
                high_thumbnail=thumbnail['high']['url']
            )
            logger.info('video data updated successfully')
        except:
            logger.error('video data is not updated')
