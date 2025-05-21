import requests
from config import API_KEY, BASE_URL

def convert_currency(from_currency, to_currency, amount):
    try:
        url = f"{BASE_URL}/{API_KEY}/pair/{from_currency}/{to_currency}/{amount}"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and data.get("result") == "success":
            rate = data["conversion_rate"]
            converted = data["conversion_result"]
            return rate, converted
        else:
            print("❌ API error:", data.get("error-type", "Unknown error"))
            return None, None
    except Exception as e:
        print("⚠️ Network or parsing error:", e)
        return None, None
