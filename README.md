# pyrogram_middleware_patch

pyrogram_middleware_patchis a Python library this is a library that adds middlewares to pyrogram.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install https://kotttee.github.io/dist/pyrogram_middleware_patch.zip
```

## Usage

```python
from pyrogram_middleware_patch import patch

# create client
app = Client("my_account", api_id=api_id, api_hash=api_hash)

# patch client
patch(app)

# include middleware
app.dispatcher.include_middleware(MyMiddleware(*args, **kwargs))

```

## Create middleware

```python
class MyMiddleware:

    # it can be any value you want

    def __init__(self, *args, **kwargs) -> None:
        self.value = value

    # you cannot change the call arguments
    def __call__(self, update) -> dict:
        
        # do whatever you want
        # need to return dictionary
        return {"my_value_name": my_value}
```


## handle midleware data

```python

@app.on_message(filters.me)
async def my_commands(client, message, my_value_name):
    print(my_value_name)

# if you don't get any arguments, an error will be thrown.
# so please use **kwargs now, it will be fixed in future updates
# more details: https://kotttee.github.io/docs/pyrogram-middleware-patch/


@app.on_message(filters.me)
async def my_commands(client, message):
    # error


@app.on_message(filters.me)
async def my_commands(client, message, *kw):
    # ok!

```

## Contributing
Pull requests are welcome. For major changes, please open a question first to discuss what you would like to change.

Be sure to update tests as needed.

more details: https://kotttee.github.io/docs/pyrogram-middleware-patch/

## License
[MIT](https://choosealicense.com/licenses/mit/)