# Read the input value
value = float(input())

# Define the available banknotes and coins
banknotes = [100, 50, 20, 10, 5, 2]
coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

# Initialize dictionaries to store the count of each banknote and coin
banknote_counts = {}
coin_counts = {}

# Calculate the count of each banknote and coin
for note in banknotes:
    count = int(value // note)
    banknote_counts[note] = count
    value -= count * note

for coin in coins:
    count = int(value // coin)
    coin_counts[coin] = count
    value -= count * coin

# Print the result
print("NOTAS:")
for note in banknotes:
    count = banknote_counts.get(note, 0)
    print(f"{count} nota(s) de R$ {note:.2f}")

print("MOEDAS:")
for coin in coins:
    count = coin_counts.get(coin, 0)
    print(f"{count} moeda(s) de R$ {coin:.2f}")
