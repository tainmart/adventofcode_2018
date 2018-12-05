data = [i for i in open('input').readlines()]
polymer = data[0][:-1]


if __name__ == "__main__":
    old_polymer = None
    while old_polymer != polymer:
        old_polymer = polymer
        for i in range(26):
            polymer = polymer.replace(chr(ord('a') + i) + chr(ord('A') + i), '')
            polymer = polymer.replace(chr(ord('A') + i) + chr(ord('a') + i), '')
    print("Units remaining in the polymer: {:d}".format(len(polymer)))
    print("-----------------------")

    original_polymer = polymer
    shortest_polymer = polymer
    for c in range(26):
        polymer = original_polymer
        polymer = polymer.replace(chr(ord('a') + c), '')
        polymer = polymer.replace(chr(ord('A') + c), '')
        old_polymer = None
        while old_polymer != polymer:
            old_polymer = polymer
            for i in range(26):
                polymer = polymer.replace(chr(ord('a') + i) + chr(ord('A') + i), '')
                polymer = polymer.replace(chr(ord('A') + i) + chr(ord('a') + i), '')
        shortest_polymer = polymer if len(polymer) < len(shortest_polymer) else shortest_polymer

    print("Shortest polymer possible: {:d}".format(len(shortest_polymer)))