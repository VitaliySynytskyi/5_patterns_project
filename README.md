Щоб тестувати вашу систему управління витратами, ви можете використовувати різні варіанти JSON-даних для різних сценаріїв. Ось кілька прикладів даних, які ви можете ввести у текстове поле на веб-сторінці вашого Flask-додатку:

### 1. Простий Приклад
Цей приклад містить основні дані про покупки трьох товарів:
```json
[
    {"item": "Apples", "price": 1.20, "quantity": 10},
    {"item": "Bananas", "price": 0.50, "quantity": 5},
    {"item": "Milk", "price": 2.00, "quantity": 2}
]
```

### 2. Деталізований Приклад зі Знижками
Цей приклад може бути використаний для перевірки деталізованої стратегії розрахунку, яка враховує знижки за певну кількість товарів:
```json
[
    {"item": "Coffee", "price": 3.50, "quantity": 1},
    {"item": "Tea", "price": 2.50, "quantity": 3},
    {"item": "Chocolate", "price": 1.75, "quantity": 5}
]
```

### 3. Приклад з Великою Кількістю Товарів
Цей приклад включає велику кількість одного товару, що може викликати застосування більших знижок або інших спеціальних умов обрахунку:
```json
[
    {"item": "Water Bottles", "price": 0.99, "quantity": 50}
]
```

### 4. Змішаний Приклад
Цей приклад містить різні товари з різною кількістю і цінами, ідеально підходить для перевірки загальної роботи системи:
```json
[
    {"item": "Bread", "price": 1.50, "quantity": 2},
    {"item": "Butter", "price": 3.50, "quantity": 1},
    {"item": "Jam", "price": 2.50, "quantity": 3},
    {"item": "Eggs", "price": 0.20, "quantity": 12}
]
```

Ці дані можуть бути використані для тестування різних аспектів вашого веб-додатку, включаючи валідацію вводу, розрахунок витрат за допомогою вибраних стратегій, а також реакцію системи на різні форми і кількості вводу. Ви можете адаптувати ці приклади або створити власні, базуючись на специфіці ваших тестових потреб.