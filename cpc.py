class Pc:
    def __init__(self, video_card, memory, cpu, price):
        self.video_card = video_card
        self.memory = memory
        self.cpu = cpu
        self.price = price

    def __str__(self):
        return f"компьютер:{self.video_card} {self.memory} {self.cpu} {self.price}"