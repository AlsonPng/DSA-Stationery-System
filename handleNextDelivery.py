import sqlite3

def handleNextDelivery(queue):
    if queue.is_empty():
        return "No deliveries available."

    # Dequeue the next delivery
    next_delivery = queue.dequeue()
    print(f"Next Delivery: Prod_id = {next_delivery.prod_id}, Quantity = {next_delivery.quantity}")

    # Ask the staff if they want to accept the delivery
    accept = input("Do you want to accept this delivery? (yes/no): ").strip().lower()

    if accept == 'yes':
        # Update the stock quantity in the database
        conn = sqlite3.connect('product.db')
        c = conn.cursor()
        c.execute('UPDATE products SET stock = stock + ? WHERE id = ?', (next_delivery.quantity, next_delivery.prod_id))
        conn.commit()
        conn.close()

        print("Delivery accepted and stock updated.")
    else:
        # Enqueue the delivery back into the queue
        queue.enqueue(next_delivery)
        print("Delivery moved to the back of the queue.")

    return f"Remaining deliveries: {len(queue)}"