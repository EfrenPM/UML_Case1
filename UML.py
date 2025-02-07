# Código en Python (Signin)
def signin(user):
  user = {
    userId = '55_323_45_DC'
    username = 'Pepe'
    password = '1234Pepe1'
    email = 'xxxx@email.com'
    }
  validate_user = False
  for user in database:
    if database[user] == database[user - 1]:
      return validate_user
    elif isinstance(user.values(), str) and 8 >= len(user[username]) <= 10:
      database.extend(user)
      validate_user = True
  return user

#def validate_credentials(user):
 # if isinstance(user.values(), str) and 8 >= len(user[username]) <= 10:
  #  return True
  # else:
  #  return False

# def get_details(user):
  # database.extend(user)
  # return user

# def add_user(user):
  # for user in database:
    # if database[user] == database[user - 1]:
      # return False
    # else:
      # return True
