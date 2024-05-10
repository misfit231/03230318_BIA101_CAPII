class TaxPayer:
    def __init__(self):
        self.salary_income = 0
        self.pf_gis_contributions = 0
        self.rental_income = 0
        self.dividend_income = 0
        self.dividend_interest_loans = 0
        self.other_income = 0
        self.num_children = 0
        self.education_allowance = 0
        self.life_insurance_premium = 0
        self.self_education_allowance = 0
        self.donations = 0
        self.sponsored_children = 0

    def get_income_input(self):
        self.salary_income = float(input("Enter your salary income: "))
        self.pf_gis_contributions = float(input("Enter your PF and GIS contributions: "))
        self.rental_income = float(input("Enter your rental income: "))
        self.dividend_income = float(input("Enter your dividend income: "))
        self.dividend_interest_loans = float(input("Enter interest on loans for shareholding: "))
        self.other_income = float(input("Enter your other income: "))

    def get_deduction_input(self):
        self.num_children = int(input("Enter the number of children: "))
        self.education_allowance = float(input("Enter your education allowance per child (max 350,000): "))
        self.life_insurance_premium = float(input("Enter your life insurance premium: "))
        self.self_education_allowance = float(input("Enter your self-education allowance (max 350,000): "))
        self.donations = float(input("Enter your donations: "))
        self.sponsored_children = int(input("Enter the number of sponsored children: "))

    def calculate_tax(self):
        # Specific deductions/exemptions
        salary_income_taxable = self.salary_income - self.pf_gis_contributions
        rental_income_taxable = self.rental_income * 0.8  # 20% deduction for repairs, interest, taxes, insurance
        dividend_income_taxable = max(self.dividend_income - 30000, 0)  # Nu. 30,000 exemption
        dividend_tds = 0
        if self.dividend_income > 30000:
            dividend_tds = self.dividend_income * 0.1  # 10% TDS on the whole amount
        dividend_income_taxable -= self.dividend_interest_loans
        other_income_taxable = self.other_income * 0.7  # 30% deduction on Gross Other Income

        # Total taxable income
        total_taxable_income = (
            salary_income_taxable
            + rental_income_taxable
            + dividend_income_taxable
            + other_income_taxable
        )

        # General deductions
        total_deductions = (
            min(self.education_allowance * self.num_children, 350000 * self.num_children)
            + self.life_insurance_premium
            + min(self.self_education_allowance, 350000)
            + min(self.donations, 0.05 * total_taxable_income)
            + min(self.sponsored_children * 350000, 350000 * self.sponsored_children)
        )

        net_taxable_income = total_taxable_income - total_deductions

        # Calculate tax based on tax brackets
        tax = 0
        if net_taxable_income > 1500000:
            tax += (net_taxable_income - 1500000) * 0.3
            net_taxable_income = 1500000
        if net_taxable_income > 1000000:
            tax += (net_taxable_income - 1000000) * 0.25
            net_taxable_income = 1000000
        if net_taxable_income > 650000:
            tax += (net_taxable_income - 650000) * 0.2
            net_taxable_income = 650000
        if net_taxable_income > 400000:
            tax += (net_taxable_income - 400000) * 0.15
            net_taxable_income = 400000
        if net_taxable_income > 300000:
            tax += (net_taxable_income - 300000) * 0.1

        # Apply surcharge if applicable
        if tax >= 1000000:
            tax *= 1.1

        tax += dividend_tds  # Add the TDS on dividend income

        return tax

# Example usage
taxpayer = TaxPayer()

print("Enter your income details:")
taxpayer.get_income_input()

print("\nEnter your deduction details:")
taxpayer.get_deduction_input()

tax_payable = taxpayer.calculate_tax()
print(f"\nTotal tax payable: Nu. {tax_payable:.2f}")