import requests

url = "https://api.example.com/payments"

payload = {
    "amount": 100,
    "currency": "usd", 
    "source": "tok_visa",
}
    
headers = {
    "Authorization": "Bearer sk_test_123",
    "Content-Type": "application/json",
}

response = requests.post(url, json=payload, headers=headers)