# The Fetcher

this script simply fetches books data from Openlibrary.

## What it does: (v1.0.0)
- Fetches book data from the Openlibrary search api.
- Filters to books published after year 2000.
- Limits the fetched data only to 50 books.
- Saves the results into a CSV file.

## Requirements:
- certifi==2026.7.22
- charset-normalizer==3.5.1
- idna==3.20
- numpy==2.5.3
- pandas==3.0.6
- python-dateutil==2.9.0.post0
- requests==2.34.2
- six==1.17.0
- urllib3==2.8.0

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
- Now the get request has a 10sec timeout to avoid waiting for an endless time.
- CSV output no longer has index column.

## Patch Notes: (v1.2.4)
- Error handeling has been added to clarify some possible errors. (ver 1.2.x)
- Fixed : 'data' has been changed to 'books_df'. (ver 1.2.1)
- Fixed : 'resp' has been changed to 'response'. (ver 1.2.2)
- Fixed : added notes for each part to clarify what exactly is happening. (ver 1.2.3)
- Fixed : for 'parameters' and 'books_df.to_csv' there improvments for better readability. (ver 1.2.4)