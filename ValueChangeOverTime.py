# This program is intended to calculate the price of your home (or anything else)
# in the future, based off what expeced price increase or decrease has occurred
# The app does NOT collect this data by itself, you have to do that manually
import locale

locale.setlocale(locale.LC_NUMERIC,"Norwegian")

startYear = int(input("Enter start year: "))
endYear = int(input("Enter what year you intend to sell: "))
averageChange = float(
    input("Enter the average price increase/decrease in %: "))

startValue = float(input("Enter start value: "))

numYears = endYear-startYear

result = startValue*(1+(averageChange/100))**numYears


print("You can expect to sell for: " + str("{:.2f}".format(result)))


print("Format Test " + locale.format("%.0f",result,True))