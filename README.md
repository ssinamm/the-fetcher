# The Fetcher

This script simply fetches books data from Openlibrary.

## What it does: (v1.0.0)
- Fetches books data from the Openlibrary search api.
- Filters to books published after year 2000.
- Limits the fetched data only to 50 books.
- Saves the results into a CSV file.

## Requirements:
- pandas==3.0.6
- requests==2.34.2

## Setup:

​```bash
git clone git@github.com:ssinamm/the-fetcher.git
cd the-fetcher
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
​```

## Usage:
​```bash
python core.py
​```

## Patch Notes: (v1.1.0)
- Now the "get" request has a 10sec timeout to avoid waiting for an endless time.
- CSV output no longer has index column.

## Patch Notes: (v1.2.4)
- Error handeling has been added to clarify some possible errors. (v1.2.x)
- Fixed : 'data' has been changed to 'books_df'. (v1.2.1)
- Fixed : 'resp' has been changed to 'response'. (v1.2.2)
- Fixed : added notes for each part to clarify what exactly is happening. (v1.2.3)
- Fixed : for 'parameters' and 'books_df.to_csv' there improvments for better readability. (v1.2.4)

## Patch Notes : (v1.3.4)
- Dropped the ```['']``` wrapper on the values across all the columns from final result.