from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from source.get_video_ids import get_video_ids
from source.get_video_information import get_video_information
from source.buildinfo import buildinfo  # This is just a python file with APIKEY as a variable
from source.get_video_transcripts import get_video_transcripts

video_ids = get_video_ids("starcraft", 10, buildinfo)

video_information = get_video_information(video_ids, buildinfo)

video_transcripts = get_video_transcripts(video_ids[0])