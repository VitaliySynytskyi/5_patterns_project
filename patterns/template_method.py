from abc import ABC, abstractmethod

class ExpenseCalculator(ABC):
    def calculate_expense(self, data, strategy):
        # Перший крок - отримання даних
        expense_data = self.process_data(data)
        # Другий крок - використання стратегії для розрахунку витрат
        result = strategy.calculate(expense_data)
        # Третій крок - логування результату
        self.log_expense(result)
        return result

    @abstractmethod
    def process_data(self, data):
        pass

    def log_expense(self, result):
        print(f"Expense logged: {result}")

class BaseExpenseCalculator(ExpenseCalculator):
    def process_data(self, data):
        # Тут припускаємо, що data вже є Python об'єктом (списком, словником)
        return data  # Просто повертаємо дані, так як вони вже в правильному форматі

