
# Palace of Goods

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation and Setup](#installation-and-setup)
  - [Prerequisites](#prerequisites)
  - [Steps](#steps)
- [Usage](#usage)
- [Project Directory Structure](#project-directory-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview
**Palace of Goods** is a robust e-commerce platform designed for seamless shopping experiences. It offers a user-friendly interface, advanced search features, and secure payment options. Built for scalability, it can handle thousands of products and concurrent users.

## Features
- **Dynamic Product Catalog**: Easily browse and filter thousands of items.
- **Secure Payment Gateway**: Supports multiple payment options like credit cards, PayPal, and cryptocurrencies.
- **User Accounts**: Register, log in, and manage your profile.
- **Wishlist and Cart**: Save your favorite items and manage your shopping cart.
- **Order Tracking**: Track your orders in real time.
- **Admin Dashboard**: Full control for sellers to manage products, categories, and orders.

## Tech Stack
- **Frontend**: React, Tailwind CSS
- **Backend**: Node.js, Express.js
- **Database**: MongoDB
- **Authentication**: JWT, OAuth
- **Deployment**: Vercel (frontend), Heroku (backend)

## Installation and Setup
## pip install pi-network
### Prerequisites
- Node.js (v14 or higher)
- MongoDB (Local or cloud-based like MongoDB Atlas)

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/username/palace-of-goods.git
   cd palace-of-goods
   ```

2. **Set Up the Flask Backend**
   1. Create a `backend/` folder for the Flask backend:
      ```bash
      mkdir backend
      cd backend
      ```
   2. Create a virtual environment (optional but recommended):
      ```bash
      python3 -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate
      ```
   3. Install Flask and dependencies:
      ```bash
      pip install flask flask-cors
      ```
   4. Create the required files:
      - Create `app.py`:
        ```bash
        touch app.py
        ```
      - Create `requirements.txt` to track dependencies:
        ```bash
        pip freeze > requirements.txt
        ```
   5. Add basic Flask boilerplate code in `app.py`:
      ```python
      from flask import Flask, jsonify
      from flask_cors import CORS

      app = Flask(__name__)
      CORS(app)  # Allow React frontend to make API requests during development

      @app.route('/api/items', methods=['GET'])
      def get_items():
          items = [
              {"id": 1, "name": "Golden Cup", "price": 19.99},
              {"id": 2, "name": "Silver Sword", "price": 34.99},
          ]
          return jsonify(items)

      if __name__ == "__main__":
          app.run(debug=True)
      ```
   6. Test the Flask app: Run the backend:
      ```bash
      python app.py
      ```
      Visit [http://127.0.0.1:5000/api/items](http://127.0.0.1:5000/api/items) in your browser. You should see the JSON data.

3. **Set Up the React Frontend**
   1. Go back to the project root and create a `frontend/` folder:
      ```bash
      cd ..
      npx create-react-app frontend
      ```
   2. Navigate into the `frontend/` folder:
      ```bash
      cd frontend
      ```
   3. Install Axios for making API requests:
      ```bash
      npm install axios
      ```
   4. Start the React development server:
      ```bash
      npm start
      ```
      This will launch the React app at [http://localhost:3000](http://localhost:3000).

4. **Modify React to Fetch Data From Flask**
   1. Open `src/App.js` in the `frontend/` folder and replace its contents with:
      ```javascript
      import React, { useState, useEffect } from "react";
      import axios from "axios";

      function App() {
          const [items, setItems] = useState([]);

          useEffect(() => {
              axios.get("http://127.0.0.1:5000/api/items")
                  .then(response => setItems(response.data))
                  .catch(error => console.error("Error fetching data:", error));
          }, []);

          return (
              <div>
                  <h1>Palace of Goods</h1>
                  <ul>
                      {items.map(item => (
                          <li key={item.id}>
                              {item.name} - ${item.price.toFixed(2)}
                          </li>
                      ))}
                  </ul>
              </div>
          );
      }

      export default App;
      ```
   2. Save and restart the React development server (`npm start`).
   3. Visit [http://localhost:3000](http://localhost:3000). You should see the items fetched from the Flask backend displayed.

## Project Directory Structure
At this stage, your project should look like this:
```
Palace-of-Goods/
├── backend/
│   ├── app.py               # Flask backend code
│   ├── requirements.txt     # Backend Python dependencies
│   └── venv/                # Python virtual environment (optional)
│
├── frontend/
│   ├── src/
│   │   └── App.js           # Main React component
│   ├── public/
│   ├── package.json         # Frontend dependencies
│   └── build/               # Production build of React (after `npm run build`)
│
└── README.md                # Project documentation
```

## Contributing
We welcome contributions! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
docker-compose up --build
If you're not ready to deploy yet, the focus should be on local development and testing while preparing the project structure for eventual deployment. Here's how you can continue building and testing the Palace of Goods project locally using Docker:


---

1. Local Development Setup

A. Update the docker-compose.yml for Development

For local development, ensure you can make changes and see updates without rebuilding Docker containers.

version: '3.8'

services:
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    env_file:
      - .env
    volumes:
      - ./backend:/app
    depends_on:
      - db

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
      - /app/node_modules
    environment:
      - CHOKIDAR_USEPOLLING=true

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: test_user
      POSTGRES_PASSWORD: test_password
      POSTGRES_DB: test_db
    ports:
      - "5432:5432"
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:

Key Features:

Volumes: Mounts local code into the container for live updates.

Chokidar Polling: Ensures React hot reloading works in Docker.



---

B. Development Dockerfiles

Backend

For development, use flask run instead of Gunicorn to simplify debugging.

# backend/Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

Frontend

Add CHOKIDAR_USEPOLLING for hot reloading in Docker.

# frontend/Dockerfile
FROM node:18

WORKDIR /app

COPY package.json .
RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]


---

2. Running the Development Environment

To start all services:

docker-compose up --build

Access the services:

Frontend: http://localhost:3000

Backend: http://localhost:5000

PostgreSQL: Connect at localhost:5432 with test_user and test_password.



---

3. Testing the Pi Network Integration Locally

To test Pi Network payments, use the sandbox mode. You don't need real transactions for testing.

Steps:

1. Enable Sandbox Mode in .env:

PI_SANDBOX=true
PI_API_KEY=your_test_api_key


2. Simulate Payments: Use mock transactions with the Pi SDK's sandbox tools.


3. Run Local Flask App: Test the /payment endpoint:

curl -X POST http://localhost:5000/payment \
     -H "Content-Type: application/json" \
     -d '{"tx_id": "mock_transaction_id"}'




---

4. Debugging Tools

A. Inspect Logs

Run Docker in detached mode and view logs:

docker-compose up -d
docker-compose logs -f

B. Database Access

Use a PostgreSQL client (e.g., psql or a GUI like pgAdmin):

psql -h localhost -U test_user -d test_db

C. React Debugging

Open browser dev tools to inspect the React frontend.

Use npm start directly in the frontend folder 
