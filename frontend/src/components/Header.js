import { Link } from "react-router-dom";

const Header = () => {
    return (
        <nav className="navbar navbar-dark bg-dark px-3">
            <Link className="navbar-brand" to="/">Credit Rating System</Link>
            <Link className="btn btn-primary" to="/add">Add Mortgage</Link>
        </nav>
    );
};

export default Header;
