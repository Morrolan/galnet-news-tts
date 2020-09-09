import boto3
import os
import tempfile
import time
from pysndfx import AudioEffectsChain

from datetime import datetime


def speak(input_string: str):
    polly_client = boto3.client('polly')

    response = polly_client.synthesize_speech(VoiceId='Amy', OutputFormat='mp3', Text=input_string,
                                              LanguageCode='en-GB')

    # response = polly_client.synthesize_speech(VoiceId='Amy', Engine='neural', OutputFormat='mp3', Text=input_string, LanguageCode='en-GB')

    temp_file = os.path.join(tempfile.gettempdir(), 'speech.mp3')

    with open(temp_file, 'wb') as f:
        f.write(response['AudioStream'].read())

    os.system(f"afplay {temp_file}")


def speak_with_effect(input_string: str):
    fx = (
        AudioEffectsChain()
            .highshelf()
            .reverb()
            .phaser()
            # .delay()
            .lowshelf()
            .compand(attack=100, decay=2, soft_knee=2.0, threshold=-20, db_from=-20.0, db_to=-20.0)
    )

    polly_client = boto3.client('polly')

    response = polly_client.synthesize_speech(VoiceId='Amy', OutputFormat='mp3', Text=input_string,
                                              LanguageCode='en-GB')

    # declare where we are going to cache our speech pattern
    temp_file = os.path.join(tempfile.gettempdir(), 'temp.mp3')

    # lets take the input stream from the response and write it out to our tempfile
    with open(temp_file, 'wb') as f:
        f.write(response['AudioStream'].read())

    # declare our post-processing output location
    outfile = 'speech_with_effects.mp3'

    # add effects
    fx(temp_file, outfile)

    # play the damned thing!
    os.system(f"afplay {outfile}")


def speak_async(input_string: str):
    polly_client = boto3.client('polly')

    response = polly_client.synthesize_speech(VoiceId='Amy', OutputFormat='mp3', Text=input_string,
                                              LanguageCode='en-GB')

    temp_file = os.path.join(tempfile.gettempdir(), 'speech.mp3')
    with open(temp_file, 'wb') as f:
        f.write(response['AudioStream'].read())

    os.system(f"afplay {temp_file} &")


def speak_header():
    ed_date = (datetime.now())

    ed_date_string = ed_date.strftime("%b %d")

    header_string = f"Welcome to Galnet News version 1.1.  The date is {str(ed_date_string)} 3305."
    speak(header_string)
    #
    polite_string = "Press A to read all headlines, or select the story ID."
    speak(polite_string)


def speak_headlines(news_item_list: list):
    for news_item in news_item_list:
        speak(f"{news_item['date']} - {news_item['title']}")
        time.sleep(0.8)


def speak_news_item(news_item: dict):
    news_story = str(news_item['content']).replace('<br \/>', '\n')
    news_story = news_story.replace('\n  ', '\n')
    news_item_str = f"{news_item['title']}.  {news_item['date']}.  {news_story}."

    speak(news_item_str)
    # speak_with_effect(news_item_str)
