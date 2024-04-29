#!/usr/bin/python3
''' Uses `urllib` to fetch `https://alx-intranet.hbtn.io/status'''
import urllib.request as urllib_req

if __name__ == '__main__':
    with urllib_req.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content_bytes = response.read()
        print("Body response:")
        print(f"\t- type: {type(content_bytes)}")
        print(f"\t- content: {content_bytes}")
        print(f"\t- utf8 content: {content_bytes.decode('utf-8')}")
