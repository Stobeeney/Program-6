#Program by Daniel Rein Cosare
#PROGRAM #6

class TV:
    def __init__(self):
        self.channel = 1
        self.volumeLevel = 1
        self.on = False

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False

    def getChannel(self):
        return self.channel

    def setChannel(self, channel):
        if 1 <= channel <= 120:
            self.channel = channel

    def getVolume(self):
        return self.volumeLevel

    def setVolume(self, volumeLevel):
        if 1 <= volumeLevel <= 7:
            self.volumeLevel = volumeLevel

    def channelUp(self):
        if self.channel < 120:
            self.channel += 1

    def channelDown(self):
        if self.channel > 1:
            self.channel -= 1

    def volumeUp(self):
        if self.volumeLevel < 7:
            self.volumeLevel += 1

    def volumeDown(self):
        if self.volumeLevel > 1:
            self.volumeLevel -= 1