from datetime import datetime


def print_galnet_header():
    raw_date = datetime.now()
    formatted_date = raw_date.strftime("%b %d")
    ed_date = str(f"{formatted_date} 3305")

    print("///////////////////////////////////")
    print(f"GALNET NEWS v1.1 - {ed_date}")
    print("///////////////////////////////////\n")


def print_headlines(news_items: list, count: int):
    i = 1

    for news_item in news_items:
        if i < 10:
            print(f"{i}.   {news_item['date']}   {news_item['title']}")
        else:
            print(f"{i}.  {news_item['date']}   {news_item['title']}")

        i += 1

    print(f'\nA to read all headlines, else enter story ID (1 - {count}):')


def print_news_item(news_item: dict):
    news_story = str(news_item['content']).replace('<br \/>', '\n')
    news_story = news_story.replace('\n  ', '\n')
    string_to_print = f"\n{news_item['title']}\n\n{news_item['date']}\n\n{news_story}"

    print("\n/////////////////////////////////////////////////////////////////////////////////")
    print(string_to_print)
