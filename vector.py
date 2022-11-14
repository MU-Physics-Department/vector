class Vector:
    def __init__(self, x: [int, float], y: [int, float], z: [int, float]):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)


    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    
    
    def __str__(self):
        return "x component: %f, y component: %f, z component: %f" % (self.x, self.y, self.z)


print("Vector module is imported successfully.")
