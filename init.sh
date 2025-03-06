#!/bin/bash

echo "🐍 Создаю виртуальное окружение..."
python3 -m venv .venv

echo "✅ Виртуальное окружение создано."

echo "🔄 Активирую venv..."
source .venv/bin/activate

echo "📦 Устанавливаю зависимости..."
pip install --upgrade pip
pip install -r requirements.txt

echo "🔑 Загружаю переменные окружения..."
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
    echo "✅ Переменные загружены."
else
    echo "⚠️ Файл .env не найден, пропускаю загрузку переменных."
fi

echo "🚀 Всё готово! Виртуальное окружение активировано."
