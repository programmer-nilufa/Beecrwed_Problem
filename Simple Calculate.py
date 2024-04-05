def calculate_payment(product1_code, product1_units, product1_price, product2_code, product2_units, product2_price):
    total_payment = (product1_units * product1_price) + (product2_units * product2_price)
    return total_payment

def main():
    # Read input
    product1_code, product1_units, product1_price = map(float, input().split())
    product2_code, product2_units, product2_price = map(float, input().split())

    # Calculate total payment
    total_payment = calculate_payment(product1_code, product1_units, product1_price, product2_code, product2_units, product2_price)

    # Print output
    print("VALOR A PAGAR: R$ {:.2f}".format(total_payment))

if __name__ == "__main__":
    main()
