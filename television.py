#Sterling Arnold Lab 12
class Television(object):
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self):
        """
        initialized object TV that has states such as status, muted, volume and channel
        """
        self.status = False
        self.muted = False
        self.volume = self.MIN_VOLUME
        self.channel = self.MIN_CHANNEL
    def power(self):
        '''
        This function turns on and off the television object
        '''
        self.status = not self.status #Really proud of this one line of code
    def mute(self):
        '''
        This function turns on and off the television object
        '''
        if self.status == True: self.muted = not self.muted
    def channel_up(self):
        '''
        This function turns the channel of the TV up, if at max it goes to the min channel
        '''
        if self.status == True:
            if self.channel < self.MAX_CHANNEL: 
                self.channel = self.channel + 1
            else: 
                self.channel = self.MIN_CHANNEL
    def channel_down(self):
        '''
        This function turns the channel of the TV down, if at min it goes to the max channel
        '''
        if self.status == True:
            if self.channel > self.MIN_CHANNEL: 
                self.channel = self.channel - 1
            else: 
                self.channel = self.MAX_CHANNEL
    def volume_up(self):
        '''
        This function turns the volume of the TV up and unmutes it if the TV is muted
        '''
        if self.status == True:
            if self.muted == False:
                if self.volume < self.MAX_VOLUME: 
                    self.volume = self.volume + 1
            else:
                self.muted = False
                self.volume = self.volume + 1
    def volume_down(self):
        '''
        This function turns the volume of the TV down and unmutes it if the TV is muted
        '''
        if self.status == True:
            if self.muted == False:
                if self.volume > self.MIN_VOLUME: 
                    self.volume = self.volume - 1
            else: 
                self.muted = False
                self.volume = self.volume - 1
    def __str__(self):
        '''
        This function turns on and off the television object
        :return: String of the different states of the TV
        '''
        if self.muted == False:
            return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}'
        else: return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.MIN_VOLUME}'
