"""
Author: Evan
Date: 6/9
Purpose: calculate total price given various coupons.
"""


def main():
    print("Enter item Price, your coupon amount, and the percentage reduction of your final coupon.")
    price_ = input()
    cash_c = input()
    percent_c = input()
    total_c = calculate_price(price_, cash_c, percent_c)


def calculate_price(price, cash_coupon, percent_coupon):
    if float(price) <= 0:
        print("Enter a valid price")
        exit()
    elif float(cash_coupon) > 10 or float(cash_coupon) < 0:
        print("invalid coupon")
        exit()
    if float(cash_coupon) > 0:
        total = float(price) - float(cash_coupon)
    else:
        total = float(price)
    if float(percent_coupon) > 0:
        tot = float(total) * (0+(float(percent_coupon)/100.0))
        total -= tot
    shipping = 0
    if total <= 10.0:
        shipping = 5.95
    elif total < 30.0:
        shipping = 7.95
    elif total < 50.0:
        shipping = 11.95
    tmp = total + shipping

    print("Your total cost with shipping is: ", total, "$.  Your shipping costs were: ", shipping)
    return tmp


if __name__ == '__main__':
    main()
