# Palace of Goods - Frontend

This is the frontend for the **Palace of Goods** project, built with React.js. The frontend provides a user-friendly interface to interact with the backend API and Pi Network payment system.

---

## **Table of Contents**
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Environment Variables](#environment-variables)
- [Available Scripts](#available-scripts)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)

---

## **Features**
- Dynamic product listing with pagination.
- User authentication (register, login, and token-based sessions).
- Integration with the Pi Network SDK for payments.
- Responsive design for mobile and desktop.
- Interacts seamlessly with the backend API.

---

## **Technologies Used**
- **React.js**: Frontend library for building user interfaces.
- **React Router**: For navigation and routing.
- **Pi Network SDK**: To enable Pi cryptocurrency payments.
- **Axios**: For HTTP requests.
- **Bootstrap/Tailwind CSS**: (Optional) For UI styling.

---

## **Setup Instructions**

### Prerequisites
1. Install [Node.js](https://nodejs.org/) (version 14.x or later).
2. Ensure the backend is running to handle API requests (refer to the backend README for setup).

### Clone the Repository
```bash
git clone https://github.com/<your-username>/Palace-of-Goods.git
cd Palace-of-Goods/frontend

Install Dependencies

npm install

Start the Development Server

npm start

The app will be available at http://localhost:3000.


---

Environment Variables

Create a .env file in the frontend/ directory and add the following variables:

# Backend API URL
REACT_APP_API_URL=http://localhost:5000

# Pi Network SDK Configuration
REACT_APP_PI_SANDBOX=true  # Use "true" for development; "false" for production
REACT_APP_PI_PUBLIC_KEY=your_pi_network_public_key


---

Available Scripts

In the project directory, you can run:

npm start

Runs the app in development mode. Open http://localhost:3000 to view it in your browser.

npm run build

Builds the app for production to the build/ folder. It bundles React in production mode and optimizes the build for the best performance.

npm test

Launches the test runner in interactive watch mode.

npm run lint

Checks the code for style and syntax errors using ESLint (if configured).


---

File Structure

frontend/
├── public/                    # Public assets (e.g., index.html)
│   └── index.html             # Main HTML template
├── src/                       # Main source folder
│   ├── components/            # Reusable React components (e.g., Header, Footer)
│   ├── pages/                 # Pages (e.g., Home, ProductDetail)
│   ├── services/              # API and Pi SDK integrations
│   ├── context/               # React Context for global state management
│   ├── App.js                 # Main app component
│   └── index.js               # Entry point for React
├── .env                       # Environment variables (not committed)
├── package.json               # Dependencies and scripts
└── README.md                  # Documentation


---

Contributing

1. Fork the repository.


2. Create a feature branch:

git checkout -b feature-name


3. Commit your changes:

git commit -m "Add feature-name"


4. Push to the branch:

git push origin feature-name


5. Open a pull request.




---

License

This project is licensed under the MIT License. See the LICENSE file for details.

---

### **Steps to Use This Template**
1. Place this `README.md` file in the `frontend/` directory.
2. Update any placeholder information, such as:
   - Replace `<your-username>` with your GitHub username.
   - Add the actual Pi Network public key in the environment variables section.
3. Ensure the setup instructions and environment variables match your project configuration.

