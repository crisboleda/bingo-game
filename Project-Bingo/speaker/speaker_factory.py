from speaker.gtts_speaker import GTTSpeaker


class SpeakerFactory:
    def __init__(self, speaker_name):
        self.speaker_name = speaker_name.upper()

    def get_speaker(self):
        if self.speaker_name == "WINDOWS":
            pass
        elif self.speaker_name == "GTTS":
            return GTTSpeaker(language="es")
