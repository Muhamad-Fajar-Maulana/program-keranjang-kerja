# PROGRAM KERANJANG BELANJA 

print('''
      =====================================
      
           PROGRAM KERANGJANG BELANJA
      
      =====================================
      ''')

foods = []
prices = []
total = 0

while True:
    food = input("Masukkan makanan yang akan dibeli (Ketik s jika sudah selesai): ")
    if food.lower() == "s":
        break
    else:
        price = float(input(f"Masukkan harga {food}: Rp"))
        foods.append(food)
        prices.append(price)
        
print("--------------------------")
print("      KERANJANG ANDA      ")
print("--------------------------")

for food in foods:
    print(food, end=" ")
    
for price in prices:
    total += price
    
print(f"Ini total semua belanjaan yang anda beli: Rp{total}")