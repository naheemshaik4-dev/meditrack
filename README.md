# MediTrack — Medical Shop Manager

A full-stack web application for tracking medicine inventory and sales, built with Python (Flask) and HTML/CSS/JS.

## Features
- **Dashboard** — KPIs: total medicines, revenue, stock value, low-stock count
- **Medicines** — Add, edit, delete medicines with stock, price, expiry, supplier
- **Stock Alerts** — Highlights low-stock and expiring medicines
- **Sales** — Record sales (auto-deducts stock), view history with filters
- **Persistent Storage** — All data saved to `data.json`

## Setup & Run

### 1. Install dependencies
```bash
pip install flask
```

### 2. Run the app
```bash
cd medshop
python app.py
```

### 3. Open in browser
```
http://localhost:5000
```

## Project Structure
```
medshop/
├── app.py              # Flask backend (REST API)
├── data.json           # Auto-generated data store
├── templates/
│   └── index.html      # Frontend (HTML/CSS/JS)
└── README.md
```

## API Endpoints
| Method | Endpoint               | Description           |
|--------|------------------------|-----------------------|
| GET    | /api/dashboard         | Dashboard stats       |
| GET    | /api/medicines         | List all medicines    |
| POST   | /api/medicines         | Add new medicine      |
| PUT    | /api/medicines/:id     | Update medicine       |
| DELETE | /api/medicines/:id     | Delete medicine       |
| GET    | /api/sales             | List all sales        |
| POST   | /api/sales             | Record a sale         |
