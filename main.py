from time import sleep
from pytube import YouTube, Stream
from moviepy.editor import *
from os import listdir


def main() -> None:
    run_video_downloads()
    run_video_to_audio_conversion()


def run_video_downloads() -> None:
    urls = open('urls.txt', 'r')
    urls = [x.removesuffix('\n') for x in urls]

    for index, url in enumerate(urls):
        index: int
        url: str
        yt: YouTube

        try:
            yt = YouTube(url)
        except:
            error_message = 'Connection error! - URL: %s' % url
            print(error_message)
            continue
        
        try:
            streams = yt.streams
        except:
            error_message = 'Connection error! - URL: %s' % url
            print(error_message)
            continue
        
        streams = list(streams.filter(only_audio=True, file_extension='mp4'))

        if len(streams) == 0:
            error_message = 'Could not find streams for URL: %s' % url
            print(error_message)
            continue

        stream: Stream
        stream = streams[0]

        try:
            stream.download('C:/Users/Amir Sharapov/code/random/3/videos')
        except:
            error_message = 'Connection error! - URL: %s' % url
            print(error_message)
            continue

        success_message = 'Success: {}/{}: URL: {}'.format(
            index, len(urls), url)
        print(success_message)

        sleep(1)


def run_video_to_audio_conversion() -> None:
    videos = listdir('videos')

    for video in videos:
        input_name = video
        input_name = 'videos/{}'.format(input_name)

        output_name = video.removesuffix('.mp4')
        output_name = output_name + '.mp3'
        output_name = 'audio/{}'.format(output_name)

        audio_clip = AudioFileClip('videos/{}'.format(video))
        audio_clip.write_audiofile(output_name)
        audio_clip.close()


if __name__ == '__main__':
    main()