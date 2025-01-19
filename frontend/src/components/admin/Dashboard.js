import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

const Dashboard = () => {
    const [stats, setStats] = useState({
        productCount: 0,
        recentOrders: [],
        loading: true,
        error: null
    });
    const [currentTime, setCurrentTime] = useState(new Date());
    
    // User info - In a real application, this might come from an auth context or prop
    const userInfo = {
        login: 'erikg713',
        role: 'Administrator',
        lastLogin: new Date().toISOString()
    };

    // Fetch dashboard data
    useEffect(() => {
        const fetchDashboardData = async () => {
            try {
                setStats(prev => ({ ...prev, loading: true }));
                // Replace with your actual API endpoint
                const response = await fetch('/api/dashboard-stats');
                const data = await response.json();
                
                setStats({
                    productCount: data.productCount,
                    recentOrders: data.recentOrders,
                    loading: false,
                    error: null
                });
            } catch (error) {
                setStats(prev => ({
                    ...prev,
                    loading: false,
                    error: 'Failed to load dashboard data'
                }));
            }
        };

        fetchDashboardData();
    }, []);

    // Update time every second
    useEffect(() => {
        const timer = setInterval(() => {
            setCurrentTime(new Date());
        }, 1000);

        return () => clearInterval(timer);
    }, []);

    const formatUTCDateTime = (date) => {
        return date.toISOString().replace('T', ' ').slice(0, 19);
    };

    if (stats.loading) {
        return <div className="dashboard-loading">Loading dashboard data...</div>;
    }

    if (stats.error) {
        return <div className="dashboard-error">Error: {stats.error}</div>;
    }

    return (
        <div className="dashboard-container">
            <header className="dashboard-header">
                <div className="header-left">
                    <h2>Admin Dashboard</h2>
                    <span className="current-time">
                        UTC: {formatUTCDateTime(currentTime)}
                    </span>
                </div>
                <div className="user-info">
                    <span className="user-login">👤 {userInfo.login}</span>
                    <span className="user-role">{userInfo.role}</span>
                </div>
            </header>
            
            <nav className="dashboard-nav">
                <ul>
                    <li><Link to="/admin/products">Manage Products</Link></li>
                    <li><Link to="/admin/orders">Manage Orders</Link></li>
                    <li><Link to="/admin/users">Manage Users</Link></li>
                    <li><Link to="/admin/settings">Settings</Link></li>
                </ul>
            </nav>

            <div className="dashboard-content">
                <div className="dashboard-stats">
                    <h3>Statistics</h3>
                    <div className="stats-grid">
                        <div className="stat-card">
                            <h4>Products</h4>
                            <p className="stat-number">{stats.productCount}</p>
                        </div>
                        <div className="stat-card">
                            <h4>Active Session</h4>
                            <p className="stat-text">Since {new Date(userInfo.lastLogin).toLocaleTimeString()}</p>
                        </div>
                        {/* Add more stat cards as needed */}
                    </div>
                </div>

                <div className="recent-activity">
                    <h3>Recent Activity</h3>
                    <div className="activity-container">
                        <div className="recent-orders">
                            <h4>Latest Orders</h4>
                            <ul>
                                {stats.recentOrders.map(order => (
                                    <li key={order.id} className="order-item">
                                        <span className="order-id">#{order.id}</span>
                                        <span className="order-amount">${order.total}</span>
                                        <span className="order-status">{order.status}</span>
                                    </li>
                                ))}
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

// Add some basic styles
const styles = `
    .dashboard-container {
        padding: 20px;
        max-width: 1200px;
        margin: 0 auto;
    }

    .dashboard-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 1px solid #eee;
    }

    .current-time {
        color: #666;
        font-size: 0.9em;
        margin-left: 15px;
    }

    .user-info {
        text-align: right;
    }

    .user-login {
        font-weight: bold;
        margin-right: 10px;
    }

    .user-role {
        color: #666;
        font-size: 0.9em;
    }

    .dashboard-nav ul {
        display: flex;
        gap: 20px;
        list-style: none;
        padding: 0;
    }

    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 20px;
        margin-top: 20px;
    }

    .stat-card {
        padding: 20px;
        background: #f8f9fa;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    .stat-number {
        font-size: 24px;
        font-weight: bold;
        color: #007bff;
    }

    .activity-container {
        margin-top: 20px;
    }

    .order-item {
        display: flex;
        justify-content: space-between;
        padding: 10px;
        border-bottom: 1px solid #eee;
    }

    .dashboard-loading,
    .dashboard-error {
        text-align: center;
        padding: 40px;
        font-size: 18px;
    }
`;

// Add styles to document
const styleSheet = document.createElement("style");
styleSheet.innerText = styles;
document.head.appendChild(styleSheet);

export default Dashboard;
