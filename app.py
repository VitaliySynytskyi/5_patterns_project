from flask import Flask, request, render_template, redirect, url_for
from patterns.observer import ExpenseTracker, EmailAlert, SMSAlert, TelegramAlert
from patterns.strategy import SimpleCostStrategy, DetailedCostStrategy, CostCalculationStrategy
from patterns.template_method import BaseExpenseCalculator
from patterns.adapter import DataAdapter
from patterns.memento import Caretaker, Originator
import json
import datetime

app = Flask(__name__)

# Ініціалізація патернів
expense_tracker = ExpenseTracker()
expense_tracker.subscribe(EmailAlert())
expense_tracker.subscribe(SMSAlert())
expense_tracker.subscribe(TelegramAlert())
cost_strategy = CostCalculationStrategy()
base_expense_calculator = BaseExpenseCalculator()
data_adapter = DataAdapter()
originator = Originator()
caretaker = Caretaker(originator)

expenses = []  # Ліст для зберігання історії витрат

def is_summer():
    current_month = datetime.datetime.now().month
    return current_month in [6, 7, 8]

@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        expense_data = request.form.get('expense_data')
        strategy_choice = request.form.get('strategy')

        if expense_data and strategy_choice:  # Перевірка наявності обов'язкових полів
            data = json.loads(expense_data)
            adapted_data = data_adapter.adapt(data)

            if strategy_choice == 'simple':
                cost_strategy.set_strategy(SimpleCostStrategy())
            else:
                cost_strategy.set_strategy(DetailedCostStrategy())

            expense = base_expense_calculator.calculate_expense(adapted_data, cost_strategy)
            originator.set_state(expense)
            caretaker.backup()
            expense_tracker.notify(expense)
            expenses.append(expense)
            message = f"Expense recorded successfully: {expense}"
        else:
            message = "Please fill in all required fields."

    return render_template('index.html', message=message, expenses=expenses)

@app.route('/undo', methods=['POST'])
def undo_last_expense():
    if expenses:  # Перевірка, чи існують витрати для відміни
        caretaker.undo()
        expenses.pop()  # Видалення останньої записаної витрати зі списку
        message = "Last expense has been undone."
    else:
        message = "No more expenses to undo."

    return render_template('index.html', message=message, expenses=expenses)


if __name__ == '__main__':
    app.run(debug=True)
