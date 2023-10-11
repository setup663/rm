from cpc import Pc
from ctv import Tv
from csofa import Sofa
from cchair import Chair


class Room:
    MAX_LENGTH = 50
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.things = []

    def __str__(self):
        return f"комната:{length} {width} {height}"

    def add_tv(self, tv):
            self.things.append(tv)

    def add_pc(self, pc):
        self.things.append(pc)

    def add_chair(self, chair):
        self.things.append(chair)

    def add_sofa(self, sofa):
        self.things.append(sofa)

with open("room.txt", "r", encoding="utf-8") as froom:
    line = froom.readline()
length, width, height = line.split()
length = int(length)
width = int(width)
height = float(height)
room = Room(length, width, height)
print(room)

with open("tv.txt", "r", encoding="utf-8") as ftv:
    for line in ftv:
        model, diag, price = line.split(';')
        diag = int(diag)
        price = int(price)
        room.add_tv(Tv(model, diag, price))

with open("pc.txt", "r", encoding="utf-8") as fpc:
    for line in fpc:
        video_card, memory, cpu, price = line.split(';')
        memory = int(memory)
        price = int(price)
        room.add_pc(Pc(video_card, memory, cpu, price))

for thing in room.things:
    print(str(thing), end=';')











# r1 = Room(3, 4, 2.5)
# tv1 = Tv("samsung", 32, 40000)
# pc1 = Pc('geforce', 8, 'intel', 80000)
# cha1 = Chair('wood', 'black', 12000)
# sof1 = Sofa('leather', 'white', 23000)
# r1.add_tv(tv1)
# r1.add_pc(pc1)
# r1.add_chair(cha1)
# r1.add_sofa(sof1)
#
#
# print(f'{r1.length} {r1.width} {r1.height}')
# print(f'{tv1.model} {tv1.diag} {tv1.price}')
# print(f'{pc1.video_card} {pc1.memory} {pc1.cpu} {pc1.price}')
# print(f'{cha1.material} {cha1.color} {tv1.price}')
# print(f'{sof1.material} {sof1.color} {sof1.price}')
