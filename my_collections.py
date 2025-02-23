import collections


def finde_max(liste):
    groeßte = 0
    for element in liste:
        if element > groeßte:
            groeßte = element
    return groeßte

def durchschnitt(liste):
    summe=0
    for e in liste :
        summe+=e
    return sum(liste)/len(liste)


def gemeinsam(liste1,liste2):
    liste3=liste1

    for element in liste2:
        if element not in liste3:
            liste3.append(element)

    return liste3


def gemeinsam2(liste1,liste2):
    return list(set(liste1) |set(liste2))
liste1 = [1,2,2,3,3,3]
liste2= [3,4,5]

def haeufigkeiten(liste) :
    dict_h= dict()
    list2= list()


    for element in liste:
        if element in dict_h:
            dict_h[element]+=1
        elif element not in dict_h:
            dict_h[element]=1
    return dict_h



print(haeufigkeiten(liste1))


