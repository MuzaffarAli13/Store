import requests
from agents import function_tool

@function_tool
def post_order_data_to_sheet(name: str, phone: str, shipping_address: str, product_name: str, quantity: int,price:int,total_price:int,status="Pending") -> str:
    """
    Posts an order entry to Google Sheet using a webhook (Google Apps Script or Pipedream).

    Args:
        name (str): Customer's full name
        phone (str): Customer's phone number
        shipping_address (str): Complete shipping address
        product_name (str): Name of the product ordered
        quantity (int): Quantity of the product
        status (str, optional): Order status (default: Pending)
        price (int)
        total_price (int total price calculate quantity)
    """

    # Replace with your actual Google Apps Script or Pipedream URL
    url = "https://script.google.com/macros/s/AKfycbzr0XFLtQf693CY01M8TGYJNz_N8oRmXmKQQn6N79YCh4GxraVCXl7jOBh9BT1bogZt/exec"

    payload = {
        "name": name,
        "phone": phone,
        "product_name": product_name,
        "shipping_address": shipping_address,
        "quantity": quantity,
        "status": status,
        "price":price,
        "total_price":total_price
    }
    
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return "✅ Order successfully submitted!"
    else:
        return f"❌ Failed to submit order. Status: {response.status_code}"
