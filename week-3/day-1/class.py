class Dog(object):
    num_of_legs = 4

    # def __init__(self):
    #     pass
    
    def speak(self):
        print("whoof")

    def walk(self, x: int):
        print(f"i walked {x * self.num_of_legs} meters ")
        self.speak()

    



def main():
    dog = Dog()
    walk(dog, 5)
    # dog.speak()
    
    yellowDog = Dog()
    # yellowDog.speak()
    # yellowDog.walk



if __name__ == "__main__":
    main()