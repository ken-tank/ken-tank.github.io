import os

def filter_duplicate(arr: list[str]):
    seen = []
    for a in arr:
        if (a not in seen and not a.isspace()):
            seen.append(a)
    return seen

if (not os.path.exists("app-ads.txt")):
    print("app-ads.txt not found")
    input("Press any key...")
    quit()

with open("app-ads.txt", "r") as file:
    lines = file.readlines()

filtered = filter_duplicate(lines)
final = sorted(filtered)

with open("app-ads.txt", "w") as file:
    file.writelines(final)
    
print("app-ads.txt Resolved!")
input("Pres any key...")
quit()