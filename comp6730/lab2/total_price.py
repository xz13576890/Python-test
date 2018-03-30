price_of_book = 24.95
online_discount = 0.4
shipping_cost_first = 3
shipping_cost_additional = 0.75

def total_price(n):
    t_p = n*price_of_book*(1-online_discount)+3+(0.75*n)
    print(t_p)
    
    
 