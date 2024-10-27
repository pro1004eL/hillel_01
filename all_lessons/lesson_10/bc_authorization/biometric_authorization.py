# Біометрична авторизація. Функція виконує авторизацію на підставі отриманого списка словників даних та словника,
# отриманого з іншої функції від користувача.

# Параметри користувача: id - int, name - str, second_name - str, age - int
# Якщо дані від користувача співпадають з єталонними даними - користувач отримує повний доступ.
# Якщо відрізняється одне поле - доступ read-only, якщо більше - доступ заборонено.
# Функція повертає рівень доступу: full, read-only, denied

# варіант вхідних значень
database_users = [
    {"id": 1, "name": "John", "second_name": "Doe", "age": 30},
    {"id": 2, "name": "Jane", "second_name": "Joi", "age": 25}
]
# варіанти user_input :
user_data = {"id": 1, "name": "John", "second_name": "Doe", "age": 130}
#{"id": 1, "name": "John", "second_name": "Joi", "age": 30},
#{"id": 1, "name": "John", "second_name": "Joi", "age": 25}

def biometric_authorization(database_users, users_data):
    for db_user in database_users:
        if db_user['id'] == user_data['id']:
            mismatches = sum(db_user[key] != users_data[key]
                             for key in ['name', 'second_name', 'age'])

            if mismatches == 0:
                return "full-access"
            elif mismatches == 1:
                return "read-only"
            else:
                return "access denied"

    return "access denied"

print(biometric_authorization(database_users, user_data))