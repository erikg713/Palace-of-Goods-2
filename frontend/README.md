Frontend Setup

Follow the steps below to configure and run the Frontend of Palace of Goods.


---

Prerequisites

Ensure you have the following installed on your system:

Node.js (v16 or higher)

npm (v8 or higher)

Git



---

Step-by-Step Instructions

1. Clone the Repository

Clone the project repository and navigate to the frontend directory:

git clone https://github.com/username/palace-of-goods.git
cd palace-of-goods/frontend


---

2. Install Dependencies

Install all required Node.js dependencies using npm:

npm install


---

3. Configure Environment Variables

Set up environment variables by creating a .env file in the frontend directory. Use the .env.example file as a template:

cp .env.example .env

Update the following variables in the .env file:

# Backend API Base URL
REACT_APP_API_BASE_URL=http://localhost:4000/api

# Stripe Public Key
REACT_APP_STRIPE_PUBLIC_KEY=your_stripe_public_key


---

4. Start the Development Server

Start the React development server:

npm start

The frontend will be available at http://localhost:3000.


---

Project Structure

The frontend directory is structured as follows:

frontend/
├── public/                # Static assets
├── src/
│   ├── components/        # Reusable UI components
│   ├── pages/             # Page-specific components
│   ├── hooks/             # Custom React hooks
│   ├── context/           # Context API for global state
│   ├── utils/             # Utility functions
│   ├── services/          # API service functions
│   ├── styles/            # Global styles and CSS
│   ├── App.js             # Root component
│   ├── index.js           # Entry point
│   └── routes.js          # App routing
├── .env                   # Environment variables
├── package.json           # Dependencies and scripts
└── README.md              # Frontend-specific README


---

Available Scripts

npm start

Runs the app in development mode at http://localhost:3000.

npm run build

Builds the app for production in the build folder. The build is optimized for best performance.

npm run test

Launches the test runner.

npm run eject

Note: This action is irreversible. Use it to customize the build configurations.


---

API Integration

The frontend communicates with the backend through API calls. The base URL for the API is configured in the .env file:

REACT_APP_API_BASE_URL=http://localhost:4000/api

Example API Service

Here’s an example of an API service file (src/services/authService.js):

import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;

export const loginUser = async (credentials) => {
  const response = await axios.post(`${API_BASE_URL}/auth/login`, credentials);
  return response.data;
};

export const registerUser = async (userData) => {
  const response = await axios.post(`${API_BASE_URL}/auth/register`, userData);
  return response.data;
};


---

Styling

This project uses TailwindCSS for styling. Ensure TailwindCSS is installed and configured in the project:

npm install tailwindcss postcss autoprefixer
npx tailwindcss init

Update the tailwind.config.js file with the project-specific configurations.


---

Debugging

If you encounter issues:

1. Ensure the backend is running at http://localhost:4000.


2. Verify the .env file is correctly configured.


3. Check the browser console for error messages.


4. Use the React Developer Tools for debugging React components.




---

Deployment

To deploy the frontend for production:

1. Build the project:

npm run build


2. Deploy the contents of the build folder to a hosting provider like:

Vercel

Netlify

AWS S3

Firebase Hosting

