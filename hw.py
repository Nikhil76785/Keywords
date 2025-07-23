def calculate_due_amount(bill_amount, amount_paid):
    if amount_paid < 0 or bill_amount < 0:
        print("Invalid amounts")
        return

    while True:
        if amount_paid >= bill_amount:
            due = 0
            break
        elif amount_paid < bill_amount:
            due = bill_amount - amount_paid
            break
        else:
            pass
            continue

    return due

print(calculate_due_amount(1000, 700))