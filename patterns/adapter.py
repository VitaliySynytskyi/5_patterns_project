class DataAdapter:
    def adapt(self, data):
        # Цей адаптер призначений для трансформації одного формату даних у інший
        # Наприклад, з JSON у список словників, який може обробляти наша система
        import json
        return json.loads(data)  # Перетворення JSON строки у Python об'єкт
