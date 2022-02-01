# Youtube Audio Builder

The purpose of this project is to donwload mp3 audios from a list of youtube video links.

# Get Started

## Setup the project

1. `python -m venv .venv`
2. `. .venv/Scripts/activate`
3. `pip install -r requirements.txt`

## Configure

Configure the `urls.txt` file to include the youtube URLS that you would like to download the mp3 version of.

## Run!

Run the following command:

`python main.py`

And you will see your console is going to have things happening and you will see your downloads in the videos and audio folder respectively!

# Notes

1. pytube is a library which sends requests to youtube and grabs the data. youtube in return can ocassionally change their code which can ocassionally cause pytube to crash. If that is the case, copy and paste the following into google: `AttributeError("'NoneType' object has no attribute 'span'")` and debug! :)