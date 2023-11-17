import pytest
from television import Television

class TestTelevision:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def test_init(self):
        self.tv = Television()
        self.tv.__init__()
        assert self.tv.__str__() == f"Power = False, Channel = {self.MIN_CHANNEL}, Volume = {self.MIN_VOLUME}"
    def test_power(self):
        self.tv = Television()
        self.tv.__init__()
        self.tv.power()
        assert self.tv.__str__() == f"Power = True, Channel = {self.MIN_CHANNEL}, Volume = {self.MIN_VOLUME}"
        self.tv.power()
        assert self.tv.__str__() == f"Power = False, Channel = {self.MIN_CHANNEL}, Volume = {self.MIN_VOLUME}"
    def test_mute(self):
        self.tv = Television()
        self.tv.__init__()
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        assert self.tv.__str__() == f"Power = True, Channel = {self.MIN_CHANNEL}, Volume = 0"
        self.tv1 = Television()
        self.tv1.__init__()
        self.tv1.power()
        self.tv1.mute()
        self.tv1.mute()
        assert self.tv1.__str__() == f"Power = True, Channel = {self.MIN_CHANNEL}, Volume = 0"
        self.tv2 = Television()
        self.tv2.__init__()
        self.tv2.mute()
        assert self.tv2.__str__() == f"Power = False, Channel = {self.MIN_CHANNEL}, Volume = 0"
        self.tv3 = Television()
        self.tv3.__init__()
        self.tv3.mute()
        self.tv3.mute()
        assert self.tv3.__str__() == f"Power = False, Channel = {self.MIN_CHANNEL}, Volume = 0"
    def test_channel_up(self):
        self.tv = Television()
        self.tv.__init__()
        self.tv.channel_up()
        assert self.tv.__str__() == f"Power = False, Channel = {self.MIN_CHANNEL}, Volume = 0"
        self.tv2 = Television()
        self.tv2.__init__()
        self.tv2.power()
        self.tv2.channel_up()
        assert self.tv2.__str__() == f"Power = True, Channel = 1, Volume = 0"
        self.tv3 = Television()
        self.tv3.__init__()
        self.tv3.power()
        self.tv3.channel_up()
        self.tv3.channel_up()
        assert self.tv3.__str__() == f"Power = True, Channel = 2, Volume = 0"
        self.tv4 = Television()
        self.tv4.__init__()
        self.tv4.power()
        self.tv4.channel_up()
        self.tv4.channel_up()
        self.tv4.channel_up()
        self.tv4.channel_up()
        assert self.tv4.__str__() == f"Power = True, Channel = {self.MIN_CHANNEL}, Volume = 0"
    def test_channel_down(self):
        self.tv = Television()
        self.tv.__init__()
        self.tv.channel_down()
        assert self.tv.__str__() == f"Power = False, Channel = {self.MIN_CHANNEL}, Volume = {self.MIN_VOLUME}"
        self.tv2 = Television()
        self.tv2.__init__()
        self.tv2.power()
        self.tv2.channel_down()
        assert self.tv2.__str__() == f"Power = True, Channel = 3, Volume = {self.MIN_VOLUME}"
    def test_volume_up(self):
        self.tv = Television()
        self.tv.__init__()
        self.tv.volume_up()
        assert self.tv.__str__() == f"Power = False, Channel = {self.MIN_CHANNEL}, Volume = {self.MIN_VOLUME}"
        self.tv1 = Television()
        self.tv1.__init__()
        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.__str__() == f"Power = True, Channel = {self.MIN_CHANNEL}, Volume = 1"
        self.tv2 = Television()
        self.tv2.__init__()
        self.tv2.power()
        self.tv2.mute()
        self.tv2.volume_up()
        assert self.tv2.__str__() == f"Power = True, Channel = {self.MIN_CHANNEL}, Volume = 1"
        self.tv3 = Television()
        self.tv3.__init__()
        self.tv3.power()
        self.tv3.volume_up()
        self.tv3.volume_up()
        self.tv3.volume_up()
        assert self.tv3.__str__() == f"Power = True, Channel = {self.MIN_CHANNEL}, Volume = 2"
    def test_volume_down(self):
        self.tv = Television()
        self.tv.__init__()
        self.tv.volume_down()
        assert self.tv.__str__() == f"Power = False, Channel = {self.MIN_CHANNEL}, Volume = 0"
        self.tv2 = Television()
        self.tv2.__init__()
        self.tv2.power()
        self.tv2.volume_up()
        self.tv2.volume_up()
        self.tv2.volume_down()
        assert self.tv2.__str__() == f"Power = True, Channel = {self.MIN_CHANNEL}, Volume = 1"
        self.tv3 = Television()
        self.tv3.__init__()
        self.tv3.power()
        self.tv3.volume_up()
        self.tv3.volume_up()
        self.tv3.mute()
        self.tv3.volume_down()
        assert self.tv3.__str__() == f"Power = True, Channel = {self.MIN_CHANNEL}, Volume = 1"
        self.tv4 = Television()
        self.tv4.__init__()
        self.tv4.power()
        self.tv4.volume_down()
        self.tv4.volume_down()
        assert self.tv4.__str__() == f"Power = True, Channel = {self.MIN_CHANNEL}, Volume = {self.MIN_VOLUME}"































