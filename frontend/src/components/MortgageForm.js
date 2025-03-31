import { useState, useEffect } from "react";
import { createMortgage, updateMortgage, getMortgageById } from "../api/mortgageApi";
import { useNavigate, useParams } from "react-router-dom";
import ErrorMessage from "./ErrorMessage"; // Import the ErrorMessage component

const MortgageForm = () => {
    const navigate = useNavigate();
    const { id } = useParams();
    const isEditing = !!id;

    const [mortgage, setMortgage] = useState({
        credit_score: "",
        loan_amount: "",
        property_value: "",
        annual_income: "",
        debt_amount: "",
        loan_type: "fixed",
        property_type: "single_family",
    });

    const [errors, setErrors] = useState({});

    useEffect(() => {
        if (isEditing) {
            getMortgageById(id).then(data => setMortgage(data));
        }
    }, [id, isEditing]);

    const validateForm = () => {
        let newErrors = {};

        if (mortgage.credit_score < 300 || mortgage.credit_score > 850) {
            newErrors.credit_score = "Credit score must be between 300 and 850.";
        }
        if (mortgage.loan_amount <= 0) {
            newErrors.loan_amount = "Loan amount must be a positive number.";
        }
        if (mortgage.property_value <= 0) {
            newErrors.property_value = "Property value must be greater than zero.";
        }
        if (mortgage.annual_income <= 0) {
            newErrors.annual_income = "Annual income must be greater than zero.";
        }
        if (mortgage.debt_amount < 0) {
            newErrors.debt_amount = "Debt amount cannot be negative.";
        }

        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
    };

    const handleChange = (e) => {
        setMortgage({ ...mortgage, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        if (!validateForm()) return;

        if (isEditing) {
            await updateMortgage(id, mortgage);
        } else {
            await createMortgage(mortgage);
        }
        navigate("/");
    };

    return (
        <form onSubmit={handleSubmit} className="card p-4">
            <h4>{isEditing ? "Edit Mortgage" : "Add Mortgage"}</h4>

            <div className="mb-3">
                <label>Credit Score (300 - 850)</label>
                <input type="number" name="credit_score" value={mortgage.credit_score} onChange={handleChange} className="form-control" required />
                <ErrorMessage message={errors.credit_score} />
            </div>

            <div className="mb-3">
                <label>Loan Amount ($)</label>
                <input type="number" name="loan_amount" value={mortgage.loan_amount} onChange={handleChange} className="form-control" required />
                <ErrorMessage message={errors.loan_amount} />
            </div>

            <div className="mb-3">
                <label>Property Value ($)</label>
                <input type="number" name="property_value" value={mortgage.property_value} onChange={handleChange} className="form-control" required />
                <ErrorMessage message={errors.property_value} />
            </div>

            <div className="mb-3">
                <label>Annual Income ($)</label>
                <input type="number" name="annual_income" value={mortgage.annual_income} onChange={handleChange} className="form-control" required />
                <ErrorMessage message={errors.annual_income} />
            </div>

            <div className="mb-3">
                <label>Debt Amount ($)</label>
                <input type="number" name="debt_amount" value={mortgage.debt_amount} onChange={handleChange} className="form-control" required />
                <ErrorMessage message={errors.debt_amount} />
            </div>

            <div className="mb-3">
                <label>Loan Type</label>
                <select name="loan_type" value={mortgage.loan_type} onChange={handleChange} className="form-control">
                    <option value="fixed">Fixed</option>
                    <option value="adjustable">Adjustable</option>
                </select>
            </div>

            <div className="mb-3">
                <label>Property Type</label>
                <select name="property_type" value={mortgage.property_type} onChange={handleChange} className="form-control">
                    <option value="single_family">Single Family</option>
                    <option value="condo">Condo</option>
                </select>
            </div>

            <button type="submit" className="btn btn-success">{isEditing ? "Update Mortgage" : "Add Mortgage"}</button>
        </form>
    );
};

export default MortgageForm;
