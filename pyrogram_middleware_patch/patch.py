from .dispatcher import PatchedDispatcher
from pyrogram import Client


class PatchManager:
    def __init__(self, dispatcher: PatchedDispatcher):
        self.dispatcher = dispatcher

    def include_middleware(self, middleware: 'PatchMiddleware') -> None:
        self.dispatcher.pyrogram_middleware_patch_include_middleware(middleware)

    def include_outer_middleware(self, middleware: 'PatchMiddleware') -> None:
        self.dispatcher.pyrogram_middleware_patch_include_outer_middleware(middleware)


def patch(app: Client) -> PatchManager:
    """app - instance of your pyrogram client
       returns
       MiddlewarePatchManager instance with methods:
       include_middleware and include_outer_middleware
    """
    app.__delattr__("dispatcher")
    app.dispatcher = PatchedDispatcher(app)
    return PatchManager(app.dispatcher)


