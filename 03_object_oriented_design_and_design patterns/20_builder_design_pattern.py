class Computer():
    def __init__(self, cpu, ram, storage):
        self.ram = ram
        self.cpu = cpu
        self.storage = storage
    def __str__(self):
        return f"Computer with CPU: {self.cpu}, RAM: {self.ram}, STORAGE: {self.storage}"
class Computer_builder:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
    def set_cpu(self, cpu):
        self.cpu = cpu
        return self
    def set_ram(self, ram):
        self.ram = ram
        return self
    def set_storage(self, storage):
        self.storage = storage
        return self

    def build(self):
        return Computer(self.cpu, self.ram, self.storage)

builder = Computer_builder()
computer = builder.set_cpu("Intel core i9").set_ram("32GB").set_storage("1TB SSD").build()
print(computer)