from asyncio.windows_events import NULL
import uuid


class Player:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.points = 0
        self.lastPoints = [0, 0]
        self.rank = 9999999999

    def havePanality(self):
        print(self.lastPoints[0], self.lastPoints[1])
        if self.lastPoints[0] == 1 and self.lastPoints[1] == 1:
            return True
        return False

    def haveBonusChance(self):
        if self.lastPoints[1] == 6:
            return True
        return False

    def addPoint(self, point):
        self.points = self.points + point
        self.lastPoints[0] = self.lastPoints[1]
        self.lastPoints[1] = point
