import { Link } from "react-router-dom";

const MortgageItem = ({ mortgage, onDelete }) => {
    return (
        <div className="card p-3 mb-3">
            <h5>Loan Amount: $ {mortgage.loan_amount}</h5>
            <p>Credit Score: {mortgage.credit_score}</p>
            <p>Property Value: $ {mortgage.property_value}</p>
            <p>Annual Income: $ {mortgage.annual_income}</p>
            <p>Debt Amount: $ {mortgage.debt_amount}</p>
            <p>Loan Type: {mortgage.loan_type}</p>
            <p>Property Type: {mortgage.property_type}</p>
            <p><strong>Credit Rating:</strong> {mortgage.credit_rating}</p>

            <div>
                <Link className="btn btn-warning me-2" to={`/edit/${mortgage.id}`}>Edit</Link>
                <button className="btn btn-danger" onClick={() => onDelete(mortgage.id)}>Delete</button>
            </div>
        </div>
    );
};

export default MortgageItem;
