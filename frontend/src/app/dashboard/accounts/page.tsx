import AddButton from "@/components/dashboard/(accounts)/AddButton"
import AccountComponent from "@/components/dashboard/(accounts)/AccountComponent"
import { getUserAccounts } from "@/lib/server/getUserAccounts"

import { AccountType } from "@/types"


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
                        currency={account.currency} 
                        key={account.id}
                    />
                )}
                <AccountComponent id={1} balance="100.00" currency="USD"/>
                <AccountComponent id={2} balance="250.00" currency="EUR"/>
                <AccountComponent id={3} balance="1000.00" currency="BRL"/>
            </section>
        </>
    )
}