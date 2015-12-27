class GuidGenerator(object):
    def __init__(self):
        pass
    def next_guid(self):
        pass

class SequentialGuidGenerator(object):
    def __init__(self):
        self._next_guid = 0
    def next_guid(self):
        guid = self._next_guid
        self._next_guid += 1
        return guid
