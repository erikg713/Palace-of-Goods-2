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

import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Avatar, AvatarFallback } from '@/components/ui/avatar';
import { 
  LayoutDashboard, 
  Package, 
  ShoppingCart, 
  Users, 
  Settings,
  Clock
} from 'lucide-react';
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from 'recharts';

const Dashboard = () => {
  const [stats, setStats] = useState({
    productCount: 0,
    recentOrders: [],
    dailyStats: [], // For the chart
    loading: true,
    error: null
  });
  const [currentTime, setCurrentTime] = useState(new Date());
  
  const userInfo = {
    login: 'erikg713',
    role: 'Administrator',
    lastLogin: new Date().toISOString()
  };

  useEffect(() => {
    const fetchDashboardData = async () => {
      try {
        setStats(prev => ({ ...prev, loading: true }));
        // Simulated API response with daily stats
        const response = await fetch('/api/dashboard-stats');
        const data = await response.json();
        
        setStats({
          productCount: data.productCount,
          recentOrders: data.recentOrders,
          dailyStats: generateDummyDailyStats(), // In real app, this would come from API
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

  useEffect(() => {
    const timer = setInterval(() => {
      setCurrentTime(new Date());
    }, 1000);

    return () => clearInterval(timer);
  }, []);

  // Helper function to generate dummy data for the chart
  const generateDummyDailyStats = () => {
    return Array.from({ length: 7 }, (_, i) => ({
      date: new Date(Date.now() - (6 - i) * 24 * 60 * 60 * 1000).toLocaleDateString(),
      orders: Math.floor(Math.random() * 50) + 20,
      revenue: Math.floor(Math.random() * 5000) + 1000
    }));
  };

  const formatUTCDateTime = (date) => {
    return date.toISOString().replace('T', ' ').slice(0, 19);
  };

  const navigationItems = [
    { icon: <Package className="w-4 h-4" />, label: 'Products', path: '/admin/products' },
    { icon: <ShoppingCart className="w-4 h-4" />, label: 'Orders', path: '/admin/orders' },
    { icon: <Users className="w-4 h-4" />, label: 'Users', path: '/admin/users' },
    { icon: <Settings className="w-4 h-4" />, label: 'Settings', path: '/admin/settings' },
  ];

  if (stats.loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <p className="text-lg">Loading dashboard data...</p>
      </div>
    );
  }

  if (stats.error) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <p className="text-lg text-red-500">Error: {stats.error}</p>
      </div>
    );
  }

  return (
    <div className="p-6 max-w-7xl mx-auto space-y-6">
      <div className="flex justify-between items-center">
        <div className="space-y-1">
          <h2 className="text-2xl font-bold tracking-tight">Dashboard</h2>
          <div className="flex items-center text-sm text-muted-foreground">
            <Clock className="w-4 h-4 mr-1" />
            UTC: {formatUTCDateTime(currentTime)}
          </div>
        </div>
        
        <div className="flex items-center space-x-4">
          <div className="text-right">
            <p className="text-sm font-medium">{userInfo.login}</p>
            <p className="text-sm text-muted-foreground">{userInfo.role}</p>
          </div>
          <Avatar>
            <AvatarFallback>{userInfo.login.slice(0, 2).toUpperCase()}</AvatarFallback>
          </Avatar>
        </div>
      </div>

      <div className="flex space-x-4">
        {navigationItems.map((item) => (
          <Link key={item.path} to={item.path}>
            <Button variant="outline" className="w-full">
              {item.icon}
              <span className="ml-2">{item.label}</span>
            </Button>
          </Link>
        ))}
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Total Products</CardTitle>
            <Package className="w-4 h-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{stats.productCount}</div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-sm font-medium">Active Session</CardTitle>
            <Clock className="w-4 h-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <div className="text-sm text-muted-foreground">
              Since {new Date(userInfo.lastLogin).toLocaleTimeString()}
            </div>
          </CardContent>
        </Card>
      </div>

      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-7">
        <Card className="col-span-4">
          <CardHeader>
            <CardTitle>Weekly Overview</CardTitle>
          </CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={stats.dailyStats}>
                <XAxis dataKey="date" />
                <YAxis yAxisId="left" />
                <YAxis yAxisId="right" orientation="right" />
                <Tooltip />
                <Line
                  yAxisId="left"
                  type="monotone"
                  dataKey="orders"
                  stroke="#8884d8"
                  name="Orders"
                />
                <Line
                  yAxisId="right"
                  type="monotone"
                  dataKey="revenue"
                  stroke="#82ca9d"
                  name="Revenue"
                />
              </LineChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>

        <Card className="col-span-3">
          <CardHeader>
            <CardTitle>Recent Orders</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-2">
              {stats.recentOrders.map(order => (
                <div
                  key={order.id}
                  className="flex items-center justify-between p-2 rounded-lg bg-muted/50"
                >
                  <div className="flex items-center space-x-4">
                    <ShoppingCart className="w-4 h-4 text-muted-foreground" />
                    <span>#{order.id}</span>
                  </div>
                  <div className="flex items-center space-x-4">
                    <span className="font-medium">${order.total}</span>
                    <span className="text-sm text-muted-foreground">{order.status}</span>
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default Dashboard;
