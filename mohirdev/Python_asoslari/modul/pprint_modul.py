from pprint import pprint
import json

filename = "F:\Learn\mohirdev\Python_asoslari\json\/bemor.json"
with open(filename) as f:
    bemor = json.load(f)

# pprint(bemor)
pprint(bemor)

import requests

r = requests.get("https://api.github.com")

# Bu jsonni va kattta fayllarni chiroyli qilib chiqarish uchun
pprint(r.json())