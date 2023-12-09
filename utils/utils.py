import random

class Utils:
    
    def __init__(self) -> None:
        pass

    def random_phone_number():
   
        # A random 10-digit number with the (XXX) XXX-XXXX format
        return f"({random.randint(100, 999)}) {random.randint(100, 999)}-{random.randint(1000, 9999)}"
