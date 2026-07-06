import requests

def get_price():
    url = "https://open.er-api.com/v6/latest/USD"

    try:
        r = requests.get(url, timeout=10)

        if r.status_code == 200:
            data = r.json()

            print("===================================")
            print("      ZF MARKET ENGINE")
            print("===================================")

            print("EUR/USD :", round(1 / data["rates"]["EUR"], 5))
            print("GBP/USD :", round(1 / data["rates"]["GBP"], 5))
            print("AUD/USD :", round(1 / data["rates"]["AUD"], 5))

            print("===================================")

        else:
            print("Gagal mengambil data.")

    except Exception as e:
        print("Error :", e)
