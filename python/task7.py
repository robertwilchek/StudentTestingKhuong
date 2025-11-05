
from collections import defaultdict
from orders_data import ORDERS  # reuse from Task 3

def group_totals_by_customer(orders):
    """
    Return a dict mapping 'Last, First' -> total_spent (float).
    TODO: implement
    """
    sums = defaultdict(float)

    for row in orders:
        customer_name = row.get("customer")
        key = f"{customer_name.get("last")}, {customer_name.get("first")}"

        # If customer already in dict then add previous total to current total
        sums[key] = row.get("total") + sums.get(key) if key in sums else row.get("total")

    return dict(sums)

def top_customers(sums, n=3):
    """
    Return a list of (name, total) sorted by total DESC, then name ASC.
    TODO: implement
    """
    top = []

    # Build list
    for k, v in sums.items():
        top.append((k, v))

    # Sort by total DESC
    sorted_top = sorted(top, key=lambda x:x[1], reverse=True)
    # Sort by name ASC
    sorted_top = sorted(sorted_top[:n], key=lambda x:x[0])
    
    return sorted_top

def render_html(top_list):
    """
    Return a minimal HTML string with a <ul> of 'Name — $Total'.
    TODO: implement (simple string builder is fine)
    """
    title = "Customer Spend — Top 3"
    first, second, third = top_list[0], top_list[1], top_list[2]

    html = f"""
        <!DOCTYPE html>
        <html>

        <head><title>{title}</title>
        </head>

        <h3>{title}</h3>
        <ul>
            <li>{first[0]} - ${first[1]}</li>
            <li>{second[0]} - ${second[1]}</li>
            <li>{third[0]} - ${third[1]}</li>
        </ul>
        
        </html>
    """
    return html

if __name__ == "__main__":
    sums = group_totals_by_customer(ORDERS)
    top3 = top_customers(sums, n=3)
    html = render_html(top3)
    with open("report.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Wrote report.html")