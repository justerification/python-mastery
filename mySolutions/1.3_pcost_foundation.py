file_path = "Data/portfolio.dat"

# First attempt
# I'm reading the file, storing them then using it

with open(file_path, "r", encoding="utf-8") as file:
    stock = ""
    amount = ""
    price = ""
    final_dict = []
    ft = 0

    content = file.read().rstrip()
    new_content = (content.split("\n"))

    
    for c in new_content:
        stock = c.split(" ")[0]
        amount = int(c.split(" ")[1])
        price = float(c.split(" ")[2])
        stock_dict = {
            "Stock": stock,
            "Amount": amount,
            "Price": price
        }
        final_dict.append(stock_dict)

    for s in final_dict:
        t = s["Amount"] * s["Price"]
        ft += t

    print(f"This is the amount on my first attempt: ${ft:,.2f}")


# Second attempt
# I should be iterating as I calculate

total = 0

with open(file_path, "r") as f:
    for line in f:
        fields = line.split()
        total += int(fields[1]) * float(fields[2])
    print(f"This is the amount on my second attempt: ${ft:,.2f}")

# The learning here is that if there isn't a need to store values, don't store
