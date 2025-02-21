#####################################
# Entornos de Desarrollo (ETS)
# Proyecto de UML: Caso 1
# Darío y Efrén 1ºDAW
#####################################

# Archivos donde se guardarán los datos
DATABASE_FILE = 'usuarios.txt'
SESSIONS_FILE = 'sesiones.txt'

# Función para cargar los datos desde los archivos
def load_data():
    # Inicializamos las variables
    database = []
    active_sessions = {}

    # Cargar base de datos de usuarios
    with open(DATABASE_FILE, 'r') as file:
        lines = file.readlines()
        for line in lines:
            user_data = line.strip().split(',')
            user = {
                'userId': user_data[0],
                'username': user_data[1],
                'password': user_data[2],
                'email': user_data[3]
            }
            database.append(user)

    # Cargar sesiones activas
    with open(SESSIONS_FILE, 'r') as file:
        lines = file.readlines()
        for line in lines:
            user_id, is_active = line.strip().split(',')
            active_sessions[user_id] = is_active == 'True'  # Convertimos la cadena 'True'/'False' en booleano

    return database, active_sessions

# Función para guardar los datos en los archivos
def save_data(database, active_sessions):
    # Guardar base de datos de usuarios
    with open(DATABASE_FILE, 'w') as file:
        for user in database:
            # Guardamos los datos del usuario como una cadena separada por comas
            user_data = f"{user['userId']},{user['username']},{user['password']},{user['email']}\n"
            file.write(user_data)

    # Guardar sesiones activas
    with open(SESSIONS_FILE, 'w') as file:
        for user_id, is_active in active_sessions.items():
            # Guardamos el ID de usuario y si está activo como una cadena separada por comas
            file.write(f"{user_id},{is_active}\n")

# Base de datos de usuarios y sesiones activas (cargadas al inicio)
database, active_sessions = load_data()

user_id_counter = len(database) + 1  # Inicializamos el contador basado en el número de usuarios actuales

# Código en Python (Signin)
def signin(user: dict[str, str]) -> str:
    global user_id_counter
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
        save_data(database, active_sessions)  # Guardamos los cambios
        return new_user_id  # Devolvemos el ID del nuevo usuario
    return None  # Validación fallida

# Código en Python (Login)
def login(login_user: dict[str, str]) -> bool:
    for existing_user in database:
        if existing_user['username'] == login_user['username'] and existing_user['password'] == login_user['password']:
            active_sessions[existing_user['userId']] = True  # Marcamos la sesión como "activa"
            save_data(database, active_sessions)  # Guardamos los cambios
            return True  # Login exitoso
    return False  # Login fallido

# Código en Python (Logout)
def logout(user_id: str) -> bool:
    if user_id in active_sessions and active_sessions[user_id]:  # Verificamos si el usuario está activo
        active_sessions[user_id] = False  # Marcamos la sesión como "no activa"
        save_data(database, active_sessions)  # Guardamos los cambios
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
            print('\n--- Menú de inicio ---\n')
            print('1. Signin')
            print('2. Login')
            option = input('\nSeleccione una opción (1-2): ')

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
                    print(f'\nUsuario {username} registrado exitosamente con ID: {user_id}.')
                else:
                    print(f'\nError: El usuario {username} ya existe o la validación falló.')

            # Si seleccionamos 2, se ejecutará el login
            elif option == '2':
                username = input('Ingrese su nombre de usuario: ')
                password = input('Ingrese su contraseña: ')
                login_user_data = {
                    'username': username,
                    'password': password
                }
                if login(login_user_data):
                    print(f'\nUsuario {username} ha iniciado sesión.')
                else:
                    print(f'\nError: Credenciales incorrectas para el usuario {username}.')

            # Si no seleccionamos ni 1 ni 2, saltará un error
            else:
                print('\nError: Opción no válida, pruebe de nuevo.')

        # Si hay sesiones activas:
        else:
            print('\n--- Menú de usuario ---\n')
            print('1. Logout')
            print('2. Salir')
            option = input('\nSeleccione una opción (1-2): ')

            # Si seleccionamos 1, se ejecutará el logout
            if option == '1':
                if logout(logged_in_user_id):
                    print(f'\n{username} ha cerrado la sesión correctamente.')

            # Si seleccionamos 2, se ejecutará la salida del programa
            elif option == '2':
                print('Saliendo del sistema...')

            # Si no seleccionamos ni 1 ni 2, saltará un error
            else:
                print('Error: Opción no válida, pruebe de nuevo.')

# Ejecución del menú
if __name__ == '__main__':
    main_menu()
