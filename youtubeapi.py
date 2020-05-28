from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = ''
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def make_youtubevideo_url(video_id):
    url = "https://www.youtube.com/watch?v=" + video_id

    return url


def get_video_ids(query, max_results):
    # builds the youtube API object
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=query,
        part='id,snippet',
        relevanceLanguage="en",
        maxResults=max_results,
    ).execute()

    # Starts a blank list
    videos_ids = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos_ids.append((search_result['id']['videoId']))  # youtubevideo URL

    # In order for it to work the video api requests,
    stringifed_videos_ids = ",".join(videos_ids)

    return stringifed_videos_ids


def get_video_information(list_of_video_ids):
    # builds the youtube API object
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the video ids
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=list_of_video_ids
    )

    # execute's the command
    video_information = request.execute()

    # returns the items
    return video_information['items']


youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                developerKey=DEVELOPER_KEY)

testing = get_video_information(get_video_ids("starcraft", 10))

caption_id = "N2BePn4bhvih7yKQLXhp20OT-jNuF-He_qJO6k7XFFw"
subtitle = youtube.captions().download(
    id=caption_id,
).execute()

print("First line of caption track: %s" % subtitle)

"""
if __name__ == '__main__':

    keyword = input("Input search: ")
    nm_of_results = input("Maximum number of results: ")
    try:
        youtube_search(keyword, nm_of_results)
    except HttpError as e:
        print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
"""
"""
def get_video_statistics(list_of_video_ids):

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        ids = list_of_video_ids
    ).execute()
"""
