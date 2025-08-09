import AddButton from "@/components/dashboard/(accounts)/AddButton"
import AccountComponent from "@/components/dashboard/(accounts)/AccountComponent"
import { authUserAxios } from "@/lib/server/authUserAxios"

import { AccountType } from "@/types"

async function getUserAccounts() {
    try{
        const response = await authUserAxios.get('/accounts/')
        return response.data
    } catch (error) {
        return null
    }
}
export default async function AccountPage() {
    const accounts = (await getUserAccounts()) as AccountType[]
    return (
        <>
            <section className="flex p-[30px_50px] gap-[15px]">
                <h1 className="text-[24px]">Accounts</h1>
                <AddButton/>
            </section>
            <section className="flex flex-wrap p-[0_50px] gap-[10px]">
                {accounts?.map((account) => 
                    <AccountComponent 
                        id={account.id} 
                        balance={account.balance} 
                        code={account.code} 
                        key={account.id}
                    />
                )}
                <AccountComponent id={1} balance="100.00" code="USD"/>
                <AccountComponent id={2} balance="250.00" code="EUR"/>
                <AccountComponent id={3} balance="1000.00" code="BRL"/>
            </section>
        </>
    )
}