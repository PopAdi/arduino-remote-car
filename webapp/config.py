class serverInfo(object):
    host = "192.168.0.105"
    port = 80

    @classmethod
    def getHost(self):
        return self.host

    @classmethod
    def getPort(self):
        return self.port


class BTConfig(object):
    channel = 1
    timeout = 5

    @classmethod
    def getChannel(self):
        return self.channel

    @classmethod
    def getTimeout(self):
        return self.timeout
