# Museum Management System

A comprehensive university project designed with Python and PyQt5, this application offers efficient management of museum activities, bookings, user authentication, and asset tracking. It also supports ticketing and backup maintenance, adhering to modern software development principles.

---

## Technologies Used
- **Python 3.x**: Core programming language
- **PyQt5**: For building the graphical user interface
- **SQLite/Pickle**: For data persistence and storage
- **pytest**: For testing and ensuring code quality

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MColletta02/progettoingsoftware2023.git
   cd museum-management-system
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Project Structure

```plaintext
├── attivita/               # Activities management
│   ├── controller/         # Business logic for activities
│   ├── model/              # Data models for activities
│   ├── view/               # GUI components for activities
│   └── data/               # Data storage for activities
├── backupemanutenzione/    # Backup and maintenance utilities
│   ├── controller/         # Backup logic and controllers
│   └── data/               # Backup data files
├── beni/                   # Museum assets management
│   ├── controller/         # Business logic for assets
│   ├── model/              # Data models for assets
│   ├── view/               # GUI components for assets
│   └── data/               # Data storage for assets
├── biglietto/              # Ticket management
│   ├── controller/         # Logic for ticket generation
│   ├── model/              # Data models for tickets
│   └── data/               # Ticket storage
├── prenotazioni/           # Booking system
│   ├── controller/         # Booking logic
│   ├── model/              # Booking data models
│   ├── view/               # GUI components for bookings
│   └── data/               # Booking data storage
├── utente/                 # User management
│   ├── controller/         # User authentication logic
│   ├── model/              # User data models
│   └── view/               # GUI components for user management
├── UI/                     # UI resources
├── Test/                   # Unit test files
└── main.py                 # Application entry point
```

---

## Features

1. **User Authentication**: Secure login and registration system.  
2. **Activity Management**: Tools to create, update, and delete museum activities.  
3. **Booking System**: Efficient handling of reservations for museum visits.  
4. **Ticket Generation**: Generate and manage digital tickets for users.  
5. **Asset Management**: Track and organize museum artifacts seamlessly.  
6. **Backup System**: Reliable utilities for data backup and maintenance.  

---

## Running the Application

1. **Start the application**:
   ```bash
   python main.py
   ```

2. **Login or Register**:  
   Use your credentials to log in or create a new account.

---

## Testing

To run the test suite and validate the functionality:  
```bash
pytest Test/
```

---

## Development Guidelines

1. Follow the **MVC (Model-View-Controller)** design pattern.  
2. Use **PyQt5** for all graphical user interface components.  
3. Maintain **separation of concerns** between layers for cleaner code.  
4. Write **unit tests** for any new features or changes to ensure reliability.
