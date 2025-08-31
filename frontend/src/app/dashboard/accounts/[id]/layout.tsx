import { redirect } from "next/navigation";

import AccountBlackMask from "@/components/dashboard/(accounts)/[id]/AccountBlackMask";
import AccountMenu from "@/components/dashboard/(accounts)/[id]/AccountMenu";

import { authUserAxios } from "@/lib/server/authUserAxios"
import { AccountType } from "@/types"

export async function getUserAccount(id:Pick<AccountType, "id">) {
    try{
        const response = await authUserAxios.get(`/accounts/${id}`)
        return response.data
    } catch (error) {
        return null
    }
}
export default async function AccountLayout({
    params,
    children
}:{
    params: Promise<{id: Pick<AccountType, "id">}>,
    children:React.ReactNode
}) {
    const user={}

    if (!user) {
        redirect("/")
    }
    return (
        <>
            <AccountBlackMask/>
            <AccountMenu accountId={(await params).id}>
                {children}
            </AccountMenu>
       </>
    )
}