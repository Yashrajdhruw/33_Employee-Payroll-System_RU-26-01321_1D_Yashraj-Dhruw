# PS 33 - Employee Payroll System

## Problem Statement
A Python 3 payroll program using OOP to calculate the net salary of employees and managers from basic pay, overtime and bonus, with PF and tax deductions. Payslips are saved to `payroll.txt`.

## Concepts Used
Functions, Calculations, OOP (classes, inheritance, method overriding), File Handling, Input Validation

## Rules
- Overtime = Rs. 200 x overtime hours
- Manager bonus = 10% of basic (Employee bonus = 0)
- Gross = Basic + Overtime + Bonus
- PF = 12% of Basic
- Tax = 10% of Gross if Gross > 50000, else 0
- Net = Gross - PF - Tax

## Classes
- `Employee(emp_id, name, basic, overtime_hours)` - `calculate_gross()`, `calculate_net()`, etc.
- `Manager(Employee)` - overrides `calculate_bonus()`

## How to Run
```
python payroll.py
```
Enter type (E/M), ID, name, basic and overtime hours. Choose `y` to add more employees. Every payslip is appended to `payroll.txt`.

## Test Cases
| # | Input | Result |
|---|-------|--------|
| 1 | E1 Aman, 30000, 10 hrs | Gross 32000, PF 3600, Tax 0, Net 28400 |
| 2 | E2 Neha, 10000, 0 hrs | Gross 10000, PF 1200, Tax 0, Net 8800 |
| 3a | Basic -5000 | Invalid basic salary. Enter a positive number. |
| 3b | Overtime abc | Invalid overtime hours. Enter a non-negative number. |
| 4 | Manager M1 Riya, 60000, 5 hrs | Bonus 6000, Gross 67000, PF 7200, Tax 6700, Net 53100 |

Screenshots are in the `Testcases` folder.
