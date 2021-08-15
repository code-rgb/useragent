## Example
```python
import requests
from random import choice

UA_REPO = "https://raw.githubusercontent.com/code-rgb/useragent/main"


def random_ua() -> str:
    browser = choice(("chrome", "firefox", "safari"))
    resp = requests.get(f"{UA_REPO}/{browser}.txt")
    assert resp.status_code == 200
    return choice(resp.text.split("\n"))
```
