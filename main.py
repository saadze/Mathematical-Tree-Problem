from anytree import Node, RenderTree, findall_by_attr
#This file is completely in French !  Sorry English speakers, but you can still understand part of it
nombreEtages = int(input("nombre d'étages:"))
#Creates first nodes
prem = Node(1)
deux = Node(2, parent=prem)
droite = Node(3,parent=deux)
gauche = Node(1,parent=deux)
somme =[]
previous = [gauche,droite]
somme.append(1)
somme.append(2)
somme.append(4)
#For every line
for i in range(1,nombreEtages+1):
    liste = []
    #for every node in a line
    for j in range(len(previous)):
        parent = previous[j].parent.name
        calc= previous[j].name - parent
        #checks if the difference between the two last values in a branch is positive
        if calc > 0:
            n = Node(calc,parent=previous[j])
            liste.append(n)
        addi = previous[j].name + parent
        v = Node(addi,parent=previous[j])
        liste.append(v)
    #saves the values in the last line for later
    previous= list(liste)
    liste2 = [i.name for i in liste]
    somme.append(sum(liste2))
print('Somme des lignes: ',somme)
print(RenderTree(prem,maxlevel=nombreEtages).by_attr())
cond= 'y'
while cond == 'y':
    searchNb = int(input("Nombre que tu cherches dans l'arbre :"))
    print("Nombre d'apparitions:",len(findall_by_attr(prem,searchNb,maxlevel=nombreEtages)))
    cond = str(input('Entrer( y ) pour pouvoir tester un second nombre'))
#keeps the terminal window open
input()