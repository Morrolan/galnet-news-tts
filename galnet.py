import ast
import boto3
import requests
import os

GALNET_URL = "https://www.alpha-orbital.com/galnet-feed"


def fetch_galnet_news(galnet_url: str) -> str:
    response = requests.get(galnet_url)
    news_items = response.text

    news_item_list = ast.literal_eval(news_items)
    news_item = news_item_list[0]

    news_story = str(news_item['content']).replace('<br \/>', '\n')
    news_story = news_story.replace('\n  ', '\n')

    news_item_str = f"{news_item['title']}.  {news_item['date']}.  {news_story}."
    news_item_str = news_item_str.replace('..', '.')

    string_to_print = f"""\n{news_item['title']}\n\n{news_item['date']}\n\n{news_story}"""

    string_to_print = string_to_print.replace('<br \/>', '\n')
    print(string_to_print)

    return news_item_str


def send_to_polly(input_string: str):
    polly_client = boto3.client('polly')

    response = polly_client.synthesize_speech(VoiceId='Amy', OutputFormat='mp3', Text=input_string,
                                              LanguageCode='en-GB')

    with open('speech.mp3', 'wb') as f:
        f.write(response['AudioStream'].read())

    os.system("afplay speech.mp3")


def main():
    news_item = fetch_galnet_news(GALNET_URL)
    send_to_polly(news_item)


if __name__ == "__main__":
    main()
