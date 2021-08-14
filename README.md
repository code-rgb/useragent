# useragent

## Usage
```python
import requests
from random import choice

def random_ua() -> str:
    browser = choice(("chrome", "firefox", "safari"))
    url = f"https://raw.githubusercontent.com/code-rgb/useragent/main/{browser}.txt"
    ua_list = requests.get(url).text.split("\n")
    return choice(ua_list)
```
