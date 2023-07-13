for i in range(2, 10, 3):
    for j in range(2, 11):
        row = []
        for k in range(i, min(i + 3, 10)):
            row.append(f"{k} x {j} = {k*j}")
        print("   ".join(row))
    print("---------------------------")
