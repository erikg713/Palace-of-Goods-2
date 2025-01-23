import { AuthProvider } from "./context/AuthContext";
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Marketplace from './components/Marketplace';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Marketplace />} />
            </Routes>
        </Router>
    );
}

export default App;
function App() {
  return (
    <AuthProvider>
      <Router>
        <Header />
        <main>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
          </Routes>
        </main>
        <Footer />
      </Router>
    </AuthProvider>
  );
}
