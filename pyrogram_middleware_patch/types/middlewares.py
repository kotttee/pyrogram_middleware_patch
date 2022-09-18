from pyrogram.handlers.message_handler import MessageHandler
from pyrogram.handlers.poll_handler import PollHandler
from pyrogram.handlers.disconnect_handler import DisconnectHandler
from pyrogram.handlers.inline_query_handler import InlineQueryHandler
from pyrogram.handlers.callback_query_handler import CallbackQueryHandler
from pyrogram.handlers.chat_join_request_handler import ChatJoinRequestHandler
from pyrogram.handlers.raw_update_handler import RawUpdateHandler
from pyrogram.handlers.chat_member_updated_handler import ChatMemberUpdatedHandler
from pyrogram.handlers.chosen_inline_result_handler import ChosenInlineResultHandler
from pyrogram.handlers.deleted_messages_handler import DeletedMessagesHandler
from pyrogram.handlers.edited_message_handler import EditedMessageHandler
from pyrogram.handlers.user_status_handler import UserStatusHandler


class OnUpdateMiddleware:
    """middleware for all"""

    def __eq__(self, other) -> bool:
        return True


class OnEditedMessageMiddleware:
    """middleware for on_edited_message"""

    def __eq__(self, other) -> bool:
        if type(other) == EditedMessageHandler:
            return True
        return False


class OnUserStatusMiddleware:
    """middleware for on_user_status"""

    def __eq__(self, other) -> bool:
        if type(other) == UserStatusHandler:
            return True
        return False


class OnRawUpdateMiddleware:
    """middleware for on_raw_update"""

    def __eq__(self, other) -> bool:
        if type(other) == RawUpdateHandler:
            return True
        return False


class OnChosenInlineResultMiddleware:
    """middleware for on_chosen_inline_result"""

    def __eq__(self, other) -> bool:
        if type(other) == ChosenInlineResultHandler:
            return True
        return False


class OnDeletedMessagesMiddleware:
    """middleware for on_deleted_messages"""

    def __eq__(self, other) -> bool:
        if type(other) == DeletedMessagesHandler:
            return True
        return False


class OnChatMemberUpdatedMiddleware:
    """middleware for on_chat_member_updated"""

    def __eq__(self, other) -> bool:
        if type(other) == ChatMemberUpdatedHandler:
            return True
        return False


class OnChatJoinRequestMiddleware:
    """middleware for on_chat_join_request"""

    def __eq__(self, other) -> bool:
        if type(other) == ChatJoinRequestHandler:
            return True
        return False


class OnCallbackQueryMiddleware:
    """middleware for on_callback_query"""

    def __eq__(self, other) -> bool:
        if type(other) == CallbackQueryHandler:
            return True
        return False


class OnInlineQueryMiddleware:
    """middleware for on_inline_query"""

    def __eq__(self, other) -> bool:
        if type(other) == InlineQueryHandler:
            return True
        return False


class OnDisconnectMiddleware:
    """middleware for on_disconnect"""

    def __eq__(self, other) -> bool:
        if type(other) == DisconnectHandler:
            return True
        return False


class OnMessageMiddleware:
    """middleware for on_message"""

    def __eq__(self, other) -> bool:
        if type(other) == MessageHandler:
            return True
        return False


class OnPoolMiddleware:
    """middleware for on_pool"""

    def __eq__(self, other) -> bool:
        if type(other) == PollHandler:
            return True
        return False
