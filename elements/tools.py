class Compare(object):
    def __init__(self):
        pass
    
    def checkPos(self, target):
        if (target.isnumeric() and (int(target) >= 0 and int(target) <= 9)):
            return True
        else:
            return False
    def checkVoid(self, target):
        if (len(target) == 0):
            return (False)
        else:
            return (True)

    def checkNum(self, target):
        if (target.isnumeric()):
            return (True)
        else:
            return (False)