# E-Commerce Application

## Overview
This is a full-fledged E-Commerce application built using **FastAPI** and **SQLModel** for the backend. It supports user authentication, product management, and order processing.

## Features
- **User Authentication**: Sign up, login, and secure API keys
- **Product Management**: Add, update, and delete products with images
- **Order System**: Place orders, manage order status, and process payments
- **Database Integration**: SQLModel for structured data management
- **API-Driven**: RESTful APIs for seamless frontend integration

## Tech Stack
- **Backend**: FastAPI, SQLModel, Pydantic
- **Database**: PostgreSQL / SQLite
- **Authentication**: JWT-based authentication
- **Storage**: Cloud-based or local storage for images
- **Deployment**: Docker, Kubernetes (optional)

## Installation
### Prerequisites
- Python 3.9+
- PostgreSQL (or SQLite for local development)
- Git

### Steps to Set Up
1. **Clone the Repository**
   ```sh
   git clone <repository-url>
   cd ecom-app
   ```
2. **Create a Virtual Environment**
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set Up Database**
   ```sh
   alembic upgrade head  # Apply migrations
   ```
5. **Run the Application**
   ```sh
   uvicorn app.main:app --reload
   ```

## API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST   | `/auth/signup` | Register a new user |
| POST   | `/auth/login` | User login and token generation |
| GET    | `/products/` | List all products |
| POST   | `/products/` | Add a new product |
| POST   | `/orders/` | Place an order |

## Future Enhancements
- Payment Gateway Integration
- Admin Panel for Order & Inventory Management
- AI-based Product Recommendations

## Contributing
Feel free to fork the repo and submit pull requests!

## License
This project is licensed under the MIT License.

