#!/usr/bin/python3
''' Uses `urllib` to fetch `https://alx-intranet.hbtn.io/status'''
import urllib.request as urllib_req

if __name__ == '__main__':
    with urllib_req.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content_bytes = response.read()
        print(f"""Body response:
    - type: {type(content_bytes)}
    - content: {content_bytes}
    - utf8 content: {content_bytes.decode('utf-8')}""")
