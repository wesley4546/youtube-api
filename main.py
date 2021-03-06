import csv
import sys
import time
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
        self.channel_id = channel_id
        self.transcription = transcription


# Creates a function to create a file name based off the keyword
def paste_filename(search):
    """
    Function that will create a name for the files to be saved to using the search
    """
    # Removes any spaces
    cleaned_keyword = search.replace(' ', '_')

    # Adds 'videos.csv' at the end
    filename = cleaned_keyword + "_videos.csv"

    return filename


def main():
    """
    Function starts the process of extracting videos from YouTube using a user-input search

    I'm not sure of any restrictions when it comes to API calls from other modules in this program so I have a delay
    of 5 seconds between each function call in the looping process If this causes and issue then it can certainly
    be changed.
    """
    url_number = 1

    # Takes a YouTube URL as input
    input_keyword = input("Enter YouTube Search: ")
    input_results = int(input("Enter # of Max Results: "))

    # Data used as each column
    csv_column_names = ['keyword',
                        'id',
                        'title',
                        'description',
                        'views',
                        'published',
                        'likes',
                        'dislikes',
                        'comment_count',
                        'channel_id',
                        'channel_name',
                        'transcription']

    # Creates a file
    print("Creating New CSV File...")
    with open(paste_filename(input_keyword), 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(csv_column_names)

    # Gets the list of video IDs
    video_ids = get_video_ids(input_keyword, input_results, buildinfo)

    # Starts loop through video IDs
    for id in video_ids:

        print(f"Starting video ID:{id}")
        time.sleep(5)

        # Gets the video information
        video_information = get_video_information(id, buildinfo)

        # Testing for missing values
        if not 'commentCount' in video_information[0]['statistics']:
            video_information[0]['statistics']['commentCount'] = "Not Found"

        if not 'likeCount' in video_information[0]['statistics']:
            video_information[0]['statistics']['likeCount'] = "Not Found"

        if not 'dislikeCount' in video_information[0]['statistics']:
            video_information[0]['statistics']['dislikeCount'] = "Not Found"

        # Gets the video transcription
        video_transcripts = get_video_transcripts(id)

        # Adds them to the YouTube Class
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
            channel_id=video_information[0]['snippet']['channelId'],
            transcription=video_transcripts
        )

        # Rows to be written to CSV
        csv_file_rows = (input_keyword,
                         yt_v.id,
                         yt_v.title,
                         yt_v.description,
                         yt_v.views,
                         yt_v.published,
                         yt_v.likes,
                         yt_v.dislikes,
                         yt_v.comment_count,
                         yt_v.channel_id,
                         yt_v.channel_name,
                         yt_v.transcription
                         )

        # Writes the rows to the files
        with open(paste_filename(input_keyword), 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(csv_file_rows)

        # Messaging
        print(f"{url_number}/{input_results} Complete...")
        url_number += 1

    print("Done!")


if __name__ == '__main__':
    main()
