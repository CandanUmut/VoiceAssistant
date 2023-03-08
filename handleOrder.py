import openai


openai.api_key = "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"


menu = {
    "bigmac": 10,
    "french fries": 5,
    "milkshake": 6,
    "chicken nuggets": 8,
    "coke": 2
}

def handle_order(order):
    # Initialize total cost
    total_cost = 0
    # Initialize list of items ordered
    items_ordered = []
    while order:
        # Split the order into the item and the quantity
        item, quantity = order.split(" ", 1)
        # Check if the item is in the menu
        if item in menu:
            # Add the item to the list of items ordered
            items_ordered.append(f"{quantity} {item}")
            # Add the cost of the item to the total cost
            total_cost += menu[item] * int(quantity)
            # Ask if the customer wants anything else
            prompt = f"Anything else? (Your order so far is {', '.join(items_ordered)} for a total of ${total_cost})"
            response = openai.Completion.create(
              model="text-davinci-002",
              prompt=prompt
            )
            order = response["choices"][0]["text"].strip()
        else:
            # Inform the customer that the item is not on the menu
            order = None
    # Print the items ordered and total cost
    print(f"Your order is {', '.join(items_ordered)} for a total of ${total_cost}")