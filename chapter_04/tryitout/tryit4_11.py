# 4-11 My Pizzas Your Pizzas
fav_pizzas = ['pepperoni', 'cheese', 'chicken bbq']
friend_pizzas = fav_pizzas[:]

fav_pizzas.append('peperoni with corn')
friend_pizzas.append('gluten free')

print("My Favorite Pizzas:")
for pizza in fav_pizzas:
    print(pizza)

print("\nMy Friends Favorite Pizzas:")
for pizza in friend_pizzas:
    print(pizza)