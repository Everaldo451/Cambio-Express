import { getUserAccounts } from "@/lib/server/getUserAccounts"

import { AccountType } from "@/types"
import { redirect } from "next/navigation"
import Form from "@/components/dashboard/(accounts)/[id]/(convert)/Form"

export default async function AccountConversionPage({
    params,
}:{
    params: Promise<{id: Pick<AccountType, "id">["id"]}>,
}) {
    const accounts = await getUserAccounts() || [{id: 2, balance: "100.0", currency: "USD"}]
    const id = (await params).id
    if (!accounts) {
        return redirect("/")
    }
    return <Form id={id} accounts={accounts}/>
}