Exit = ""
while(Exit != "Exit"):
    x = int(input("Wpisz Liczbę Przedmiotów "))
    Kategoria = input("Kategoria itemów ")
    i = 1
    Lista = []
    while(i > 0):
     print("Wpisz",i,"Item do listy ")
     Słowo = [input()]
     Lista += Słowo 
     i+=1
     if(x < i):
      break
    import random
    print("Twój/Twoja",Kategoria,"to",random.choice(Lista))
    Exit = input("Wpisz \"Exit\" aby wijść ")
    

