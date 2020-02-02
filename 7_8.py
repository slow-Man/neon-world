sandwich_oders = ['pork', 'chicken', 'vegetable']
finished_sandwiches = []

while sandwich_oders:
    making_sandwiches = sandwich_oders.pop()
    print("Now making " + making_sandwiches)
    finished_sandwiches.append(making_sandwiches)

print("\nThese sandwiches are finished:\n")
for finished in finished_sandwiches:
    print(finished)