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



| Param             | Explanation                                                  |
| ----------------- | ------------------------------------------------------------ |
| key               | name of environment variable.                                |
| default           | Optional - default value if key is not present in environment |
| return_type       | Optional - specify return_type.                              |
| list_element_type | Optional - cast/parse each element of a list with provided callable. Only used if the setting is a list. |

​        If key is not present in environment, and there is not provided a default value,
​        None will be returned.

       ## Guidelines for settings in Environment
​        A couple of conventions exist when designing
​        environment variables for settings.

         1. **All values are stored as strings in the environment variable**
                  2. Bools are encoded as one of "1", "True" or "true" if True,
            all other values are interpreted as False
         
   2. **Lists are encoded as a comma separated string**
      in example:  "a,b,c,   d"
  (intentionally put whitespace in there. It is allowed)
        

   3. **Default Values are preffered to be set to the same type as the setting.**

  The type of the default value implicitly sets the datatype of the env var.
  May be overriden by setting `return_type` explicitly.

  * `list` -> `[]`, 
  * `str` -> `''`
  *  `int` -> `0` 
  * `bool` -> `True` or `False`