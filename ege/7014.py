if __name__ == "__main__":
    n = int(input())
    prices = []
    for _ in range(n):
        prices.append(int(input()))
    
    best_deal_days = []
    best_price = -1
    for day in range(n-1, -1, -1):
        if prices[day] > best_price:
            best_price = prices[day]
            # Note that days are stored in reverse order
            best_deal_days.append(day)

    # The following code would be cleaner if we did
    # a `prices.reverse()` before further steps;
    # I deliberately demonstrate a version that could be
    # easily written in languages without built-in
    # `reverse()` functionality (it also avoids moving data)
    best_deal_size = 0
    profit = 0
    # Fantom value hack to avoid branching in the loop 
    best_deal_days.append(-1)
    for selling_day_idx in range(len(best_deal_days) - 1):
        selling_day = best_deal_days[selling_day_idx]
        prev_selling_day = best_deal_days[selling_day_idx + 1]
        price = prices[selling_day]
        deal_size = (selling_day - prev_selling_day) * price
        profit += deal_size
        best_deal_size = max(best_deal_size, deal_size)

    print(profit, best_deal_size)
