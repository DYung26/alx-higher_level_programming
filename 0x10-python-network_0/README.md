# 0x10-python-network_0

This repository contains 10 tasks for the Python Network #0 project, covering concepts such as cURL, HTTP and HTTPS protocols, headers, and web scraping.

## Tasks
Here are the links to all the tasks in this repository:

| Task | Description |
| --- | --- |
| [0-body_size.sh](./0-body_size.sh) | Bash script that takes in a URL, sends a request to that URL, and displays the size of the response body in bytes. |
| [1-body.sh](./1-body.sh) | Bash script that takes in a URL, sends a GET request to that URL, and displays the response body. |
| [2-delete.sh](./2-delete.sh) | Bash script that sends a DELETE request to a given URL and displays the response body. |
| [3-methods.sh](./3-methods.sh) | Bash script that takes in a URL and displays all HTTP methods the server will accept for that URL. |
| [4-header.sh](./4-header.sh) | Bash script that takes in a URL, sends a GET request to that URL, and displays the response body.  |
| [5-post_params.sh](./5-post_params.sh) | Bash script that takes in a URL, sends a POST request to that URL, and displays the response body. |
| [6-peak.py](./6-peak.py) | Python function that finds a peak in a list of unsorted integers. |
| [100-status_code.sh](./100-status_code.sh) | Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response. |
| [101-post_json.sh](./101-post_json.sh) | Bash script that sends a JSON POST request to a URL passed as an argument, and displays the response body. |
| [102-catch_me.sh](./102-catch_me.sh) | Bash script that makes a request to 0.0.0.0:5000/catch_me to return You got me! response. |

Each task comes with a detailed description of what is expected and how it should be achieved.

### Task 0: 0-body_size.sh
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the response body in bytes. The script should display only the size of the response body, nothing else.

### Task 1: 1-body.sh
Write a Bash script that takes in a URL, sends a GET request to that URL, and displays the response body. The script should display only the body of the response, nothing else.

### Task 2: 2-delete.sh
Write a Bash script that sends a DELETE request to a given URL and displays the response body. The script should display only the body of the response, nothing else.

### Task 3: 3-methods.sh
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept for that URL.

### Task 4: 4-header.sh
Write a Bash script that takes in a URL, sends a GET request to that URL, and displays the response body. The script should also send a header variable `X-HolbertonSchool-User-Id` with a value of `98`.

### Task 5: 5-post_params.sh
Write a Bash script that takes in a URL, sends a POST request to that URL, and displays the response body. The script should also set the variables `email` to `hr@holbertonschool.com` and `subject` to `I will always be here for PLD`.

### Task 6: 6-peak.py
Write a function `def find_peak(list_of_integers):` that finds a peak in a list of unsorted integers. A peak is an element that is greater than its neighbors. For example, in the list `[1, 2, 4, 6, 3]`, `6` is a peak. The function should return the peak element if it exists, otherwise return `None`. The function should have a time complexity of `O(log(n))`.

### Task 100: 100-status_code.sh
Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.

### Task 101: 101-post_json.sh
Write a Bash script that sends a JSON POST request to a URL passed as an argument, and displays the response body.

### Task 102: 102-catch_me.sh
Write a Bash script that makes a request to `0.0.0.0:5000/catch_me` and causes the server to respond with a message containing `You got me!`. The response should be displayed.

## Usage
The bash scripts in this repository can be run like so:

```bash
./script.sh [URL]
```

For example, to run the `0-body_size.sh` script:

```bash
./0-body_size.sh http://example.com
```

## Contributing
To contribute to this project, follow these steps:

1. Fork this repository.
2. Create a new branch with your feature: `git checkout -b my-feature`.
3. Commit your changes: `git commit -m "feat: add new feature"`.
4. Push to the branch: `git push origin my-feature`.
5. Submit a pull request with your changes.

