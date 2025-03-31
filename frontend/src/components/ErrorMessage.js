const ErrorMessage = ({ message }) => {
    if (!message) return null;
    
    return <p className="text-danger">{message}</p>;
};

export default ErrorMessage;
