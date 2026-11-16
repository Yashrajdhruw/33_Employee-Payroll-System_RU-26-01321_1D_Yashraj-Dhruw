"""
PS 33 - Employee Payroll System
Calculates net salary of employees and managers and saves payslips to payroll.txt
"""

OVERTIME_RATE = 200      # Rs. per overtime hour
PF_RATE = 0.12           # 12% of basic
TAX_RATE = 0.10          # 10% of gross
TAX_LIMIT = 50000        # tax applies only if gross is above this
MANAGER_BONUS_RATE = 0.10  # 10% of basic
PAYSLIP_FILE = "payroll.txt"


class Employee:
    def __init__(self, emp_id, name, basic, overtime_hours):
        self.emp_id = emp_id
        self.name = name
        self.basic = basic
        self.overtime_hours = overtime_hours

    def calculate_overtime(self):
        return self.overtime_hours * OVERTIME_RATE

    def calculate_bonus(self):
        return 0

    def calculate_gross(self):
        return self.basic + self.calculate_overtime() + self.calculate_bonus()

    def calculate_pf(self):
        return self.basic * PF_RATE

    def calculate_tax(self):
        gross = self.calculate_gross()
        return gross * TAX_RATE if gross > TAX_LIMIT else 0

    def calculate_net(self):
        return self.calculate_gross() - self.calculate_pf() - self.calculate_tax()

    def role(self):
        return "Employee"


class Manager(Employee):
    def calculate_bonus(self):
        return self.basic * MANAGER_BONUS_RATE

    def role(self):
        return "Manager"


def fmt(value):
    """Show whole numbers without decimals (e.g. 3600 instead of 3600.0)."""
    return int(value) if float(value).is_integer() else round(value, 2)


def generate_payslip(emp):
    lines = [
        "=" * 40,
        f"PAYSLIP - {emp.role()}",
        "=" * 40,
        f"ID            : {emp.emp_id}",
        f"Name          : {emp.name}",
        f"Basic         : {fmt(emp.basic)}",
        f"Overtime      : {fmt(emp.calculate_overtime())}",
    ]
    if isinstance(emp, Manager):
        lines.append(f"Bonus         : {fmt(emp.calculate_bonus())}")
    lines += [
        f"Gross         : {fmt(emp.calculate_gross())}",
        f"PF            : {fmt(emp.calculate_pf())}",
        f"Tax           : {fmt(emp.calculate_tax())}",
        f"Net Salary    : {fmt(emp.calculate_net())}",
        "=" * 40,
        "",
    ]
    return "\n".join(lines)


def print_payslip(emp):
    print("\n" + generate_payslip(emp))


def save_payslip(emp, filename=PAYSLIP_FILE):
    try:
        with open(filename, "a") as f:
            f.write(generate_payslip(emp) + "\n")
    except OSError as e:
        print(f"Error saving payslip: {e}")


# ---------- Input validation ----------
def read_basic():
    while True:
        value = input("Basic: ").strip()
        try:
            basic = float(value)
            if basic > 0:
                return basic
        except ValueError:
            pass
        print("Invalid basic salary. Enter a positive number.")


def read_overtime():
    while True:
        value = input("Overtime hours: ").strip()
        try:
            hours = float(value)
            if hours >= 0:
                return hours
        except ValueError:
            pass
        print("Invalid overtime hours. Enter a non-negative number.")


def read_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def read_role():
    while True:
        choice = input("Type (E = Employee, M = Manager): ").strip().upper()
        if choice in ("E", "M"):
            return choice
        print("Invalid choice. Enter E or M.")


def main():
    print("===== Employee Payroll System =====")
    while True:
        role = read_role()
        emp_id = read_non_empty("ID: ")
        name = read_non_empty("Name: ")
        basic = read_basic()
        overtime = read_overtime()

        emp = Manager(emp_id, name, basic, overtime) if role == "M" \
            else Employee(emp_id, name, basic, overtime)

        print_payslip(emp)
        save_payslip(emp)
        print(f"Payslip saved to {PAYSLIP_FILE}")

        again = input("\nAdd another employee? (y/n): ").strip().lower()
        if again != "y":
            break
    print("Thank you. All payslips are in", PAYSLIP_FILE)


if __name__ == "__main__":
    main()
