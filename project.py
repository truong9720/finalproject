import requests
from datetime import datetime
import platform
import json
import sys
import os

def clear():
    if platform.system() == 'Windows':
        os.system('cls')

def getposts(topic: str, days, sortby):
    if not days:
        days = datetime.now().date()
    if not sortby:
        sortby = "popularity"

    KEY = "4918a39177f64b02a96be747c45b4296"
    url = f"https://newsapi.org/v2/everything?q={topic}&from={days}&sortBy={sortby}&apiKey={KEY}"
    feedback = requests.get(url)
    result = feedback.json()
    return result

def get_top_headlines(keyword):
    KEY = "4918a39177f64b02a96be747c45b4296"
    url = f"https://newsapi.org/v2/top-headlines?country={keyword}&apiKey={KEY}"
    feedback = requests.get(url)
    result = feedback.json()
    if len(result.get("articles", [])) == 0:
        print("There are no headlines on this  keyword")
    return result

def save_news(result, filename):
    try:
        articles = []
        for post in result.get("articles", []):
            articles.append(
                {
                    "title": post.get("title", "No title available"),
                    "description": post.get("description", "No description available"),
                    "url": post.get("url", "No URL available"),
                    "author": post.get("author", "Unknown author"),
                    "urlToImage": post.get("urlToImage", "No image available")
                }
            )
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(articles, f, indent=4)
        print(f"\nSuccessfully saved news to {filename}")

    except Exception as e:
        print(f"Error while saving news to file: {e}")

def menu():
    print("\n📰 === News Application === 📰")
    print("1. 📝 Search News 📝")
    print("2. 🔔 Get Top Headlines 🔔")
    print("3. 💾 Save news to file 💾")
    print("4. 🛑 Exit 🛑")
    return input("Choose an option between 1-4: ")

def printposts(result):
    count = 0
    for post in result.get("articles", []):
        if post.get("title") and post["title"] != "[Removed]":
            count += 1
            print("Title: {}".format(post.get("title", "No title available")))
            description = post.get("description", "No description available")
            if description:
                print("Description: {}".format(description.strip()))
            else:
                print("No description available")
            print("Url: {}".format(post.get("url", "No URL available")))
            print("Author: {}".format(post.get("author", "Unknown author")))
            print("UrlToImage: {}".format(post.get("urlToImage", "No image available")))
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
            sortby = input("Sort By (e.g newer, older, popularity): ")
            try:
                news = getposts(topic, days, sortby)
                printposts(news)
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "2":
            try:
                keyword = input("Enter a country code (e.g., us, gb, in): ")
                news = get_top_headlines(keyword)
                printposts(news)
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "3":
            if news:
                filename = input("Enter a file name (default is news.json): ") 
                if not filename:
                    filename = 'news.json'
                save_news(news, filename)
            else:
                print("There are no recent news searches to save!")
        elif choice == "4":
            print("Exiting .....")
            sys.exit(0)
        else:
            print("Invalid input! Please choose a valid option.")

if __name__ == "__main__":
    clear()
    main()
