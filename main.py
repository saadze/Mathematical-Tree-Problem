from anytree import Node, RenderTree, findall_by_attr

nombreEtages = int(input("nombre d'étages:"))

prem = Node(1)
deux = Node(2, parent=prem)

droite = Node(3,parent=deux)
gauche = Node(1,parent=deux)
gauche1 = Node(3,parent=gauche)
droite1 = Node(1,parent=droite)
droite11 = Node(5,parent=droite)
somme =[]
previous = [gauche1,droite1,droite11]
somme.append(1)
somme.append(2)
somme.append(4)
somme.append(9)
ite=2
for i in range(2,nombreEtages+1):
    liste = []
    for j in range(len(previous)):
        parent = previous[j].parent.name
        calc= previous[j].name - parent
        if calc > 0:
            n = Node(calc,parent=previous[j])
            liste.append(n)
        addi = previous[j].name + parent
        v = Node(addi,parent=previous[j])
        liste.append(v)
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
input()


    