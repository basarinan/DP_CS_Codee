def ProductPrice(lst1,lst2):
	sums = 0
	total = 0

	for i in range(len(Product_ID)):
		sums = sums + Unit_Price[i]
		total = total +1
	averageprice = sums / total
	return averageprice
Product_ID = ["Mints", "Chocolate", "Candy", "Bread"]
Unit_Price = [1,2,3,4]

print(ProductPrice(Product_ID,Unit_Price))
