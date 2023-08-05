"""
Main interface for polly service literal definitions.

Usage::

    ```python
    from mypy_boto3_polly.literals import DescribeVoicesPaginatorName

    data: DescribeVoicesPaginatorName = "describe_voices"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeVoicesPaginatorName",
    "Engine",
    "Gender",
    "LanguageCode",
    "ListLexiconsPaginatorName",
    "ListSpeechSynthesisTasksPaginatorName",
    "OutputFormat",
    "SpeechMarkType",
    "TaskStatus",
    "TextType",
    "VoiceId",
)


DescribeVoicesPaginatorName = Literal["describe_voices"]
Engine = Literal["neural", "standard"]
Gender = Literal["Female", "Male"]
LanguageCode = Literal[
    "arb",
    "cmn-CN",
    "cy-GB",
    "da-DK",
    "de-DE",
    "en-AU",
    "en-GB",
    "en-GB-WLS",
    "en-IN",
    "en-US",
    "es-ES",
    "es-MX",
    "es-US",
    "fr-CA",
    "fr-FR",
    "hi-IN",
    "is-IS",
    "it-IT",
    "ja-JP",
    "ko-KR",
    "nb-NO",
    "nl-NL",
    "pl-PL",
    "pt-BR",
    "pt-PT",
    "ro-RO",
    "ru-RU",
    "sv-SE",
    "tr-TR",
]
ListLexiconsPaginatorName = Literal["list_lexicons"]
ListSpeechSynthesisTasksPaginatorName = Literal["list_speech_synthesis_tasks"]
OutputFormat = Literal["json", "mp3", "ogg_vorbis", "pcm"]
SpeechMarkType = Literal["sentence", "ssml", "viseme", "word"]
TaskStatus = Literal["completed", "failed", "inProgress", "scheduled"]
TextType = Literal["ssml", "text"]
VoiceId = Literal[
    "Aditi",
    "Amy",
    "Astrid",
    "Bianca",
    "Brian",
    "Camila",
    "Carla",
    "Carmen",
    "Celine",
    "Chantal",
    "Conchita",
    "Cristiano",
    "Dora",
    "Emma",
    "Enrique",
    "Ewa",
    "Filiz",
    "Geraint",
    "Giorgio",
    "Gwyneth",
    "Hans",
    "Ines",
    "Ivy",
    "Jacek",
    "Jan",
    "Joanna",
    "Joey",
    "Justin",
    "Karl",
    "Kendra",
    "Kevin",
    "Kimberly",
    "Lea",
    "Liv",
    "Lotte",
    "Lucia",
    "Lupe",
    "Mads",
    "Maja",
    "Marlene",
    "Mathieu",
    "Matthew",
    "Maxim",
    "Mia",
    "Miguel",
    "Mizuki",
    "Naja",
    "Nicole",
    "Olivia",
    "Penelope",
    "Raveena",
    "Ricardo",
    "Ruben",
    "Russell",
    "Salli",
    "Seoyeon",
    "Takumi",
    "Tatyana",
    "Vicki",
    "Vitoria",
    "Zeina",
    "Zhiyu",
]
