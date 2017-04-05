# -*- coding: utf-8 -*-
import urllib.request


def get_webpage(url):
    print("Getting url %s" % url)
    with urllib.request.urlopen(url) as f:
        print(f.getcode())


def print_digit(digit):
    print(str(digit))


if __name__ == '__main__':
    print_digit(1)
    print_digit(2)
    get_webpage('http://python.org/')
    print_digit(4)
    print_digit(5)
