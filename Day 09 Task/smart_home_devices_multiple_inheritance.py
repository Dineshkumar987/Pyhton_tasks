class WiFiDevice:
    def wifi(self):
        print("WiFi Connected")


class VoiceAssistant:
    def voice(self):
        print("Voice Assistant Enabled")


class SmartSpeaker(WiFiDevice, VoiceAssistant):
    def display(self):
        print("Smart Speaker Ready")


s = SmartSpeaker()
s.wifi()
s.voice()
s.display()