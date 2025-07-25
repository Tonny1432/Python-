Arithmetic Arranger 🧮

This Python project arranges a list of arithmetic problems (addition and subtraction) vertically and side-by-side, formatted like a worksheet. 

---

🚀 Features

- Supports addition and subtraction.
- Arranges problems vertically with consistent spacing.
- Validates:
  - Only digits are used.
  - Maximum of 4 digits per number.
  - Maximum of 5 problems.
- Optional display of the answers.


 📌 Example

```python
from arithmetic_arranger import arithmetic_arranger

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
output:
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  730      3799      88      172
