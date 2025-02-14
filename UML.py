# Creando la Base de Datos
database = [] # En el ejemplo está vacía, pero realmente hay miles de usuarios registrados/almacenados
# Código en Python (Signin)
def signin(user: dict[str, str]) -> bool:
    user = {
        "userId" : "55_223_405_DC",
        "username" : "Pepe Morales",
        "password" : "1234Pepe1",
        "email" : "example@email.com"
    }
    validate_user = False
    
    # Verificamos si existe ya un usuario
    for existing_user in database:
        if any(value in existing_user.values() for value in user.values()):
            return False
            
    # Confirmarmos que todos los valores del usuario sean strings y que el nombre de usuario tenga una longitud válida
    if all(isinstance(value, str) for value in user.values()) and 4 <= len(user["username"]) <= 20: 
        database.append(user)
        validate_user = True #usuario validado
    return validate_user 
