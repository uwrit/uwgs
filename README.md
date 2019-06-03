# uwgs
Python3 Client Library for UW Groups API v3

### Functionality
At the moment, this library provides read-only functionality for:
- [Get Group By Id](https://iam-tools.u.washington.edu/apis/gws/#/Groups/getGroup)
- [All Read Membership Endpoints (except history)](https://iam-tools.u.washington.edu/apis/gws/#/Membership)
- [Search](https://iam-tools.u.washington.edu/apis/gws/#/Searches/get_search)

```python
import uwgs
from collections import namedtuple
import os
import json

Config = namedtuple('Config', ['client_cert', 'client_key', 'url'])

def load_config():
    cwd = os.path.dirname(os.path.abspath(__file__))
    fp = os.path.join(cwd, 'uwgs.json')
    with open(fp, 'r') as f:
        data = json.load(f)
        cfg = Config(data['client_cert'], data['client_key'], data['url'])
        return cfg
    

def cli():
    cfg = load_config()
    client = uwgs.Client(cfg.client_cert, cfg.client_key, cfg.url)
    
    payload = client.search(name='<group_prefix>*')
    if payload.ok:
        for group in payload.data['data']:
            first = client.get_members(group['id'])
            print(first)
            break

if __name__ == "__main__":
    cli()
```