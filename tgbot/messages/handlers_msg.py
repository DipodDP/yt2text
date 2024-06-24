from enum import Enum


class AdminHandlerMessages(str, Enum):
    GREETINGS = "Hello, admin! It's yt@text bot.\n Press /stop to stop bot\n"
    STOPPING = 'Stopping bot...'


class UserHandlerMessages(str, Enum):
    GREETINGS = "Hello! Send a link to YouTube video to get transcription"
    HELP = "Try some commands from menu"
