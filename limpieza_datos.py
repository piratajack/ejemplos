#este codigo elimina espacios en blanco y email que esten duplicados


def limpiar_emails(lista_emails):  #definimos una funcion llamado limpiar _emails 
    # Usa un set para eliminar duplicados y strip para quitar espacios
    emails_limpios = {email.strip() for email in lista_emails}   #aca usando email.strip eliminamos espacios en blanco y usando for creamos un conjunto set que no permite elememtos duplicados asi que solo guarda uno  
    return list(emails_limpios)  #aca covertimos el conjuto set y una lista usando list(...)
emails = [
    "  user1@example.com",
    "user2@example.com  ",
    "user1@example.com",
    " user2@example.com",  
]

resultado = limpiar_emails(emails)    #aca imprimimos el resultado aunque puede que sea de manera desordenada por que los conjutos set no mantienen orden 
print(resultado)
