import morse

mensaje = input("Dime algo: ")

telegrama = morse.toMorse(mensaje)
print(telegrama)