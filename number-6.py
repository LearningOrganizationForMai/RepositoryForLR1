scores = {"Alice": 85, "Bob": 90}
scores["Charlie"] = 78
scores["Bob"] = 95
print(scores)
balls = scores.get("Dave")
print(balls)
print(scores.get("Bob"))
del scores["Alice"]
print(scores)
print(len(scores))
print(scores.keys(), scores.values())