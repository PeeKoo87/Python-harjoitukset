class publication:
    def __init__(self, name):
        self.name = name


    def printInfo(self):

        print(f"julkaisun nimi on: {self.name}")

class magazine(publication):
    def __init__(self, name, editor):
        self.editor = editor
        super().__init__(name)
    def printInfo(self):
        super().printInfo()
        print(f"päätoimittaja: {self.editor}")

class book(publication):
    def __init__(self,author,pageCount):
        self.author = author
        self.pageCount = pageCount
        #todo: make this work

pub1 = magazine("Aku Ankka","Aki Hyyppä")
pub1.printInfo()
pub2 = book("Hytti nro 6","Rosa Liksom", 220)
pub2.printInfo()