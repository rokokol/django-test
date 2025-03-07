#!/bin/bash

# Остановим выполнение, если какая-то команда вернётся с ошибкой
set -e

echo "⚙️  Проверяю наличие python3..."
if ! command -v python3 &> /dev/null; then
    echo "❌ python3 не найден. Установите Python 3, пожалуйста."
    exit 1
fi

echo "⚙️  Проверяю наличие docker-compose..."
if ! command -v docker-compose &> /dev/null; then
    echo "❌ docker-compose не найден. Установите docker-compose, пожалуйста."
    exit 1
fi

echo "🐍 Создаю виртуальное окружение .venv..."
python3 -m venv .venv

echo "✅ Виртуальное окружение .venv создано."

echo "🔄 Активирую .venv..."
source .venv/bin/activate

echo "📦 Устанавливаю зависимости..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🔑 Загружаю переменные окружения (если есть .env)..."
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
    echo "✅ Переменные окружения загружены."
else
    echo "⚠️ Файл .env не найден. Пропускаю загрузку переменных."
fi

echo "🐳 Запускаю сервисы через Docker Compose..."
docker-compose up -d

echo "⏳ Делаю небольшую паузу (5 секунд), чтобы PostgreSQL успел подняться..."
sleep 5

echo "🔄 Применяю миграции Django..."
python manage.py migrate

echo "🚀 Запускаю сервер разработки Django..."
python manage.py runserver

echo "✅ Всё готово! Сервер доступен по адресу http://127.0.0.1:8000"
