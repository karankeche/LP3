def fractional_knapsack(values, weights, capacity):
    n = len(values)
    
    # Step 1: Calculate value/weight ratio
    ratio = [(values[i] / weights[i], values[i], weights[i]) for i in range(n)]
    
    # Step 2: Sort items by ratio in descending order
    ratio.sort(reverse=True)
    
    total_value = 0  # total value accumulated
    remaining_capacity = capacity
    
    # Step 3: Pick items greedily
    for r, value, weight in ratio:
        if remaining_capacity >= weight:
            # Take the whole item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take fraction of the item
            total_value += r * remaining_capacity
            break  # knapsack full
    
    return total_value


# Example
values = [60, 50, 40, 30, 70]
weights = [5, 3, 4, 2, 6]
capacity = 15

print("Maximum value (Fractional Knapsack):", fractional_knapsack(values, weights, capacity))
