price: int = 100
tax: float = 1.1


def calc_price_with_tax(price: int, tax: float) -> int:
    return int(price * tax)


if __name__ == "__main__":
    print(f"{calc_price_with_tax(price, tax)}円")
