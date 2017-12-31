class Collar:
    def __init__(self, name, phoneNum, address):
        self.name = name
        self.phoneNum = phoneNum
        self.address = address

    def getInfo(self):
        print("Owner Name    : {}".format(self.name))
        print("Contact Number: {}".format(self.phoneNum))
        print("Address       : {}".format(self.address))