# Museum Management System

A comprehensive museum management application built with Python and PyQt5, designed to handle activities, bookings, and user management for museums.

## Technologies Used
- Python 3.x
- PyQt5
- SQLite/Pickle (for data persistence)
- pytest (for testing)

## Installation

1. Clone the repository:
git clone https://github.com/MColletta02/progettoingsoftware2023.git
cd museum-management-system


2. Install dependencies:
pip install -r requirements.txt

## Project Structure
├── attivita/               # Activities management
│   ├── controller/
│   ├── model/
│   ├── view/
│   └── data/
├── backupemanutenzione/    # Backup and maintenance
│   ├── controller/
│   └── data/
├── beni/                   # Museum assets management
│   ├── controller/
│   ├── model/
│   ├── view/
│   └── data/
├── biglietto/             # Ticket management
│   ├── controller/
│   ├── model/
│   └── data/
├── prenotazioni/          # Booking system
│   ├── controller/
│   ├── model/
│   ├── view/
│   └── data/
├── utente/                # User management
│   ├── controller/
│   ├── model/
│   └── view/
├── UI/                    # UI resources
├── Test/                  # Test files
└── main.py               # Application entry point


## Features
1. User Authentication: Login and registration system
2. Activity Management: Create, update, and delete museum activities
3. Booking System: Handle reservations for museum visits
4. Ticket Generation: Create and manage digital tickets
5. Asset Management: Track and manage museum artifacts
6. Backup System: Data backup and maintenance utilities


## Running the Application

1. Start the application:
python main.py

2. Login with your credentials or register a new account


## Testing

Run the test suite:
pytest Test/


## Development Guidelines
1. Follow MVC (Model-View-Controller) pattern
2. Use PyQt5 for all GUI components
3. Maintain separation of concerns between layers
4. Write unit tests for new features
