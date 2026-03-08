if __name__ == "__main__":
    class SocialNetwork:
        """Базовый класс социальной сети"""

        def init(self, name: str, users: int):
            """
            Конструктор класса
            :param name: название сети
            :param users: количество пользователей
            """
            self.name = name
            self.users = users

        def str(self) -> str:
            """Строковое представление"""
            return f"Социальная сеть {self.name}, пользователей: {self.users}"

        def repr(self) -> str:
            """Техническое представление"""
            return f"SocialNetwork(name='{self.name}', users={self.users})"

        def add_users(self, count: int) -> None:
            """Добавить пользователей"""
            self.users += count

        def post(self, text: str) -> str:
            """Опубликовать пост"""
            return f"Пост в {self.name}: {text}"


    class VK(SocialNetwork):
        """Дочерний класс VK"""

        def init(self, name: str, users: int, music: bool):
            """
            Конструктор дочернего класса
            :param name: название сети
            :param users: количество пользователей
            :param music: есть ли музыкальный сервис
            """
            super().init(name, users)
            self.music = music

        def post(self, text: str) -> str:
            """
            Переопределение метода.
            Причина: во VK пост публикуется на стене.
            """
            return f"Запись на стене VK: {text}"

        def listen_music(self) -> str:
            """Проверка музыкального сервиса"""
            if self.music:
                return "Музыка доступна"
            return "Музыка недоступна"


    if name == "main":
        net = SocialNetwork("GenericNet", 1000)
        print(net)
        print(net.post("Привет"))

        vk = VK("VK", 5000000, True)
        print(vk)
        print(vk.post("Мой первый пост"))
        print(vk.listen_music())
    pass
