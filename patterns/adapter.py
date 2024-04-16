import json

class DataAdapter:
    def adapt(self, data, format='dict'):
        # Припускаємо, що `data` вже є Python об'єктом (наприклад, списком словників)
        # Якщо потрібно, тут можна провести додаткові трансформації
        if format == 'json':
            return json.dumps(data)
        else:
            return data
