class Pet:
    def __init__(self,name,type,age):
        self.__name = name
        self.__animal_type = type
        self.__age = age

    def set_name(self,name):
        self.__name = name

    def set_animal_type(self,type):
        self.__animal_type = type

    def set_age(self,age):
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def get_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age
    
def main():
    mypet = Pet('XX','cat',1)
    mypet.set_name('QQ')
    print(f'The name of my pet is {mypet.get_name()}') 
    print(f'The type of my pet is {mypet.get_type()}')
    print(f'The age of my pet is {mypet.get_age()}')
    
main()
    