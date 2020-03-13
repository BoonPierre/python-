import datetime


class Animal:

     def __init__(self,nom,age,sexe):

          self.nom = nom
          self.age = age
          self.sexe = sexe

     def __str__(self):

          return "nom : "+ self.nom +" age : "+ str(self.age) +" sexe: " + self.sexe


class Farm:

     def __init__(self,name):
          self.name = name
          self.list = []

     def add(self,nom,age,sexe):

          self.list.append(animal(nom,age,sexe))


     def __str__(self):

          return self.name


if __name__ == "__main__":

     farm_list = []

     farm_list.append(farm("Ferme #1"))
     farm_list.append(farm("Ferme #2"))

     #----poule
     farm_list[1].add("poule",3,"femelle")
     farm_list[1].add("poule",1,"femelle")
     farm_list[1].add("poule",2,"femelle")

     #----vache
     farm_list[0].add("vache",1,"femelle")
     farm_list[0].add("vache",5,"femelle")
     farm_list[0].add("vache",3,"femelle")


     for farm in farm_list:                       #----boucle farm qui fais parmis toute les ferme
          print(farm)
          for animal in farm.list:                #----boucle animal qui fais tous les animaux de la liste
               print(animal)
