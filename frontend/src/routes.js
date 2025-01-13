import React, { Suspense, lazy } from 'react';
import { BrowserRouter as Router, Route, Switch, Redirect } from 'react-router-dom';
import NotFound from './components/NotFound';
import Loading from './components/Loading'; // A loading component for Suspense

// Lazy load components
const Home = lazy(() => import('./components/Home'));
const Products = lazy(() => import('./components/Products'));
const Cart = lazy(() => import('./components/Cart'));
const Checkout = lazy(() => import('./components/Checkout'));
const Profile = lazy(() => import('./components/Profile'));
const Login = lazy(() => import('./components/Login'));
const Signup = lazy(() => import('./components/Signup'));

// Example of a private route component
const PrivateRoute = ({ component: Component, ...rest }) => (
    <Route
        {...rest}
        render={props =>
            localStorage.getItem('authToken') ? (
                <Component {...props} />
            ) : (
                <Redirect to="/login" />
            )
        }
    />
);

const Routes = () => {
    return (
        <Router>
            <Suspense fallback={<Loading />}>
                <Switch>
                    <Route exact path="/" component={Home} />
                    <Route path="/products" component={Products} />
                    <Route path="/cart" component={Cart} />
                    <PrivateRoute path="/checkout" component={Checkout} />
                    <PrivateRoute path="/profile" component={Profile} />
                    <Route path="/login" component={Login} />
                    <Route path="/signup" component={Signup} />
                    <Route component={NotFound} />
                </Switch>
            </Suspense>
        </Router>
    );
};

export default Routes;
