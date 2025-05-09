train_types = ['high-speed rail', 'inter-city rail', 'rapid transit', 'freight train', 'light rail']
print(f"The first three items in the list are:\n")

print("First set of train types:")
for train1 in train_types[:3]:
    print(train1.title())

print("Second set of train types:")
for train2 in train_types[1:4]:
    print(train2.title())

print("Last set of train types:")
for train3 in train_types[-3:]:
    print(train3.title())
