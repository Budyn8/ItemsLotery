Exit = ""
while(Exit != "Exit"):
    x = int(input("Enter how many items u want to have "))
    Category = input("Name a category of these items ")
    i = 1
    List = []
    while(i > 0):
     print("Enter",i,"item from the list ")
     Word = [input()]
     List += Word 
     i+=1
     if(x < i):
      break
    import random
    print("Yours",Category,"is",random.choice(List))
    Exit = input("In order to leave type \"Exit\" ")
    

