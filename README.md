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
patch_manager = patch(app)

# include middleware
patch_manager.include_middleware(MyMiddleware(*args, **kwargs))

```

## Create middleware

```python
from pyrogram_middleware_patch.types import OnUpdateMiddleware


class MyMiddleware(OnUpdateMiddleware):

    # it can be any value you want

    def __init__(self, *args, **kwargs) -> None:
        self.value = value

    # you cannot change the call arguments
    async def __call__(self, update) -> dict:
        
        # do whatever you want
        # need to return dictionary
        return {"my_value_name": my_value}
```


## Handle midleware data

```python

@app.on_message(filters.me)
async def my_commands(client, message, my_value_name):
    print(my_value_name)

```
## Middleware types and updates
```text
middleware - middleware which is called if the update is used
outer middleware - middleware that handles everything even if it wasn't caught by the handler. !!!pay attention to the arguments
```
events and middlewares
```text
on_message - OnMessageMiddleware
on_inline_query - OnInlineQueryMiddleware
on_user_status - OnUserStatusMiddleware
on_disconnect - OnDisconnectMiddleware
on_edited_message - OnEditedMessageMiddleware
on_deleted_messages - OnDeletedMessagesMiddleware
on_chosen_inline_result - OnChosenInlineResultMiddleware
on_chat_member_updated - OnChatMemberUpdatedMiddleware
on_raw_update - OnRawUpdateMiddleware
on_chat_join_request - OnChatJoinRequestMiddleware
on_callback_query - OnCallbackQueryMiddleware
on_poll - OnPoolMiddleware

OnUpdateMiddleware - middleware that reacts to everything
```
everything you can import from
```python
pyrogram_middleware_patch.types
```

## Contributing
Pull requests are welcome. For major changes, please open a question first to discuss what you would like to change.

Be sure to update tests as needed.

more details: https://kotttee.github.io/docs/pyrogram-middleware-patch/

## License
[MIT](https://choosealicense.com/licenses/mit/)