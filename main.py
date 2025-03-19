import database
import ui  # Проверь, чтобы был правильный импорт

# Создаём базу данных перед запуском UI
database.connect_db()

# Запускаем графический интерфейс
ui.start_app()