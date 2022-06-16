while (True):
   wybor = input("* - mnożenie, / - dzielić, + - dodawać, - -odejmować: \n")
   a = int(input("Liczba pierwsza:\n"))
   b = int(input("Liczba drugoa:\n"))
   if(wybor == "*"):
      print(a * b)
   elif(wybor == "/"):
       if (b == 0):
        print("Nie dziel przez zero, cholero!")
       else:
                print (a / b)
   elif(wybor == "+"):
       print(a + b)
   elif(wybor == "-"):
       print(a - b)
    
   else:
       print("nie wybrałeś dobrej opcji")
