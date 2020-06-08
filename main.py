from abc import abstractmethod
from math import pi


class Shape_3D:
    @abstractmethod
    def __init__(self, R, R2=None, R3=None):
        self.R = R
        self.R2 = R2
        self.R3 = R3
    @abstractmethod
    def surface_area(self):
        raise NotImplementedError()
    @abstractmethod
    def volume(self):
        raise NotImplementedError()


class Sphere(Shape_3D):
    def __init__(self, R):
        super().__init__(R)
    def surface_area(self):
        return 4 * pi * pow(self.R, 2)
    def volume(self):
        return 4/3 * pi * pow(self.R, 3)


class Torus(Shape_3D):
    def __init__(self, R, R2):
        super().__init__(R, R2)
    def surface_area(self):
        return 4 * pow(pi, 2) * self.R * self.R2
    def volume(self):
        return 2 * pow(pi, 2) * self.R * pow(self.R2, 2)


class Ellipsoid(Shape_3D):
    def __init__(self, R, R2, R3):
        super().__init__(R, R2, R3)
    def surface_area(self):
        P = 1.6075
        return 4 * pi * pow(pow(self.R * self.R2, P) * pow(self.R2 * self.R3, P) * pow(self.R * self.R3, P) / 3, 1/P)
    def volume(self):
        return 4/3 * pi * self.R * self.R2 * self.R3


class Interface:
    def __init__(self, shape):
        self.shape = shape

    def run(self):

        if self.shape == '1':
            R = float(input("Sphere radius: "))
            sph = Sphere(R)
            print("Sphere surface: ", round(sph.surface_area(), 2))
            print("Sphere volume: ", round(sph.volume(), 2))
            print()

        elif self.shape == '2':
            R = float(input("Torus major radius: "))
            R2 = float(input("Torus minor radius: "))
            tor = Torus(R, R2)
            print("Torus surface: ", round(tor.surface_area(), 2))
            print("Torus volume:", round(tor.volume(), 2))
            print()

        elif self.shape == "3":
            R = float(input("First ellipsoid half-axis: "))
            R2 = float(input("Second ellipsoid half-axis: "))
            R3 = float(input("Third ellipsoid half-axis: "))
            ell = Ellipsoid(R, R2, R3)
            print("Ellipsoid surface: ", round(ell.surface_area(), 2))
            print("Ellipsoid volume: ", round(ell.volume(), 2))
            print()

        else:
            return False


print("OP 6.1, by Vlasov Andrei from IP-9105\nPython 3\n")
while True:
    print("Find surface area and volume of a:\n1. sphere\n2. torus\n3. ellipsoid")
    shape = input("[1/2/3/exit]: ")
    user = Interface(shape)
    if user.run() is False:
        break
