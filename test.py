import requests

url = "https://script.google.com/macros/s/AKfycbzr0XFLtQf693CY01M8TGYJNz_N8oRmXmKQQn6N79YCh4GxraVCXl7jOBh9BT1bogZt/exec"
# url = "https://docs.google.com/spreadsheets/d/1H-CZXBiWAKAzHu6oRWDQCiLWezHxp6XnjPYA5t-nYXE/export?format=csv&gid=0"

payload = {
        "name": "Muzaffar",
        "phone": "0316227262",
        "product_name": "T Shirt",
        "shipping_address": "Karachi Pakistan",
        "quantity": 5,
        "status": "Padding",
        "price":100,
        "total_price":500
    }

response = requests.post(url,json=payload)

print("Status Code:", response.status_code)
print("Response Text:", response.text)
