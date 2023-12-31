import random, string

class Utils:
    
    def __init__(self) -> None:
        pass

    def random_phone_number():
        # A random 10-digit number with the (XXX) XXX-XXXX format
        return f"({random.randint(100, 999)}) {random.randint(100, 999)}-{random.randint(1000, 9999)}"
    
    def generate_name():
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(4))

    def user_save(user):
        with open("usr.txt","w") as file:
            file.write("usr_name: " + user.name + "\n")
            file.write("usr_mail: " + user.mail + "\n")
            file.write("usr_phone: " + user.phone + "\n")
        
