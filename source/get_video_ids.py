from googleapiclient.discovery import build

"""
**It's important that the YouTube specifications are found in the main.py in order for this function to work.**

This function is responsible for taking in a query and # of max results and returning a list of video IDs

"""


def get_video_ids(query, max_results, buildinfo):
    # builds the youtube API object
    try:
        youtube = build(
            buildinfo["YOUTUBE_API_SERVICE_NAME"],
            buildinfo["YOUTUBE_API_VERSION"],
            developerKey=buildinfo["DEVELOPER_KEY"]
        )
    except:
        print("`buildinfo` not founds`")

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


    return videos_ids
