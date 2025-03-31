import { useEffect, useState } from "react";
import { getMortgages, deleteMortgage } from "../api/mortgageApi";
import Loader from "./Loader";
import MortgageItem from "./MortgageItem";

const MortgageList = () => {
    const [mortgages, setMortgages] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        getMortgages().then(data => {
            setMortgages(data);
            setLoading(false);
        });
    }, []);

    const handleDelete = async (id) => {
        await deleteMortgage(id);
        setMortgages(mortgages.filter(m => m.id !== id));
    };

    if (loading) return <Loader />;

    return (
        <div>
            {mortgages.map(mortgage => (
                <MortgageItem key={mortgage.id} mortgage={mortgage} onDelete={handleDelete} />
            ))}
        </div>
    );
};

export default MortgageList;
