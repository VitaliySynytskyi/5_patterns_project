class Observer:
    def update(self, data):
        raise NotImplementedError("Subclasses should implement this!")

class ExpenseTracker(Observer):
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self, data):
        for observer in self.observers:
            observer.update(data)

class EmailAlert(Observer):
    def update(self, data):
        print(f"Email Alert: A new expense recorded: {data}")

class SMSAlert(Observer):
    def update(self, data):
        print(f"SMS Alert: A new expense recorded: {data}")
