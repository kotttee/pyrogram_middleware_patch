# pyrogram_patch

pyrogram_middleware_patch is a Python library this is a library that adds middlewares to pyrogram.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install https://kotttee.xyz/dist/pyrogram_middleware_patch.zip
```

# Middlewares

## Usage

```python
from pyrogram import Client
from pyrogram_middleware_patch import patch

# create client
app = Client("my_account", api_id='API_ID', api_hash='API_HASH')

# patch client
patch_manager = patch(app)

# include middleware
patch_manager.include_middleware(MyMiddleware(*args, **kwargs))

```

## Create middleware

```python
from pyrogram_middleware_patch.middlewares.middleware_types import OnUpdateMiddleware
from pyrogram_middleware_patch.middlewares import MiddlewareHelper


class MyMiddleware(OnUpdateMiddleware):

    # it can be any value you want

    def __init__(self, *args, **kwargs) -> None:
        self.value = 'my_value'

    # you cannot change the call arguments
    async def __call__(self, update, middleware_helper: MiddlewareHelper):
        # do whatever you want
        # need to return dictionary
        return await middleware_helper.insert_data('my_value_name', self.value)

    # get_data() - use this method to get the data you saved earlier
    # skip_handler() - use this method to skip the handler
    # middleware_helper.state.state - this way you can get the current state
```
## Using filters 
```python
async def my_filter(_, __, query) -> bool:
    some_data = await query.middleware_helper.get_data('my_value_name')
    await query.middleware_helper.insert_data('some_data', 'some_data' + some_data)
    return True  # False
digit_filter = filters.create(my_filter)
```
## Handle middleware data

```python
@app.on_message(filters.me & digit_filter)
async def my_commands(client, message, my_value_name, some_data):
    print(my_value_name)
```
## Middleware types and updates
```text
middleware - middleware which is called if the update is used
outer middleware - middleware that handles everything even if it wasn't caught by the handler
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
```text
from pyrogram_middleware_patch.middlewares.middleware_types
```

read more about filters on github in examples -> MRE

# Contributing
Pull requests are welcome. For major changes, please open a question first to discuss what you would like to change.

Be sure to update tests as needed.

more details: https://kotttee.xyz/docs/pyrogram-middleware-patch/

github: https://github.com/kotttee/pyrogram_middleware_patch
## License
[MIT](https://choosealicense.com/licenses/mit/)