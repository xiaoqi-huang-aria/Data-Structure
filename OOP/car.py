class Car:
    def __init__(self, year_model, make, speed):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    
    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5
    
    def get_speed(self):
        return self.__speed

def main():
    mycar = Car('2019', 'VW', 0)
    
    for i in range(5):
        mycar.accelerate()
        print(f"Current speed: {mycar.get_speed()}")

    for i in range(5):
        mycar.brake()
        print(f"Current speed: {mycar.get_speed()}")

main()