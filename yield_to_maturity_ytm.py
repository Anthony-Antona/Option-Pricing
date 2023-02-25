# -*- coding: utf-8 -*-
"""Yield to Maturity - YTM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Nzgq8x4sUvvymANvjU5ecN0qCTIaGjtR

Yield to maturity (YTM) is a common method for calculating the yield on a bond. It represents the annual rate of return that an investor can expect to earn if the bond is held until maturity and all interest payments are made on time.

The YTM calculation takes into account the bond's current market price, face value, coupon rate, and remaining time until maturity. It assumes that all coupon payments are reinvested at the same yield as the initial investment, and that the bond is held until maturity.

To calculate the YTM, the following formula can be used:

YTM = [(C + (F - P) / n) / ((F + P) / 2)] ^ (1 / n) - 1

where:

C = the annual coupon payment
F = the face value of the bond
P = the current market price of the bond
n = the number of years until maturity
The YTM calculation can be done manually or using spreadsheet software, or financial calculators. Once the YTM is calculated, it can be compared to the bond's coupon rate and current market interest rates to determine whether the bond is a good investment.
"""

# Set bond parameters
face_value = 1000
coupon_rate = 0.05
coupon_payments = 10
years_to_maturity = 5
ytm = 0.06

# Calculate coupon payment
coupon_payment = face_value * coupon_rate / coupon_payments

# Calculate present value of coupon payments
pv_coupons = 0
for i in range(1, coupon_payments + 1):
    pv_coupon = coupon_payment / (1 + ytm / coupon_payments) ** i
    pv_coupons += pv_coupon

# Calculate present value of face value payment
pv_face_value = face_value / (1 + ytm / coupon_payments) ** coupon_payments

# Calculate bond price
bond_price = pv_coupons + pv_face_value

print("Bond Price: $", round(bond_price, 2))

"""# More in deep:

The yield to maturity (YTM) is a financial measure that represents the total return anticipated on a bond if held until its maturity date. It is the internal rate of return of an investment in the bond, taking into account its price, coupon payments, and time to maturity.

The YTM is often considered the most accurate measure of a bond's return since it considers all future cash flows, including coupon payments and the final principal repayment. This differs from the current yield, which only considers the annual coupon payment as a percentage of the bond's current market price.

To calculate the YTM, you need to know the current market price of the bond, the face value or principal amount of the bond, the coupon rate, the number of years to maturity, and the frequency of coupon payments.

The YTM is calculated by solving the following equation:

P = (C / (1 + r)^1) + (C / (1 + r)^2) + ... + (C + FV) / (1 + r)^n

where:
P = current market price of the bond
C = coupon payment
r = yield to maturity
FV = face value or principal amount of the bond
n = number of years to maturity

The YTM can also be calculated using financial calculators, spreadsheet software, or specialized financial software.

In summary, the YTM is a useful measure for investors to evaluate the potential return of a bond investment over its lifetime, taking into account both the coupon payments and the final principal repayment.
"""