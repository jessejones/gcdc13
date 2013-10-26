from django.shortcuts import render
from os.path import join, dirname
from apiclient.discovery import build
from optparse import OptionParser
from lingo.local_settings import API_KEY

API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def display_results(request, mid):
    youtube = build(API_SERVICE_NAME, API_VERSION, developerKey=API_KEY)

    search_response = youtube.search().list(
        topicId=mid,
        part='id,snippet',
        maxResults=10
    ).execute()

    video_ids = []
    channel_ids = []
    playlist_ids = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            video_ids.append("%s" % search_result["id"]["videoId"])
        elif search_result["id"]["kind"] == "youtube#channel":
            channel_ids.append("%s" % search_result["id"]["channelId"])
        elif search_result["id"]["kind"] == "youtube#playlist":
            playlist_ids.append("%s" % search_result["id"]["playlistId"])

    return render (request, 'youtube/results.html', {
        "videos": video_ids,
    })