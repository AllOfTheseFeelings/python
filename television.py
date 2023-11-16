#Sterling Arnold Lab 12
class Television(object):
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self):
        self.status = False
        self.muted = False
        self.volume = self.MIN_VOLUME
        self.channel = self.MIN_CHANNEL
    def power(self):
        self.status = not self.status #Really proud of this one line of code
    def mute(self):
        if self.status == True: self.muted = not self.muted
    def channel_up(self):
        if self.status == True:
            if self.channel < self.MAX_CHANNEL: 
                self.channel = self.channel + 1
            else: 
                self.channel = self.MIN_CHANNEL
    def channel_down(self):
        if self.status == True:
            if self.channel > self.MIN_CHANNEL: 
                self.channel = self.channel - 1
            else: 
                self.channel = self.MAX_CHANNEL
    def volume_up(self):
        if self.status == True:
            if self.muted == False:
                if self.volume < self.MAX_VOLUME: 
                    self.volume = self.volume + 1
            else:
                self.muted = False
                self.volume = self.volume + 1
    def volume_down(self):
        if self.status == True:
            if self.muted == False:
                if self.volume > self.MIN_VOLUME: 
                    self.volume = self.volume - 1
            else: 
                self.muted = False
                self.volume = self.volume - 1
    def __str__(self):
        if self.muted == False:
            return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}'
        else: return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.MIN_VOLUME}'
