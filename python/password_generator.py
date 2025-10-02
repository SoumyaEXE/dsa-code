"""
currency_converter.py

A simple currency converter utility.
Supports conversion between multiple currencies with fixed exchange rates.
High-quality code suitable for Hacktoberfest contribution.

Author: Soumya
Hacktoberfest 2025 Contribution
"""

from typing import Dict


# Sample exchange rates relative to USD
EXCHANGE_RATES: Dict[str, float] = {
    "USD": 1.0,
    "EUR": 0.91,
    "INR": 83.5,
    "GBP": 0.79,
    "JPY": 150.3,
    "AUD": 1.54
}


def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    """
    Convert amount from one currency to another.

    Args:
        amount (float): The amount to convert.
        from_currency (str): Source currency code (e.g., 'USD').
        to_currency (str): Target currency code (e.g., 'INR').

    Returns:
        float: Converted amount.
    """
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in EXCHANGE_RATES:
        raise ValueError(f"Unsupported source currency: {from_currency}")
    if to_currency not in EXCHANGE_RATES:
        raise ValueError(f"Unsupported target currency: {to_currency}")

    # Convert amount to USD first, then to target currency
    amount_in_usd = amount / EXCHANGE_RATES[from_currency]
    converted_amount = amount_in_usd * EXCHANGE_RATES[to_currency]
    return round(converted_amount, 2)


if __name__ == "__main__":
    print("Currency Converter Utility")
    print("Supported currencies:", ", ".join(EXCHANGE_RATES.keys()))
    
    try:
        amount = float(input("Enter amount: "))
        from_curr = input("From currency (code): ")
        to_curr = input("To currency (code): ")
        result = convert_currency(amount, from_curr, to_curr)
        print(f"{amount} {from_curr.upper()} = {result} {to_curr.upper()}")
    except ValueError as e:
        print("Error:", e)
