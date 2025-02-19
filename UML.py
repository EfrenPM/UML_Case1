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

# Función principal para el menú
def main_menu():
    while True:
        print('\n--- Menú ---')
        print('1. Signin')
        print('2. Login')
        option = input('Seleccione una opción (1-2): ')

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

        else:
            print('Opción no válida. Intente de nuevo.')


            #elif option == '3':
            #if active_sessions:
            #    print('Sesiones activas:')
            #    for session in active_sessions:
            #        print(f'ID de Usuario: {session}')
            #    user_id = input('Ingrese su ID de usuario para cerrar sesión: ')
            #    if logout(user_id):
            #        print(f'Usuario con ID {user_id} ha cerrado sesión.')
            #    else:
            #        print(f'Error: No se pudo cerrar sesión para el ID de usuario {user_id}.')
            #else:
            #    print('No hay sesiones activas.')
                

# Ejecución del menú
if __name__ == '__main__':
    main_menu()
