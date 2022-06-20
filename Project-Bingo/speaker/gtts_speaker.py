from gtts import gTTS
import os


class GTTSpeaker:
    def __init__(self, language="es"):
        self.language = language

    """
    Say a message
    :param message string, Ie. "Hello world"
    """

    def speak(self, message):
        gtts = gTTS(text=message, lang=self.language, slow=False)
        path_audio = "/tmp/wwelcome.mp3"

        gtts.save(path_audio)
        os.system("mpg321 {}".format(path_audio))
