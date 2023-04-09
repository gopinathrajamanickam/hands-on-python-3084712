import requests

response = requests.get(
    # "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")
    "http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?date=2021&format=json"
)

last_twenty_years = response.json()[1][:20]

for year in last_twenty_years:
    display_width = year["value"] // 10_000_000
    # print(year["date"], "=" * display_width)
    print(f'{year["date"]}: {year["value"]}', "=" * display_width)
