# Name: Alson Png
# Student Admin no.: 231664Q
# Tutorial Group: 5

import sqlite3

def handleNextDelivery(queue):
    if queue.is_empty():
        return "No deliveries available."

    # Dequeue the next delivery
    next_delivery = queue.dequeue()
    print(f"Next Delivery: Prod_id = {next_delivery.prod_id}, Quantity = {next_delivery.quantity}")

    # Ask the staff if they want to accept the delivery
    accept = input("Proceed with restocking (Y/N): ").strip().lower()

    if accept == 'y':
        # Update the stock quantity in the database
        conn = sqlite3.connect('product.db')
        c = conn.cursor()
        c.execute('UPDATE products SET stock = stock + ? WHERE id = ?', (next_delivery.quantity, next_delivery.prod_id))
        stock = c.execute('SELECT stock FROM products WHERE id = ?', (next_delivery.prod_id,)).fetchone()[0]
        print(f"Product {next_delivery.prod_id} updated stock: {int(stock)}")
        conn.commit()
        conn.close()
    else:
        # Enqueue the delivery back into the queue
        queue.enqueue(next_delivery)
        print("Delivery moved to the back of the queue.")

    return f"Remaining deliveries: {len(queue)}"