import React from "react";
import { Link } from "react-router-dom";

const AdminDashboard = () => {
    return (
        <div>
            <h1>Admin Dashboard</h1>
            <nav>
                <Link to="/admin/products">Manage Products</Link> | 
                <Link to="/admin/orders">View Orders</Link> | 
                <Link to="/admin/users">Manage Users</Link>
            </nav>
        </div>
    );
};

export default AdminDashboard;
