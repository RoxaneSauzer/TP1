#Imports éventuels
#Déclaration des classes et fonctions
#Programme principal

#2

class Vector:
    def __init__(self, coeffs):
        self.list_coeffs = coeffs

    def __str__(self):
        result= '['
        for i in range(len(self.list_coeffs)):
            if i < len(self.list_coeffs)-1:
               result += str(self.list_coeffs[i]) + ';'
            else:
                result += str(self.list_coeffs[i])
        return  str(result) + ']'

    def dimension(self):
        return len(self.list_coeffs)

    def get(self,i):
        return self.list_coeffs[i]

    def calculate_sum(self,other):
        if self.dimension() != other.dimension():
            raise ValueError('Les vecteurs ne sont pas de meme dimension')
        result = []
        for i in range(len(self.list_coeffs)):
            result.append(self.get(i) + other.get(i))
        vect=Vector(result)
        return vect

#3

class Polynomial(Vector):

    def __init__(self, coeffs):
        super().__init__(coeffs)

    def degree(self):
        return self.dimension()-1

    def __str__(self):
        result = ''
        for i in range(len(self.list_coeffs)):
            if i < len(self.list_coeffs)-1:
                result += str(self.get(i)) + 'x^' + str(i) + '+'
            else:
                result += str(self.get(i)) + 'x^'+ str(i)
        return result

    def evaluate(self,x):
        result=0
        for i in range(len(self.list_coeffs)):
            result += self.get(i)*(x**i)
        return result
