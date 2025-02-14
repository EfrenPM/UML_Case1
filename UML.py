# Creando la Base de Datos
database = [] # En el ejemplo está vacía, pero realmente hay miles de usuarios registrados/almacenados
# Código en Python (Signin)
def signin(user: dict[str, str]) -> bool:
    user = {
        "userId" : str(len(database + 1)).zfill(10),
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
    
# El usuario ya ha sido registrado en la base de datos
database = [
    {"userId": str(len(database + 1)).zfill(10), "username": "Pepe Morales", "password": "1234Pepe1", "email": "example@email.com"}
]

activesessions = list(user["userId"])

# Código en Python (Login)
def login(active_user: dict[str, str]):
    # Verificamos, por ejemplo, si el usuario y la contraseña coinciden con alguno de los usuarios ya almacenados
    for existing_user in database:
        if existing_user["username"] == user["username"] and existing_user["password"] == user["password"]:
            return True  # Login exitoso
    return False  # Login fallido. Esto ocurre porque no encuentra ninguna coincidencia
    activesessions.append[active_user]

# Código en Python (Logout)
def logout():
    return activessesions.remove(active_user)
