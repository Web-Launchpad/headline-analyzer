from dataclasses import dataclass
import json

class JSONSerializable():
    def __str__(self):
        return json.dumps(self.__dict__, indent = 2, default = lambda o:o.__dict__)

    def __repr__(self):
        return self.__str__(self)


@dataclass
class HeadlineStats(JSONSerializable):
    """Stats data"""

    character_count: int
    word_count: int


