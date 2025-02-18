# Railway Management System API

This is a REST API for a Railway Management System, similar to IRCTC, where users can check train availability, book seats, and view booking details. The system includes two types of users: Admins (who can manage trains and seats) and Regular Users (who can check availability and book seats).

## Tech Stack
- **Web Framework**: Django
- **Database**: MySQL
- **Authentication**: JWT (JSON Web Token)
- **API Documentation**: Django REST Framework

## Features
1. **Register a User**: Users can register for an account.
2. **Login User**: Users can log into their accounts with JWT authentication.
3. **Add a New Train (Admin only)**: Admins can add new trains, including source, destination, and total seats.
4. **Get Seat Availability**: Users can check the availability of seats on trains between two stations.
5. **Book a Seat**: Users can book a seat on a specific train if availability is greater than zero.
6. **Get Specific Booking Details**: Users can retrieve details about their bookings.

## Setup Instructions

### Prerequisites

Make sure you have the following installed:
- Python 3.x
- MySQL

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/railway-management-api.git
   cd railway-management-api
