import time
from threading import Thread

from helpers import Queue, Task


class Server(Thread):
    def __init__(self, queue: Queue, _id: int):
        super().__init__()
        self.server_id = _id
        self.queue = queue
        self.current_task: Task | None = None
        self.remaining_time = 0

    def run(self):
        while True:
            if not self.current_task and not self.queue.is_empty():
                self.current_task = self.queue.pop()
                self.remaining_time = self.current_task.duration
                print(
                    f"Сервер {self.server_id} освобождается, задание "
                    f"из очереди направленно на Сервер {self.server_id}"
                )

            if self.current_task:
                time.sleep(1)
                self.remaining_time -= 1

                if self.remaining_time <= 0:
                    self.current_task = None
                    if self.queue.is_empty():
                        print(f"Сервер {self.server_id} завершает выполнение")


class System:
    def __init__(self, queue: Queue, servers_count: int):
        self.servers: list[Server] = []
        self.servers_count = servers_count
        self.queue = queue

    def start(self):
        for server_id in range(1, self.servers_count + 1):
            server = Server(self.queue, server_id)
            self.servers.append(server)
            server.daemon = True
            server.start()

    def add_task(self, duration):
        task = Task(duration)
        less_loaded_server = min(
            self.servers,
            key=lambda serv: serv.remaining_time if serv.current_task else 0,
        )

        if not less_loaded_server.current_task:
            less_loaded_server.current_task = task
            less_loaded_server.remaining_time = task.duration
            print(
                f"Задание с {task.duration} секундами выполнения "
                f"направлено на Сервер {less_loaded_server.server_id}."
            )
        else:
            self.queue.push(task)
            print(
                f"Задание с {task.duration} секундами выполнения "
                "добавлено в очередь."
            )

    def system_info(self):
        print("Состояние серверов:")
        for server in self.servers:
            if not server.current_task:
                print(f"Сервер {server.server_id}: пусто")
            else:
                print(
                    f"Сервер {server.server_id}: выполняет задание "
                    f"(осталось {server.remaining_time} сек.)"
                )
        current_queue = (
            "нет." if self.queue.is_empty() else self.queue.get_all()
        )
        print(f"Очередь заданий: {current_queue}")


def main():
    queue = Queue()
    print("Добро пожаловать в симулятор распределенной системы.")
    servers_count = int(input("Введите количество серверов: "))

    system = System(queue, servers_count)
    system.start()
    system.system_info()

    print(
        "Введите команду:\n"
        "- добавить <секунд> "
        "(добавляет новую задачу с заданным временем выполнения)\n"
        "- статус (выводит информацию о состоянии серверов)\n"
        "- выход (завершает работу программы)\n"
    )
    while True:
        command = input("Команда: ")

        if command.startswith("добавить"):
            _, duration = command.split()
            system.add_task(int(duration))
        elif command == "статус":
            system.system_info()
        elif command == "выход":
            break
        else:
            print(
                "Неверная команда. Используйте "
                "'добавить <секунд>', 'статус' или 'выход'"
            )


if __name__ == "__main__":
    main()
