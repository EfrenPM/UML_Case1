#####################################
# Entornos de Desarrollo (ETS)
# Proyecto de UML: Caso 1
# Darío y Efrén 1ºDAW
#####################################

database = [] # Base de datos de usuarios
active_sessions = {}  # Diccionario para guardar las sesiones activas por ID de usuario
user_id_counter = 1  # Contador global para generar IDs únicos

# Código en Python (Signin)
def signin(user: dict[str, str]) -> str:
    global user_id_counter  # Usamos la variable global para acceder al contador
    new_user_id = str(user_id_counter).zfill(10)  # Generamos el ID del usuario
    new_user = {
        'userId': new_user_id,
        'username': user['username'],
        'password': user['password'],
        'email': user['email']
    }

    # Verificamos si existe ya un usuario con el mismo nombre de usuario o correo electrónico
    for existing_user in database:
        if existing_user['username'] == new_user['username'] or existing_user['email'] == new_user['email']:
            return None  # Retornamos None si el nombre de usuario o el correo electrónico ya existen

    # Confirmamos que todos los valores del usuario sean strings y que el nombre de usuario tenga una longitud válida
    if all(isinstance(value, str) for value in new_user.values()) and 4 <= len(new_user['username']) <= 20:
        database.append(new_user)
        active_sessions[new_user_id] = False  # Inicializamos la sesión como "no activa"
        user_id_counter += 1  # Incrementamos el contador de ID
        return new_user_id  # Devolvemos el ID del nuevo usuario
    return None  # Validación fallida

# Código en Python (Login)
def login(login_user: dict[str, str]) -> bool:
    for existing_user in database:
        if existing_user['username'] == login_user['username'] and existing_user['password'] == login_user['password']:
            active_sessions[existing_user['userId']] = True  # Marcamos la sesión como "activa"
            return True  # Login exitoso
    return False  # Login fallido

# Código en Python (Logout)
def logout(user_id: str) -> bool:
    if user_id in active_sessions and active_sessions[user_id]:  # Verificamos si el usuario está activo
        active_sessions[user_id] = False  # Marcamos la sesión como "no activa"
        return True  # Logout exitoso
    return False  # Logout fallido

# Función principal para el menú
def main_menu():
    while True:
        # Encontrar al usuario activo
        logged_in_user_id = None
        for user_id, active in active_sessions.items():
            if active:
                logged_in_user_id = user_id
                break  # Salimos del bucle al encontrar al usuario activo

        # Si no hay sesiones activas:
        if logged_in_user_id is None:
            print('\n--- Menú de inicio ---')
            print('1. Signin')
            print('2. Login')
            option = input('Seleccione una opción (1-2): ')

            # Si seleccionamos 1, se ejecutará el signin
            if option == '1':
                username = input('Ingrese su nombre de usuario: ')
                password = input('Ingrese su contraseña: ')
                email = input('Ingrese su correo electrónico: ')
                user_data = {
                    'username': username,
                    'password': password,
                    'email': email
                }
                user_id = signin(user_data)
                if user_id:
                    print(f'Usuario {username} registrado exitosamente con ID: {user_id}.\nAnote su ID porque le será imprescindible para poder cerrar sesión.')
                else:
                    print(f'Error: El usuario {username} ya existe o la validación falló.')

            # Si seleccionamos 2, se ejecutará el login
            elif option == '2':
                username = input('Ingrese su nombre de usuario: ')
                password = input('Ingrese su contraseña: ')
                login_user_data = {
                    'username': username,
                    'password': password
                }
                if login(login_user_data):
                    print(f'Usuario {username} ha iniciado sesión.')
                else:
                    print(f'Error: Credenciales incorrectas para el usuario {username}.')

            # Si no seleccionamos ni 1 ni 2, salatará un error
            else:
                print('Error: Opción no válida, pruebe de nuevo.')

        # Si hay sesiones activas:
        else:
            print('\n--- Menú de usuario ---')
            print('1. Logout')
            print('2. Salir')
            option = input('Seleccione una opción (1-2): ')

            # Si seleccionamos 1, se ejecutará el logout
            if option == '1':
                if logout(logged_in_user_id):
                    print(f'Usuario con ID {logged_in_user_id} ha cerrado sesión.')
                else:
                    print('Error: No se pudo cerrar sesión.')

            # Si seleccionamos 2, se ejecutará la salida del programa
            elif option == '2':
                print('Saliendo del sistema...')
                break

            # Si no seleccionamos ni 1 ni 2, salatará un error
            else:
                print('Error: Opción no válida, pruebe de nuevo.')

# Ejecución del menú
if __name__ == '__main__':
    main_menu()
