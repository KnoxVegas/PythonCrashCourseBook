guests = ['Mike', 'Jana', 'Caitlin', 'Laramie', 'Kelly']

guests.insert(0, 'Brandon')
guests.insert(3, 'Tara')
guests.append('Garry')

print(guests)

print(f"Looks like I can really only invite two folks for dinner. The table will not come in in time!")

guest1 = guests.pop(0)
print(f"Sorry {guest1}, we will have to do dinner again sometime.")
guest2 = guests.pop(0)
print(f"Sorry {guest2}, we will have to do dinner again sometime.")
guest3 = guests.pop(0)
print(f"Sorry {guest3}, we will have to do dinner again sometime.")
guest4 = guests.pop(0)
print(f"Sorry {guest4}, we will have to do dinner again sometime.")
guest5 = guests.pop(1)
print(f"Sorry {guest5}, we will have to do dinner again sometime.")
guest6 = guests.pop(2)
print(f"Sorry {guest6}, we will have to do dinner again sometime.")

print(f"Hey {guests[0]} and {guests[1]} glad you both can still make it!")

del guests[0]
del guests[0]

print(guests)