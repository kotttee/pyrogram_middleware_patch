from .dispatcher import PatchedDispatcher


class MiddlewarePatchManager:
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher

    def include_middleware(self, middleware: object) -> None:
        self.dispatcher.include_middleware(middleware)

    def include_outer_middleware(self, middleware: object) -> None:
        self.dispatcher.include_outer_middleware(middleware)


def patch(app: object) -> MiddlewarePatchManager:
    """app - instance of your pyrogram client
       returns
       MiddlewarePatchManager instance with methods:
       include_middleware and include_outer_middleware
    """
    app.__delattr__("dispatcher")
    app.dispatcher = PatchedDispatcher(app)
    return MiddlewarePatchManager(app.dispatcher)


