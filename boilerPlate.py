class Rectangulo():
    def __init__(self, width = 5, heigth = 10):
        self.width = width
        self.heigth = heigth
    
    def set_width(self, width):
        self.width = width
    
    def set_heigth(self, heigth):
        self.heigth = heigth
    
    def get_area(self):
        area = self.width * self.heigth
        return area
    
    def get_perimetro(self):
        perimetro = ((2 * self.width) + (2 * self.heigth))
        return perimetro

    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.heigth ** 2) ** .5)
        return diagonal

    def get_picture(self):
        if self.heigth > 50:
            print("Es muy grande!")
        
        elif self.heigth <= 50:
            largo = "*" * self.width
            for i in range(self.heigth):
                print(largo)    
    
    def get_amount_inside(self, width2, heigth2):
        veces_width = self.width / width2
        veces_width_aprox = round(veces_width)

        veces_heigth = self.heigth / heigth2
        veces_heigth_aprox = round(veces_heigth)

        print("La figura cabe...")
        if veces_width_aprox > veces_width or veces_heigth_aprox > veces_heigth:
            print(veces_width_aprox - 1 , "veces")
        else:
            print(veces_width_aprox, "veces")

class Cuadrado(Rectangulo):
    def __init__(self):
        Rectangulo.__init__(self, width= 9, heigth=9)
    
    def set_heigth(self, heigth):
        self.heigth = heigth
        self.width= heigth

    def set_width(self, width):
        self.heigth = width
        self.width= width

r1 = Rectangulo(50,50)

r1.get_amount_inside(49,58)

c = Cuadrado()
area = c.get_area() 
print(area)

c.set_width(8)
area = c.get_area() 
print(area)

