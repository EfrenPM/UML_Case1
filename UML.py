# Creando la Base de Datos
database = [] # En el ejemplo está vacía, pero realmente hay miles de usuarios registrados/almacenados
active_sessions = []

# Código en Python (Signin)
def signin(user: dict[str, str]) -> bool:
    user_id = str(len(database) + 1).zfill(10)
    new_user = {
        'userId': user_id,
        'username': user['username'],
        'password': user['password'],
        'email': user['email']
    }
    
    # Verificamos si existe ya un usuario
    for existing_user in database:
        if existing_user['username'] == new_user['username'] or existing_user['email'] == new_user['email']:
            return False
            
    # Confirmarmos que todos los valores del usuario sean strings y que el nombre de usuario tenga una longitud válida
    if all(isinstance(value, str) for value in new_user.values()) and 4 <= len(new_user['username']) <= 20:
        database.append(new_user)
        return True  # Usuario validado
    return False  # Validación fallida
    
# El usuario ya ha sido registrado en la base de datos
database = [
    {'userId': str(len(database + 1)).zfill(10), 'username': 'Pepe Morales', 'password': '1234Pepe1', 'email': 'example@email.com'}
]

# Código en Python (Login)
def login(active_user: dict[str, str]) -> bool:
    for existing_user in database:
        if existing_user['username'] == active_user['username'] and existing_user['password'] == active_user['password']:
            active_sessions.append(existing_user['userId'])
            return True  # Login exitoso
        return False # Logout fallido

# Código en Python (Logout)
def logout(user_id: str) -> bool:
    if user_id in active_sessions:
        active_sessions.remove(user_id)
        return True  # Logout exitoso
    return False  # Logout fallido


# Hacer un menú con las opciones: signin, login, logout
# Construir diversas condiciones (te explicaré más adelante)


# Función principal para el menú
def main_menu():
    while True:
        print('\n--- Menú ---')
        print('1. Signin')
        print('2. Login')
        print('3. Salir')
        option = input('Seleccione una opción (1-3): ')

        if option == '1':
            username = input('Ingrese su nombre de usuario: ')
            password = input('Ingrese su contraseña: ')
            email = input('Ingrese su correo electrónico: ')
            user_data = {
                'username': username,
                'password': password,
                'email': email
            }
            if signin(user_data):
                print(f'Usuario {username} registrado exitosamente.')
            else:
                print(f'Error: El usuario {username} ya existe o la validación falló.')

        elif option == '2':
            username = input('Ingrese su nombre de usuario: ')
            password = input('Ingrese su contraseña: ')
            active_user_data = {
                'username': username,
                'password': password
            }
            if login(active_user_data):
                print(f'Usuario {username} ha iniciado sesión.')
            else:
                print(f'Error: Credenciales incorrectas para el usuario {username}.')
        
        elif option == '3':
            print('Saliendo del programa...')
            break

        else:
            print('Opción no válida. Intente de nuevo.')

# Ejecución del menú
if __name__ == '__main__':
    main_menu()
