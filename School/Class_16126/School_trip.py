#Planning trip (Comment command)
total_stud = 25
budget_per_stud = 150
has_sponsor = True

if total_stud > 20 and has_sponsor:
    bus_cost = 800
    entarnce_fee = total_stud * 25
    snacks = total_stud * 15
    total_cost = bus_cost + entarnce_fee + snacks
    cost_per_stud = total_cost / total_stud
    money_left = budget_per_stud - cost_per_stud
    print("TRIP APPROVED!")
    print(f"Bus: ${bus_cost}")
    print(f"Entrance: ${entarnce_fee}")
    print(f"Snacks: ${snacks}")
    print(f"Total Cost per Student: ${cost_per_stud:.Of}")
    print(f"You have ${money_left:.Of} left for souvernirs!")
else:
    print("Need more students or sponsor for the trip!")    