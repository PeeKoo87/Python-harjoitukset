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
        print(f"Päätoimittaja: {self.editor}")

class book(publication):
    def __init__(self,name,author,pageCount):
        self.author = author
        self.pageCount = pageCount
        super().__init__(name)
    def printInfo(self):
        super().printInfo()
        print(f"Kirjailija: {self.author}")
        print(f"Kirjan sivujen määrä: {self.pageCount}")

pub1 = magazine("Aku Ankka", "Aki Hyyppä")
pub1.printInfo()
pub2 = book("Hytti nro 6", "Rosa Liksom", "200")
pub2.printInfo()
