# E-Commerce Application

## Overview
This is a full-fledged E-Commerce application built using **FastAPI** and **SQLModel** for the backend. It supports user authentication, product management, and order processing.

## Features
- **User Authentication**: Sign up, login, and secure API keys or Bearer Token (JWT)
- **Product Management**: Add, update, and delete products with images
- **Order System**: Place orders, manage and update order details
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
4. **Run the Application**
   ```sh
   uvicorn app.main:app --reload
   ```

## API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST   | `/user/createUser` | Register a new user |
| POST   | `/user/loginUser` | User login and token generation |
| POST   | `/user/updateUser` | Update User Details |
| GET    | `/user/getUser` | Get User Details, Orders, Images uploaded, Products added |
| DELETE | `/user/removeUser` | Remove the User |
| GET   | `/product/getAll` | Fetch all the products added by the user |
| GET   | `/product/retrieveProduct/{product_id}` | Retrieve the product by the product Id |
| POST   | `/product/addProduct` | Add the Products |
| DELETE   | `/product/removeProduct` | Delete the Products |
| POST   | `/product/updateProduct/{product_id}` | Update the Products |
| GET   | `/order/getAll` | Get All the orders placed by the user |
| POST   | `/order/createOrder` | Place the order |
| POST   | `/order/updateOrder/{order_id}` | Update the order |








## Future Enhancements
- Payment Gateway Integration
- Admin Panel for Order & Inventory Management
- AI-based Product Recommendations

## Contributing
Feel free to fork the repo and submit pull requests!


