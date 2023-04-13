class Product:
    def __init__(self,id,name,description):
        self.id=id
        self.name=name
        self.description=description

dane=[
    Product(1,"Pralka", 'wash'),
    Product(2,'Scuter', 'drive'),
    Product(3,'Antyk', 'stand')
]

def getAll():
    return dane

def getOne(id):
    return [e for e in dane if int(e.id)==int(id)][0]
