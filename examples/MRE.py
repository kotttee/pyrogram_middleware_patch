from pyrogram import Client, filters
from pyrogram_middleware_patch import patch
from pyrogram_middleware_patch.middlewares.middleware_types import OnMessageMiddleware
from pyrogram_middleware_patch.middlewares import MiddlewareHelper
from pyrogram.types import Message

SESSION_NAME = "bot"
API_ID = 8
API_HASH = "7245de8e747a0d6fbe11f7cc14fcc0bb"
BOT_TOKEN = ""

"""MIDDLEWARES"""


class CheckDigitMiddleware(OnMessageMiddleware):

    def __init__(self) -> None:
        pass

    # you cannot change the call arguments
    async def __call__(self, message: Message, middleware_helper: MiddlewareHelper):
        return await middleware_helper.insert_data('is_digit', message.text.isdigit())


class CheckIgnoreMiddleware(OnMessageMiddleware):
    def __init__(self, ignore: bool) -> None:
        self.ignore = ignore  # it can be any value you want

    # you cannot change the call arguments
    async def __call__(self, message: Message, middleware_helper: MiddlewareHelper):
        if self.ignore:
            pass
        else:
            if not await middleware_helper.get_data('is_digit'):
                return await middleware_helper.skip_handler()


"""APP"""

app = Client(...)
patched = patch(app)

#patched.include_middleware(CheckDigitMiddleware())
#patched.include_middleware(CheckIgnoreMiddleware(False))

# you can use a middlewares or make your own filter
# work just with on_message

#async def my_filter(_, __, query) -> bool:
    #await query.middleware_helper.insert_data('is_digit', query.text.isdigit())
    #return True  # False
#digit_filter = filters.create(my_filter)

# combine outer_middleware and filter

patched.include_outer_middleware(CheckDigitMiddleware())


async def my_filter(_, __, query) -> bool:
    # call handler if message.text contains only digits
    return await query.middleware_helper.get_data('is_digit')
    # note that it will still be transferred to the handler ... since it was implanted by the middleware before
digit_filter = filters.create(my_filter)


@app.on_message(filters.private & digit_filter)
async def process_1(client: Client, message, is_digit: bool):
    print(is_digit)


app.run()
