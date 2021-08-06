# coding=utf-8
class Avtomobilchi:
    def __init__(self,egasi,rusumi,nomeri):
        self.egasi = egasi
        self.rusumi = rusumi
        self.nomeri = nomeri
    def __str__(self):
        return "{}    {}      {}".format(self.rusumi,self.nomeri,self.egasi)


class Parkovka:
    def __init__(self):
        self.mashinalar = []
    def registratsiya(self,a):
        self.mashinalar.append(a)
    def search(self,s):
        res = []
        for i in self.mashinalar:
            if s==i.rusumi:
                res.append(i.egasi)
        return res

    def print(self):
        for i in self.mashinalar:
            print(i)


a1 = Avtomobilchi('Dilshod','Matiz','777zz')
a5 = Avtomobilchi('Islom','malibu','736aa')
a3 = Avtomobilchi('Otabek','Jentra','123aa')
a2 = Avtomobilchi('Nurislom','Matiz','222cc')
a4 = Avtomobilchi('Nurbek','Jentra','543dd')
avt = [a1,a2,a3,a4,a5]

p = Parkovka()

for i in avt:
    p.registratsiya(i)

p.print()

print(p.search('Matiz'))