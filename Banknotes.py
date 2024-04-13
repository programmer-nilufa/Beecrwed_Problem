value = int(input())

banknotes = [100, 50, 20, 10, 5, 2, 1]

print(value)

banknote_counts = {}

for note in banknotes:
    count = value // note
    banknote_counts[note] = count
    value %= note

for note in banknotes:
    count = banknote_counts.get(note, 0)
    print(f"{count} nota(s) de R$ {note},00")
