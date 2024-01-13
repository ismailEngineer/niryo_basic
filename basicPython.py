# Ecrire ici un commenataire 
import time
import numpy as np
import json
import yaml

# from matplotlib  

time.sleep(2)

# List : 
list_string = ["lundi","ee","mardi","mercredi","lundi"]
list_int = [2,1,3]

list_string.append("jeudi")
list_string.pop(1)
list_string.remove("lundi")

print(list_string)

# Dictionnaire :
Dictio1 = dict()
Dictio1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

Joueur1 = {
    "name": "alain",
    "age": 22,
    "power": 100
}
Color_LED = {
    "R" : 255,
    "G" : 0,
    "B" : 0
}
print(Dictio1.get("brand"))
PoseRobot = [{
    "x" : 0,
    "y" : 1,
    "z" : 5 
}]
PoseRobot.append({"x":5,"y":4,"z":0})
print(PoseRobot)

# Function 

# EN C/C++
# int somme(int a ,int b)
# {
#     return (a+b);
# }

def somme(a,b):
    som = a+b
    diff = a-b
    multi = a*b
    div = a/b

    return(som,diff,multi,div)

#[] : liste
#{
    # Dictionnaire
#}
#(a,b,c,d) ==> tuplet

a,b,c,d = somme(2,3)

print(a)
print(b)
# print(c)
# print(d)

#########################################################

list_a = [1,2,3,4]

print(list_a[2])

for i in range(4):
    print(a)
    for j in range(2):
        print(b)
        for k in range(2):
            print(k)
        # instrcution
    # instruction

m = 0
flag = True
variable = 1
while m < 2:
    print("je suis en while")
    #m += 1 #m = m + 1
    # Ctrl + C pour arreter les boucles infinis 

    if flag : # flag == True | not flag ==> False
        break

    if variable : # variable ==> si variable # 0 
        print("OK")
    else :
        print("KO")

    if variable :
        print("OK")
    elif variable == 0 :
        print("KO")
    else : 
        print("KO KO")


# Class       
class robot :
    # Le constructeur
    def __init__(self,nom_1,nb_joint_1,pose_init_1):
        self.nom = nom_1
        self.nb_joint = nb_joint_1
        self.pose_init = pose_init_1
        self.pose = (-1,-1,-1)
    
    def get_postion_robot(self):
        return(self.pose)
    

r1 = robot("Niryo",6,(0, 0, 0.10))
a = r1.pose
r2 = robot("Buddy",3,(0, 0.3, 0.20))
print(a)



######### Exercice : 

# 1 - creer des fonctions :
#     - init : qui me le robot dans une position initiale 
#     - aller_gauche : qui va deplacer le robot vers une position gauche
#     - aller_droite : qui va deplacer le robot vers une position droite   
#     - aller_haut : qui va deplacer le robot vers une position haut  


#######  #######

print("###################################")

# from basic_robot_command import *
from basic_robot_command import basic_command,navigate

instance_1 = basic_command()
print("############ BEFORE ###############")
print(instance_1.getter_pose())
instance_1.setter_pose(2.0,3.0,1.0)
print("############ AFTER  ################")
print(instance_1.getter_pose())

navigate()



with open('config.yaml','r') as file:
    object_file = yaml.safe_load(file)

print(object_file['IP_ROBOT'])
#print(object_file)