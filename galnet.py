import ast
import requests

import speech
import printing

GALNET_URL = "https://www.alpha-orbital.com/galnet-feed"


def galnet_interactive():
    response = requests.get(GALNET_URL)
    news_items = response.text

    news_item_list = ast.literal_eval(news_items)

    printing.print_galnet_header()
    printing.print_headlines(news_item_list, len(news_item_list))

    speech.speak_header()

    user_input = input()
    if user_input in 'aA':
        speech.speak_headlines(news_item_list)
    elif isinstance(int(user_input), int):
        if int(user_input) <= len(news_item_list):
            idx = int(user_input) - 1

            printing.print_news_item(news_item_list[idx])
            speech.speak_news_item(news_item_list[idx])

    # TODO: Code returns here - need to manage what happens next!


# def fetch_galnet_news():
#     response = requests.get(GALNET_URL)
#     news_items = response.text
#
#     news_item_list = ast.literal_eval(news_items)
#     # news_item = news_item_list[0]
#
#     for news_item in news_item_list:
#         news_story = str(news_item['content']).replace('<br \/>', '\n')
#         news_story = news_story.replace('\n  ', '\n')
#
#         news_item_str = f"{news_item['title']}.  {news_item['date']}.  {news_story}."
#         news_item_str = news_item_str.replace('..', '.')
#
#         string_to_print = f"\n{news_item['title']}\n\n{news_item['date']}\n\n{news_story}"
#
#         string_to_print = string_to_print.replace('<br \/>', '\n')
#
#         print("\n/////////////////////////////////////////////////////////////////////////////////")
#         print(string_to_print)
#
#         speech.speak(news_item_str)


def main():
    # fetch_galnet_news()
    galnet_interactive()


if __name__ == "__main__":
    main()
