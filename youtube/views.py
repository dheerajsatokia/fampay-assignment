import logging

from django.conf import settings
from rest_framework.decorators import api_view

from .models import VideoDetail
from .serializers import VideoSerializer, APIKeySerializer

from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger()


@api_view(['GET'])
def get_videos(request):
    """

    :param request: limit - type (integer) to set pagination limit, offset - type(integer) to set the offset,
    search - type(string) to filter the database using search key word
    :type request: GET
    :return: list of videos
    :rtype: list
    """
    params = request.query_params
    offset = 0
    limit = settings.DEFAULT_LIMIT

    kwargs = {}

    if 'offset' in params and params['offset'].isdigit():
        offset = int(params['offset'])
    if 'limit' in params and params['limit'].isdigit():
        limit = int(params['limit'])
    if 'search' in params:
        kwargs['title__icontains'] = params['search']

    video_query = VideoDetail.objects.filter(**kwargs).order_by('-publishedAt')
    serializer = VideoSerializer(video_query[offset:(offset + limit)], many=True)
    data = {
        'count': video_query.count(),
        'list': serializer.data
    }
    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_api_key(request):
    """

    :type request: POST
    :return: APIKey object
    :rtype: dictionary
    """
    serializer = APIKeySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

