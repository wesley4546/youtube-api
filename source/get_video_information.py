from googleapiclient.discovery import build

"""
**It's important that the YouTube specifications are found in the main.py in order for this function to work.**

This function is responsible for taking in a list of video IDs and retrieving the information

"""


def get_video_information(list_of_video_ids, buildinfo):
    # builds the youtube API object
    try:
        youtube = build(
            buildinfo["YOUTUBE_API_SERVICE_NAME"],
            buildinfo["YOUTUBE_API_VERSION"],
            developerKey=buildinfo["DEVELOPER_KEY"]
        )
    except:
        print("`buildinfo` not founds`")

    # Call the search.list method to retrieve results matching the video ids
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=list_of_video_ids
    )

    # execute's the command
    video_information = request.execute()

    # returns the items
    return video_information['items']
