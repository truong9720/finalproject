import json
import sys
import pytest
import os
from project import getposts, get_top_headlines, printposts, save_news


def get_test_data():
    return getposts("technology", "2025-02-01", "popularity")


def test_getposts():
    result = get_test_data()
    assert isinstance(result, dict)
    assert len(result["articles"]) > 0


def test_get_top_headlines():
    result = get_top_headlines("trump")
    assert isinstance(result, dict)
    assert "articles" in result


def test_printposts(capsys):
    test_data = get_test_data()
    printposts(test_data)
    captured = capsys.readouterr()

    assert "Title" in captured.out
    assert "Description" in captured.out
    assert "Url" in captured.out


def test_save_news():
    filename = "test_news.json"
    test_data = get_test_data()
    save_news(test_data, filename)

    assert os.path.exists(filename)

    with open(filename, 'r', encoding='utf-8') as f:
        saved_data = json.load(f)
    assert len(saved_data) > 0

    assert "title" in saved_data[0]
    assert "description" in saved_data[0]

    assert "title" in saved_data[0]
    assert "description" in saved_data[0]
    assert "url" in saved_data[0]
    assert "author" in saved_data[0]
    assert "urlToImage" in saved_data[0]