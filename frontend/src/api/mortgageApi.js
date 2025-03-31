import axios from "axios";

const API_URL = `${process.env.REACT_APP_API_URL}/api/mortgages/`;

export const getMortgages = async () => {
    const response = await axios.get(API_URL);
    return response.data;
};

export const createMortgage = async (mortgageData) => {
    const response = await axios.post(API_URL, mortgageData);
    return response.data;
};

export const getMortgageById = async (id) => {
    const response = await axios.get(`${API_URL}${id}/`);
    return response.data;
};

export const updateMortgage = async (id, updatedData) => {
    const response = await axios.put(`${API_URL}${id}/`, updatedData);
    return response.data;
};

export const deleteMortgage = async (id) => {
    await axios.delete(`${API_URL}${id}/`);
};
