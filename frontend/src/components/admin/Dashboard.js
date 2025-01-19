import React from 'react';
import { Link } from 'react-router-dom';

const Dashboard = () => {
    return (
        <div>
            <h2>Admin Dashboard</h2>
            <nav>
                <ul>
                    <li><Link to="/admin/products">Manage Products</Link></li>
                    {/* Add more links to other admin features as needed */}
                </ul>
            </nav>
            <div>
                <h3>Statistics</h3>
                <p>Number of Products: {/* You can add code here to fetch and display the number of products */}</p>
                {/* Add more statistics as needed */}
            </div>
        </div>
    );
};

export default Dashboard;
