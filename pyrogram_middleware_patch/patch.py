from . dispatcher import PatchedDispatcher


def patch(app: object) -> None:
    """app - instance of your pyrogram client"""
    app.__delattr__("dispatcher")
    app.dispatcher = PatchedDispatcher(app)

