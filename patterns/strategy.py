from abc import ABC, abstractmethod

class CalculationStrategy(ABC):
    @abstractmethod
    def calculate(self, data):
        pass

class SimpleCostStrategy(CalculationStrategy):
    def calculate(self, data):
        # Припустимо, це простий розрахунок витрат без знижок
        return sum(item['price'] * item['quantity'] for item in data)

class DetailedCostStrategy(CalculationStrategy):
    def calculate(self, data):
        # Тут можуть бути складніші розрахунки з урахуванням знижок або податків
        total = 0
        for item in data:
            total += item['price'] * item['quantity']
            if item['quantity'] > 2:
                total -= item['price'] * 0.1  # 10% знижка на кількість більше 2
        return total

class CostCalculationStrategy:
    def __init__(self, strategy=None):
        self.strategy = strategy if strategy else SimpleCostStrategy()

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate(self, data):
        return self.strategy.calculate(data)
