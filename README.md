# MediTrack — Medical Shop Manager

MediTrack is a Flask-based inventory and sales dashboard for managing medicines, stock levels, revenue, and expiry alerts in a small medical shop.

## Features
- Dashboard with KPIs for total medicines, inventory value, revenue, and sales count
- Medicine management: add, edit, and delete medicines
- Low-stock and expiry alerts
- Sales tracking with automatic stock deduction
- Persistent storage in a local JSON file
- Heroku-ready deployment setup via Procfile

## Requirements
- Python 3.10+
- Flask

## Setup and Run

1. Open a terminal in the project folder.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the app:

```bash
python app.py
```

4. Open the app in your browser:

```text
http://localhost:5000
```

## Project Structure

```text
medshop/
├── app.py            # Flask backend and API
├── index.html        # Front-end UI for the dashboard and forms
├── data.json         # Auto-generated application data
├── requirements.txt  # Python dependencies
├── Procfile          # Heroku deployment entry
├── README.md         # Project documentation
└── .gitignore        # Git ignore rules
```

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/dashboard | Returns summary dashboard metrics |
| GET | /api/medicines | Lists all medicines |
| POST | /api/medicines | Adds a new medicine |
| PUT | /api/medicines/:id | Updates a medicine |
| DELETE | /api/medicines/:id | Deletes a medicine |
| GET | /api/sales | Lists recent sales |
| POST | /api/sales | Records a sale |

## Notes
- The app uses the root-level [index.html](index.html) as the frontend template, not a templates folder.
- The server is configured to run on port 5000 by default, with Heroku support via the Procfile.
- If the data file does not exist, the app creates a sample medicine inventory automatically.
