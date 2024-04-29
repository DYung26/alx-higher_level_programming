#!/usr/bin/python3
''' Uses `urllib` to fetch `https://alx-intranet.hbtn.io/status'''
import urllib.request as urllib_req

if __name__ == '__main__':
    with urllib_req.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content_bytes = response.read()
        print("Body response:")
        print(f"    - type: {type(content_bytes)}")
        print(f"    - content: {content_bytes}")
        print(f"    - utf8 content: {content_bytes.decode('utf-8')}")
