import requests
import pandas as pd
import ast


# 1. Config
source = "https://openlibrary.org/search.json"

parameters = {
    "q": "first_publish_year:[2001 TO *]",
    "sort": "random",
    "limit": 50,
}


try:

    # 2. Fetching Data
    response = requests.get(
        source,
        params=parameters, 
        timeout=14
    )
    response.raise_for_status()

    # 3. Parsing Data 
    raw_data = response.json()

    # 4. Transforming Data
    books_df = pd.DataFrame(raw_data["docs"])
    books_df = books_df.map(
        lambda x: ", ".join(x) if isinstance(x, list) else x
    )

    # 5. Exporting Data
    books_df.to_csv(
        "fetched_books_(core_v1.3.4).csv",
         index=False,
         encoding="utf-8-sig"
    )

# 6. Handling Possible Erros  
except requests.exceptions.HTTPError as error:
    print(f"HTTP Error: {error}")

except requests.exceptions.RequestException as exception:
    print(f"Request Failed: {exception}")