import json
import pytest
from flask_testing import TestCase
from app import app

class TestFlaskApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_index_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Expense Management System', response.data)


    def test_expense_submission(self):
        # Переконайтеся, що дані в тесті передаються правильно
        response = self.client.post('/', data={'expense_data': json.dumps([{"item": "Apples", "price": 1.20, "quantity": 10}]), 'strategy': 'simple'}, follow_redirects=True)
        self.assertIn(b'Expense recorded successfully', response.data)


    def test_undo_last_expense(self):
        # Adding an expense first
        # Передаємо дані як рядок JSON, якщо ваш адаптер або інша частина коду очікує рядок
        self.client.post('/', data={'expense_data': json.dumps([{"item": "Apples", "price": 1.20, "quantity": 10}]), 'strategy': 'simple'}, follow_redirects=True)
        response = self.client.post('/undo', follow_redirects=True)
        self.assertIn(b'Last expense has been undone.', response.data)


# Запуск тестів
if __name__ == '__main__':
    pytest.main()
