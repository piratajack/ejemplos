def limpiar_emails(lista_emails):
    # Usa un set para eliminar duplicados y strip para quitar espacios
    emails_limpios = {email.strip() for email in lista_emails}
    return list(emails_limpios)
emails = [
    "  user1@example.com",
    "user2@example.com  ",
    "user1@example.com",
    " user2@example.com",  # Si consideras mayúsculas/minúsculas diferentes
    "user3@example.com"
]

resultado = limpiar_emails(emails)
print(resultado)
