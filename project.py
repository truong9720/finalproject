import requests
from datetime import datetime


def getposts(topic: str, days, sortby):
    if not days:
        days = datetime.now().date()
    if not sortby:
        sortby = "Popularity"
    print(days)

    KEY = "4918a39177f64b02a96be747c45b4296"
    url = f"https://newsapi.org/v2/everything?q={
        topic}&from={days}&sortBy={sortby}&apiKey={KEY}"
    feedback = requests.get(url)
    result = feedback.json()
    return result


def printposts(result):
    count = 0
    for post in result["articles"]:
        if post["title"] != "[Removed]":
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
    topic = input("Enter Topic: ")
    days = input("Days (e.g YYYY-MM-DD): ")
    sortby = input("Sort By (e.g Newer ; Older ; Popularity) : ")
    result = getposts(topic, days, sortby)
    printposts(result)


if __name__ == "__main__":
    main()
