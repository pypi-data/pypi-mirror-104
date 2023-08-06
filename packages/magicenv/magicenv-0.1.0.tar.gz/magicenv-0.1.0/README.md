# magicenv
Simple way to parse common datatypes from env vars.


# Setup

```bash
pip install magicenv
```

# Usage
```python
from magicenv import env

DB_HOST = env('DB_HOST', "localhost:1234")              # string var
DB_NUM_TRANSACTIONS = env('DB_NUM_TRANSACTIONS', 1234)  # int var
ENABLE_FEATURE_X = env('ENABLE_FEATURE_X', True)  # bool var

DB_SERVERS = env('DB_SERVERS', ['server1', "server2"])  # interprets a comma separated string as a list

```