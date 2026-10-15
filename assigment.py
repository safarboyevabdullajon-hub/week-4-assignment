
def classify(weight_soup):
    if weight_soup < 148:
        return "Below range"
    elif weight_soup >= 148 and weight_soup <= 152:
        return "In range"
    else:
        return "Above average"
num_soup = int(input("Enter the number of soap bars: "))
total_weight = 0
below_range = 0
in_range = 0
above_range = 0

def calculate_average(total, count):
    return total / count
for i in range (num_soup):
        weight_soup = int(input("Eneter the weight of soup: "))
        result = classify(weight_soup)
        print(result)
        total_weight += weight_soup
        if result == "Below range":
            below_range += 1
        elif result == "In range":
            in_range += 1
        else:
            above_range += 1

average_weight = calculate_average(total_weight, num_soup)
print(f"Total weight: {total_weight} g")
print(f"Averege weight: {average_weight} g")
print(f"Below range: {below_range} g")
print(f"In range: {in_range} g")
print(f"Above range: {above_range} g")              
    

            
