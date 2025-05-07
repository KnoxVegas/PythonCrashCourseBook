guests = ['Mike', 'Jana', 'Caitlin', 'Laramie', 'Jessica']

print(f"I would love to invite you, {guests[0]} to dinner!")
print(f"I would love to invite you, {guests[1]} to dinner!")
print(f"I would love to invite you, {guests[2]} to dinner!")
print(f"I would love to invite you, {guests[3]} to dinner!")
print(f"I would love to invite you, {guests[4]} to dinner!")

print(f"Oh shoot! {guests[4]}, I'm sorry you can make it...")
# Now I'm replacing Jessica with someone else.
guests[4] = 'Kelly'
print(f"I would love to invite you, {guests[4]} to dinner!")

print(f"I'm really glad you are able to make it {guests[0]}!")
print(f"I'm really glad you are able to make it {guests[1]}!")
print(f"I'm really glad you are able to make it {guests[2]}!")
print(f"I'm really glad you are able to make it {guests[3]}!")
print(f"I'm really glad you are able to make it {guests[4]}!")