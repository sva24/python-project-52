### Hexlet tests and linter status:
[![Actions Status](https://github.com/sva24/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/sva24/python-project-52/actions)

# Task Manager 🚀

**Task Manager** — система управления задачами, подобная [Redmine](http://www.redmine.org/). Она позволяет эффективно ставить задачи, назначать исполнителей, изменять статусы и отслеживать прогресс. Система требует регистрации и аутентификации для работы.

## 📋 Описание

Task Manager помогает организовать работу над проектами с возможностью:
- Создания задач
- Назначения исполнителей
- Изменения статусов задач
- Просмотра и поиска задач

## 🛠️ Установка

### Запуск проекта через Poetry

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/sva24/python-project-52.git
   ```

2. Перейдите в директорию проекта:
   ```bash
   cd python-project-52
   ```

3. Установите зависимости:
   ```bash
   make install
   ```

4. Скопируйте файл `example.env` в `.env`:
   ```bash
   mv task_manager/example.env task_manager/.env
   ```

5. Отредактируйте `.env` и добавьте свои переменные окружения:
   ```bash
   SECRET_KEY=''
   DEBUG=True
   ROLLBAR_ACCESS_TOKEN=''
   POSTGRES_USER='user'
   POSTGRES_PASSWORD='password'
   POSTGRES_DB='db'
   DATABASE_URL=postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@db:5432/$POSTGRES_DB
   ```
6. Запустите проект:
   ```bash
   make run
   ```
   
### Запуск проекта через Docker:
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/sva24/python-project-52.git
   ```

2. Перейдите в директорию проекта:
   ```bash
   cd python-project-52
   ```
3. Скопируйте файл `example.env` в `.env`:
   ```bash
   mv task_manager/example.env task_manager/.env
   ```

4. Отредактируйте `.env` и добавьте свои переменные окружения:
   ```bash
   SECRET_KEY=''
   DEBUG=True
   ROLLBAR_ACCESS_TOKEN=''
   POSTGRES_USER='user'
   POSTGRES_PASSWORD='password'
   POSTGRES_DB='db'
   DATABASE_URL=postgres://$POSTGRES_USER:$POSTGRES_PASSWORD@db:5432/$POSTGRES_DB
   ```
5. Запустите проект:
   ```bash
   docker compose build
   docker compose up
   ```

## 🌟 Пример работы проекта

Вы можете ознакомиться с работой проекта по следующей ссылке:

[👉 Перейти к проекту](https://task-manager-7k6m.onrender.com)