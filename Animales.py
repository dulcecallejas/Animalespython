print ("Welcome to the animal game")
while True:
  print ("1 Perro")
  print ("2 Gato")
  print ("3 Exit")

  opcion = int(input("Introduce la opcion==>"))
  if opcion == 1:
    print("""
    ,-.___,-.
    \_/_ _\_/
      )O_O(
     { (_) }
      `-^-' 
    """ 
    )
  elif opcion == 2:
    print("""
    ┈┈╱╲┈┈┈ ╱╲┈┈╭━╮┈
    ┈╱╱╲╲__╱╱╲╲┈╰╮┃┈
    ┈▏┏┳╮┈╭┳┓▕┈┈┃┃┈
    ┈▏╰┻┛▼┗┻╯▕┈┈┃┃┈
    ┈╲┈┈╰┻╯┈┈╱▔▔┈┃┈
    ┈┈╰━┳━━━╯┈┈┈┈┃┈
    ┈┈┈┈┃┏┓┣━━┳┳┓┃┈
    ┈┈┈┈┗┛┗┛┈┈┗┛┗┛┈2"""
    )

  elif opcion == 3:
     print("Bye")
     break
  else:
    print("Opción incorrecta")
