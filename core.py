import requests
import pandas as pd

source = "https://openlibrary.org/search.json"

parameters = {
    "q" : "first_publish_year:[2001 TO *]",
    "sort" : "random",
    "limit" : 50,
}


resp = requests.get(source, params=parameters)


raw_data = resp.json()
data = pd.DataFrame(raw_data["docs"])

data.to_csv("fetched_books_(core_v1.0.0).csv", encoding='utf-8-sig')
