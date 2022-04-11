def car_listing(car_prices):
  result = ""
  for car_name, price in car_prices.items():
    result += "{} costs {} dollars".format(car_name,price) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))