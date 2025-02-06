import requests
from datetime import datetime
import json
import sys


def getposts(topic: str, days, sortby):
    if not days:
        days = datetime.now().date()
    if not sortby:
        sortby = "Popularity"

    KEY = "4918a39177f64b02a96be747c45b4296"
    url = f"https://newsapi.org/v2/everything?q={
        topic}&from={days}&sortBy={sortby}&apiKey={KEY}"
    feedback = requests.get(url)
    result = feedback.json()
    return result


def get_top_headlines(keyword):
    KEY = "4918a39177f64b02a96be747c45b4296"
    url = f"https://newsapi.org/v2/top-headlines?country={
        keyword}&apiKey={KEY}"
    feedback = requests.get(url)
    result = feedback.json()
    if len(result["articles"]) == 0:
        print("There is no headlines on this keyword")
        return result


def save_news(result, filename='news.json'):
    try:
        articles = []
        for post in result["articles"]:
            articles.append(
                {
                    "title": post["title"],
                    "description": post["description"],
                    "url": post["url"],
                    "author": post["author"],
                    "urlToImage": post["urlToImage"]
                }
            )

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(articles, f, indent=4)

        print(f"\nSuccessfully saved news to {filename}")

    except Exception as e:
        print(f"Error while saving news to file: {e}")


def menu():
    print("\n===News Application ===")
    print("1.Search news")
    print("2.Get top headlines")
    print("3.Save news to file")
    print("4.Exit")
    return input("Choose one option betwwen 1-4:")


def printposts(result):
    count = 0
    for post in result["articles"]:
        if post["title"] != "[Removed]":
            count = count + 1
            count = count + 1
            print("Title: {} ".format(post["title"]))
            print("Description: {} ".format(post["description"].strip()))
            print("Url: {} ".format(post["url"]))
            print("Author: {} ".format(post["author"]))
            print("UrlToImage: {} ".format(post["urlToImage"]))
            print("==================================")
            if count == 5:
                break


def main():
    news = None
    while True:
        choice = menu()
        if choice == "1":
            topic = input("Enter Topic: ")
            days = input("Days (e.g YYYY-MM-DD): ")
            sortby = input("Sort By (e.g Newer ; Older ; Popularity) : ")
            try:
                news = getposts(topic, days, sortby)
                printposts(news)
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "2":
            try:
                keyword = input("Enter a keyword: ")
                news = get_top_headlines(keyword)
                printposts(news)
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "3":
            if news:
                filename = input(
                    "Enter a file name: (if not, the default name is news.json)")
                save_news(news, filename)
            else:
                print("There are not any news before!")
        elif choice == "4":
            print("Exiting .....")
            sys.exit(0)
        else:
            print("Invalid inputing!!!")


if __name__ == "__main__":
    main()
