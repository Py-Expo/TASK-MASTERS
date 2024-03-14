# tax_calculator.py

class IndianTaxCalculator:
    def __init__(self):
        pass

    def calculate_tax(self, income):
        # Indian Income Tax Slabs for FY 2022-2023
        slabs = [(250000, 0.05), (500000, 0.1), (1000000, 0.2), (int(1e9), 0.3)]

        # Calculate tax based on income slabs
        remaining_income = income
        total_tax = 0

        for slab in slabs:
            slab_limit, slab_rate = slab
            if remaining_income > 0:
                taxable_amount = min(remaining_income, slab_limit)
                total_tax += taxable_amount * slab_rate
                remaining_income -= slab_limit

        return total_tax, income - total_tax

    def get_recommendations(self, income, tax_amount):
        recommendations = "Tax-Saving Recommendations:\n"

        # Placeholder logic for recommendations based on income and tax amount
        if income < 300000:
            recommendations += "- Consider contributing to a Public Provident Fund (PPF).\n"
            recommendations += "- Explore opening a Savings Account with a tax-saving FD option.\n"
        elif 300000 <= income < 700000:
            recommendations += "- Contribute to a tax-saving Fixed Deposit (FD) for guaranteed returns.\n"
            recommendations += "- Explore Equity Linked Savings Schemes (ELSS) for potential higher returns.\n"
            recommendations += "- Consider contributing to the National Pension System (NPS).\n"
        else:
            recommendations += "- Diversify investments by contributing to PPF, ELSS, and tax-saving FDs.\n"
            recommendations += "- Explore tax-saving options under Section 80C, including Life Insurance Premiums and Education Loans.\n"
            recommendations += "- Consider contributing to the National Pension System (NPS) for additional tax benefits.\n"

        recommendations += f"\nTotal Tax Amount: ₹{tax_amount:.2f}"

        return recommendations

# Example usage:
# calculator = IndianTaxCalculator()
# tax_amount, remaining_amount = calculator.calculate_tax(500000)
# recommendations = calculator.get_recommendations(500000, tax_amount)
# print(tax_amount, remaining_amount, recommendations)
