# remecap

Bypasses H-Captcha automatically using yolov5

## Installation

```
pip install remecap
```

## Example

```python
from remecap import AISolver
from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://democaptcha.com/demo-form-eng/hcaptcha.html")
    solver = AISolver(driver)
    solver.start()
```

## Todo

1- Add ReCaptcha
