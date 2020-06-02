from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from source.get_video_ids import get_video_ids
from source.get_video_information import get_video_information
from source.buildinfo import buildinfo  # This is just a python file with APIKEY as a variable
from source.get_video_transcripts import get_video_transcripts


class youtubevideo:
    """
    Class for the videos to be stored in
    """

    def __init__(self, id, title, description, views, published, likes, dislikes,
                 comment_count, channel_name, channel_id, transcription):
        self.id = id
        self.title = title
        self.description = description
        self.views = views
        self.published = published
        self.likes = likes
        self.dislikes = dislikes
        self.comment_count = comment_count
        self.channel_name = channel_name
        self.channel_url = channel_id
        self.transcription = transcription


video_ids = get_video_ids('starcraft', 10, buildinfo)










for id in video_ids:

    video_information = get_video_information(id, buildinfo)

    video_transcripts = get_video_transcripts(video_ids[id])

    yt_v = youtubevideo(
        id=video_information[0]['id'],
        title=video_information[0]['snippet']['title'],
        description=video_information[0]['snippet']['description'],
        views=video_information[0]['statistics']['viewCount'],
        published=video_information[0]['snippet']['publishedAt'],
        likes=video_information[0]['statistics']['likeCount'],
        dislikes=video_information[0]['statistics']['dislikeCount'],
        comment_count=video_information[0]['statistics']['commentCount'],
        channel_name=video_information[0]['snippet']['channelTitle'],
        channel_id= video_information[0]['snippet']['channelId'],
        transcription=video_transcripts
    )
