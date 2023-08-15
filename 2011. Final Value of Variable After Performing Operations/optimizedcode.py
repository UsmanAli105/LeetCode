operations = ["--X","X++","X++"]
X = 0

d = {
    "X++": 1,
    "++X": 1,
    "X--": -1,
    "--X": -1,
}

print(sum([d[op] + 0 for op in operations]))    