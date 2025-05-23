import { genericAPIConsumer } from "./genericAPIConsumer";
import axios from "axios"
import { CSRFType, UserType } from "@/types"
import { customAxios } from "./customAxios";


export const getCSRF = genericAPIConsumer<CSRFType>({
    instance: () => axios,
    configs: {
        withCredentials: true
    }
}, "/api/getcsrf/")


export const getUser = genericAPIConsumer<UserType>({
    instance: () => customAxios,
}, "/api/me/")
