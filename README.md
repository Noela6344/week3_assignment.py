Discount Calculator
 Description
This Python program calculates the final price of an item after applying a discount only if the discount is 20% or higher.
If the discount is less than 20%, the original price is kept. The program also includes input validation to ensure the user enters valid numbers and reasonable discount values.

 Features
Applies a discount only if it's 20% or above.

Rounds the final price to 2 decimal places.

Validates:

Price must be non-negative.

Discount percentage must be between 0 and 100.

User must enter valid numerical inputs.

How to Use
Run the Python script.

Enter the original price of the item.

Enter the discount percentage.

The program will display:

Final price if discount ≥ 20%.

No discount applied message if discount < 20%.

 Example Run
yaml
Copy
Edit
Enter the original price of the item: 1000
Enter the discount percentage: 25
Discount applied (25.0%). Final price: 750.0
yaml
Copy
Edit
Enter the original price of the item: 500
Enter the discount percentage: 10
No discount applied (discount < 20%). Price remains: 500.0
 Code Structure
calculate_discount(price, discount_percent):
Checks if the discount is ≥ 20% and returns the reduced price; otherwise returns the original price.

Input validation:

Ensures valid numbers are entered.

Rejects negative prices and out-of-range discounts.

Main Program:

Gets input from the user.

Calls calculate_discount.

Displays results.

⚙ Requirements
Python 3.x installed on your system.

 How to Run
Save the code into a file, e.g., discount_calculator.py.

Open a terminal or command prompt.

Navigate to the file location.

Run:

bash
Copy
Edit
python discount_calculator.py
