#!/usr/bin/python3
'''sends a request to ther URL and displays the value of the `X-Request-Id` variable found in the header of the response.'''

import urllib.request as urllib_req
import sys
if __name__ == '__main__':
    with urllib_req.urlopen(f'{sys.argv[1]}') as response:
        http_response = response.getheader('X-Request-Id')
        print(http_response)
