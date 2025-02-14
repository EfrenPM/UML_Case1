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

active_sessions = []

# Código en Python (Login)
def login(active_user: dict[str, str]) -> bool:
    for existing_user in database:
        if existing_user["username"] == active_user["username"] and existing_user["password"] == active_user["password"]:
            active_sessions.append(existing_user["userId"])
            return True  # Login exitoso
    return False # Logout fallido

# Código en Python (Logout)
def logout(active_sessions: list[str], user_id: str) -> bool:
    active_sessions.remove(user_id)
    return True

# Hacer un menú con las opciones: signin, login, logout
# Construir diversas condiciones (te explicaré más adelante)
