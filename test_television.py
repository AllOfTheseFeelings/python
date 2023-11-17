import pytest
from television import *

class TestTelevision:

    def test_power():
        '''Test the power method of the Television class'''
        ttvp = Television()
        ttvp.power()
        assert ttvp.str() == 'Power = [True], Channel = [0], Volume = [0]'
        ttvp.power()
        assert ttvp.str() == 'Power = [False], Channel = [0], Volume = [0]'
    def test_mute():
        '''Test the mute method of the Television class'''
        ttvm = Television()
        ttvm.mute()
        assert ttvm.str() == 'Power = [False], Channel = [0], Volume = [0]'
        ttvm.power()
        ttvm.mute()
        assert ttvm.str() == 'Power = [True], Channel = [0], Volume = [0]'
    def test_channel_up():
        '''Test the channel_up method of the Television class'''
        ttvcu = Television()
        ttvcu.channel_up()
        assert ttvcu.str() == 'Power = [False], Channel = [0], Volume = [0]'
        ttvcu.power()
        ttvcu.channel_up()
        assert ttvcu.str() == 'Power = [True], Channel = [1], Volume = [0]'
        ttvcu.channel_up()
        assert ttvcu.str() == 'Power = [True], Channel = [2], Volume = [0]'
        ttvcu.channel_up()
        assert ttvcu.str() == 'Power = [True], Channel = [3], Volume = [0]'
        ttvcu.channel_up()
        assert ttvcu.str() == 'Power = [True], Channel = [0], Volume = [0]'
    def test_channel_down():
        '''Test the channel_down method of the Television class'''
        ttvcd = Television()
        ttvcd.channel_down()
        assert ttvcd.str() == 'Power = [False], Channel = [0], Volume = [0]'
        ttvcd.power()
        ttvcd.channel_down()
        assert ttvcd.str() == 'Power = [True], Channel = [3], Volume = [0]'
        ttvcd.channel_down()
        assert ttvcd.str() == 'Power = [True], Channel = [2], Volume = [0]'
        ttvcd.channel_down()
        assert ttvcd.str() == 'Power = [True], Channel = [1], Volume = [0]'
        ttvcd.channel_down()
        assert ttvcd.str() == 'Power = [True], Channel = [0], Volume = [0]'
    def test_volume_up():
        '''Test the volume_up method of the Television class'''
        ttvvu = Television()
        ttvvu.volume_up()
        assert ttvvu.str() == 'Power = [False], Channel = [0], Volume = [0]'
        ttvvu.power()
        ttvvu.volume_up()
        assert ttvvu.str() == 'Power = [True], Channel = [0], Volume = [1]'
        ttvvu.volume_up()
        assert ttvvu.str() == 'Power = [True], Channel = [0], Volume = [2]'
        ttvvu.volume_up()
        assert ttvvu.str() == 'Power = [True], Channel = [0], Volume = [2]'
    def test_volume_down():
        '''Test the volume_down method of the Television class'''
        ttvvd = Television()
        ttvvd.volume_down()
        assert ttvvd.str() == 'Power = [False], Channel = [0], Volume = [0]'
        ttvvd.power()
        ttvvd.volume_down()
        assert ttvvd.str() == 'Power = [True], Channel = [0], Volume = [0]'
        ttvvd.volume_up()
        ttvvd.volume_up()
        ttvvd.volume_down()
        assert ttvvd.str() == 'Power = [True], Channel = [0], Volume = [1]'
        ttvvd.volume_down()
        assert ttvvd.str() == 'Power = [True], Channel = [0], Volume = [0]'
        