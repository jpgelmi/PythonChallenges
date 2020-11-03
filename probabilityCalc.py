
class Hat:
    def __init__(self,red = 1 ,**kwargs):
        self.__dict__.update(kwargs)

    def clasificar(self):
        contents = []
        contentsDict = {}
        for i in self.__dict__:
            contents.append(i)
            contentsDict[i] = self.__dict__[i]
        return contents, contentsDict
    
    def probabilidad(self, data, item):
        dataList = data[0] 
        dataDict = data[1]
        total = 0
        for i in dataDict:
            total = total + dataDict[i]
        
        if total == 0:
            print("Ingresa bien los valores")
        try:
            p = round(100*(dataDict[item]/total))
            return (str(p) + " %") 
        except:
            print("El valor que ingresaste no está en la tombola")

hat = Hat(rojo = 50 , azul = 100)
hat.clasificar()
print(hat.probabilidad(hat.clasificar(), "rojo"))


