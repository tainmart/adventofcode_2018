data = [i for i in open('input').readlines()]
data = [int(i) for i in data[0].strip().split()]

def parse_data(data):
    amt_children, amt_metadata = data[:2]
    data = data[2:]
    scores = []
    sum_metadata = 0

    for i in range(amt_children):
        metadata, score, data = parse_data(data)
        sum_metadata += metadata
        scores.append(score)

    sum_metadata += sum(data[:amt_metadata])

    if amt_children == 0:
        return (sum_metadata, sum(data[:amt_metadata]), data[amt_metadata:])
    else:
        return (
            sum_metadata,
            sum(scores[k - 1] for k in data[:amt_metadata] if k > 0 and k <= len(scores)),
            data[amt_metadata:]
        )

if __name__ == "__main__":
    total, value_root, _ = parse_data(data)
    print("Sum of all metadata entries: {:d}.".format(total))
    print("Value of the root node: {:d}.".format(value_root))