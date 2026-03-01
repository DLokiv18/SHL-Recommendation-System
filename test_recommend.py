from recommender.recommend import recommend

results = recommend("Java developer test")

for r in results:
    print(r)