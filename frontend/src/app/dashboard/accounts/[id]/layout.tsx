import { redirect } from "next/navigation";

import AccountBlackMask from "@/components/dashboard/(accounts)/[id]/AccountBlackMask";
import AccountMenu from "@/components/dashboard/(accounts)/[id]/AccountMenu";

import { AccountType } from "@/types"
import { getUserAccount } from "@/lib/server/getUserAccounts";


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