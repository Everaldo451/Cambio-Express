import { genericAPIConsumer } from "./genericAPIConsumer";
import { UserType } from "@/types"
import { authUserAxios } from "@/axios/authUser";


export const getUser = genericAPIConsumer<UserType>({
    instance: () => authUserAxios,
}, "/api/me/")
