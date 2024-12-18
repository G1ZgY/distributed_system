# Симулятор распределённой системы обработки задач

## Описание

Это приложение представляет собой симуляцию распределённой системы.
Программа демонстрирует управление очередями задач, оптимальное распределение нагрузки и взаимодействие процессов.

## Возможности

- **Распределение задач**:
  Задачи автоматически направляются на серверы с минимальной загрузкой.

- **Очередь задач**:
  Задачи, которые не могут быть сразу назначены серверу, сохраняются в общей очереди.

- **Мониторинг состояния**:
  Программа позволяет в реальном времени отслеживать, какие задачи выполняются, а также текущее состояние очереди.

## Установка

1. Убедитесь, что у вас установлен Python версии 3.8 или выше.
2. Скачайте репозиторий:
   ```bash
   git clone <URL-репозитория>
   cd <папка-репозитория>
   ```

## Запуск

1. Запустите программу:
    ```bash
   python main.py
   ```
2. Следуйте инструкциям в консоли:
    * Введите количество серверов.
    * Добавляйте задачи командой добавить <время_выполнения>.


## Пример работы

1. Инициализация сервиса:
```
Добро пожаловать в симулятор распределенной системы.
Введите количество серверов: 2
Состояние серверов:
Сервер 1: пусто
Сервер 2: пусто
Очередь заданий: нет.
Введите команду:
- добавить <секунд> (добавляет новую задачу с заданным временем выполнения)
- статус (выводит информацию о состоянии серверов)
- выход (завершает работу программы)
```

2. Добавление задач:
```
Команда: добавить 15
Задание с 15 секундами выполнения направлено на Сервер 1.
Команда: добавить 8
Задание с 8 секундами выполнения направлено на Сервер 2.
Команда: добавить 11
Задание с 11 секундами выполнения добавлено в очередь.
Команда: добавить 20
Задание с 20 секундами выполнения добавлено в очередь.
```

3. Завершение выполнения:
```
Команда: Сервер 2 освобождается, задание из очереди направленно на Сервер 2
Сервер 1 освобождается, задание из очереди направленно на Сервер 1
Сервер 2 завершает выполнение
Сервер 1 завершает выполнение
```

4. Просмотр состояния:
```
Состояние серверов:
Сервер 1: выполняет задание (осталось 16 сек.)
Сервер 2: выполняет задание (осталось 8 сек.)
Очередь заданий: [10]
```