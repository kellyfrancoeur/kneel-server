ORDERS = [
    {
      "id": 1,
      "metalid": 1,
      "styleid": 2,
      "sizeid": 5, 
      "timestamp": 1614659931693
    },
    {
      "id": 2,
      "metalid": 5,
      "styleid": 1,
      "sizeid": 4,
      "timestamp": 1614659931693
    }, 
    {
      "id": 3,
      "metalid": 4,
      "styleid": 1,
      "sizeid": 3,
      "timestamp": 1614659931693
    },
    {
      "id": 4,
      "metalid": 3,
      "styleid": 2,
      "sizeid": 1,
      "timestamp": 1614659931693
    }
  ]

def get_all_orders():
    return ORDERS

def get_single_order(id):
    requested_order = None

    for order in ORDERS:
        if order["id"] == id:
            requested_order = order

    return requested_order

def create_order(order):
    # Get the id value of the last order in the list
    max_id = ORDERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the order dictionary
    order["id"] = new_id

    # Add the order dictionary to the list
    ORDERS.append(order)

    # Return the dictionary with `id` property added
    return order

def delete_order(id):
    order_index = -1

    for index, order in enumerate(ORDERS):
        if order["id"] == id:
          
            order_index = index

   
    if order_index >= 0:
        ORDERS.pop(order_index)

def update_order(id, new_order):
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break