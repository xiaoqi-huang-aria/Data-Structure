def HollywoodBlockBusterGenerator(names, casting_size):
    result_list = [None] * casting_size
    generateBillboard(names, casting_size, result_list, 0)

def generateBillboard(names, casting_size, result_list, position):    
    if casting_size == 0:
        print(result_list)
        return
    for i in range(len(names)):
        result_list[position] = names[i]
        generateBillboard(names[i+1:], casting_size-1, result_list, position+1)
    

    
casting = ["Gal Gadot", "Al Pacino", "Gong Li", "Hu Ge", "Denzel Washington", "Zhang Ziyi", "Brad Pitt"]
HollywoodBlockBusterGenerator(casting, 2)


    
