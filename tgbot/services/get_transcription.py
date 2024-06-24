import re

from betterlogging import logging
from youtube_transcript_api import YouTubeTranscriptApi

logger = logging.getLogger(__name__)


def get_id_from_link(url):
    """
    Extracts the video ID from a YouTube URL.

    Parameters:
    url (str): The YouTube URL.

    Returns:
    str: The video ID if found, else None.
    """
    # Define regular expressions for different types of YouTube URLs
    patterns = [
        r"(?:https?:\/\/)?(?:www\.)?youtu\.be\/([a-zA-Z0-9_-]{11})",  # youtu.be/<id>
        r"(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([a-zA-Z0-9_-]{11})",  # youtube.com/watch?v=<id>
        r"(?:https?:\/\/)?(?:www\.)?youtube\.com\/embed\/([a-zA-Z0-9_-]{11})",  # youtube.com/embed/<id>
        r"(?:https?:\/\/)?(?:www\.)?youtube\.com\/v\/([a-zA-Z0-9_-]{11})",  # youtube.com/v/<id>
        r"(?:https?:\/\/)?(?:www\.)?youtube\.com\/.+\?v=([a-zA-Z0-9_-]{11})",  # youtube.com/anything_else?v=<id>
    ]

    for pattern in patterns:
        match = re.match(pattern, url)
        if match:
            return match.group(1)

    return None


async def get_transcription(video_id: str):
    """
    Getting transcript by video ID.

    Parameters:
    url (str): The YouTube URL.

    Returns:
    str: transcription if video found, else None.
    """

    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=("ru",))
    transcript_text = " ".join([chunck.get("text") for chunck in transcript])

    return transcript_text
