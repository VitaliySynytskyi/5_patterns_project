import json
import unittest
from unittest.mock import patch
from app import app, expenses, originator, caretaker, cost_strategy, DataAdapter, ExpenseTracker
from patterns.memento import Memento
from patterns.observer import EmailAlert, SMSAlert

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        expenses.clear()

    def test_index_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Expense Management System', response.data)

    def test_expense_submission(self):
        data = json.dumps([{"item": "Apples", "price": 1.20, "quantity": 10}])
        strategy = 'simple'
        with patch('app.base_expense_calculator') as mock_calculator:
            mock_calculator.calculate_expense.return_value = 12.0
            response = self.app.post('/', data={'expense_data': data, 'strategy': strategy})
            self.assertIn(b'Expense recorded successfully', response.data)
            self.assertEqual(len(expenses), 1)

    def test_undo_last_expense(self):
        expenses.append(10.0)
        with patch('app.originator') as mock_originator, \
             patch('app.caretaker') as mock_caretaker:
            mock_originator.get_state.return_value = 10.0
            response = self.app.post('/undo')
            self.assertIn(b'Last expense has been undone', response.data)
            self.assertEqual(len(expenses), 0)

    def test_no_expense_to_undo(self):
        with patch('app.expenses', []):
            response = self.app.post('/undo')
            self.assertIn(b'No more expenses to undo', response.data)

    def test_process_data(self):
        data = [{"item": "Apples", "price": 1.20, "quantity": 10}]
        processed_data = DataAdapter().adapt(data)
        self.assertEqual(processed_data, data)

    def test_simple_cost_strategy(self):
        data = [{"item": "Apples", "price": 1.20, "quantity": 10}]
        result = cost_strategy.calculate(data)
        self.assertEqual(result, 12.0)

    def test_detailed_cost_strategy(self):
        data = [{"item": "Apples", "price": 1.20, "quantity": 10}]
        result = cost_strategy.calculate(data)
        self.assertEqual(result, 12.0)

    def test_save_to_memento(self):
        originator.set_state(10.0)
        memento = originator.save_to_memento()
        self.assertIsInstance(memento, Memento)
        self.assertEqual(memento.get_state(), 10.0)

    def test_restore_from_memento(self):
        memento = Memento(10.0)
        originator.restore_from_memento(memento)
        self.assertEqual(originator.get_state(), 10.0)

    def test_subscribe_to_expense_tracker(self):
        alert = EmailAlert()
        expense_tracker = ExpenseTracker()
        expense_tracker.subscribe(alert)
        self.assertIn(alert, expense_tracker.observers)

    def test_unsubscribe_from_expense_tracker(self):
        alert = SMSAlert()
        expense_tracker = ExpenseTracker()
        expense_tracker.subscribe(alert)
        expense_tracker.unsubscribe(alert)
        self.assertNotIn(alert, expense_tracker.observers)

if __name__ == '__main__':
    unittest.main()
