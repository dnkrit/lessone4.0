class User():
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name

    def __str__(self):
        return f"ID: {self._user_id}, Имя: {self._name}, Уровень доступа: {self._access_level}"


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._users = []

    def add_user(self, user):
        if user not in self._users:
            self._users.append(user)
            print(f"Пользователь {user.get_name()} успешно добавлен в систему.")
        else:
            print("Пользователь уже добавлен в систему")

    def remove_user(self, user):
        if user in self._users:
            self._users.remove(user)
            print(f"Пользователь {user.get_name()} успешно удален из системы.")
        else:
            print("Пользователь не найден в системе")

    def list_users(self):
        for user in self._users:
            print(user)

# Тестирование системы
if __name__ == "__main__":
    admin = Admin("A1", "Алена")
    user1 = User("U1", "Эмма")
    user2 = User("U2", "Света")

    print(admin)
    admin.add_user(user1)
    admin.add_user(user2)
    admin.list_users()

    admin.remove_user(user1)
    admin.list_users()