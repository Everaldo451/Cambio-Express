import axios from "axios";

export const apiAxios = axios.create({
    baseURL: `http://${process.env.API_HOST}:${process.env.API_PORT}/api/v1/`
})