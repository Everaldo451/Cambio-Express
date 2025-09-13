'use client' 
import { useEffect, useState } from "react"

import CustomButton from "@/components/dashboard/(accounts)/[id]/CustomButton"
import AccountRouteInputContainer from "@/components/dashboard/(accounts)/[id]/styled-components/AccountRouteInputContainer"

import { transferToAnotherAccount } from "@/actions/accounts/convert"
import { AccountType } from "@/types"

interface FormProps {
    id: Pick<AccountType, "id">["id"],
    accounts: AccountType[]
}
export default function Form({id, accounts}:FormProps) {
    const [targetAccountCurrency, setTargetAccountCurrency] = useState("")
    const [targetAccountID, setTargetAccountID] = useState<number|null>(null)

    useEffect(() => {
        for (const account of accounts) {
            if (account.currency==targetAccountCurrency) {
                setTargetAccountID(account.id)
                break
            }
        }
    },[targetAccountCurrency])
    return (
        <form className="flex flex-col" action={transferToAnotherAccount}>
            <AccountRouteInputContainer inputAttrs={{name:"amount",id:"amout",required: true}}/>
            <AccountRouteInputContainer 
                inputAttrs={
                    {
                        id:"target_account",
                        required: true,
                        onInput: (e) => {setTargetAccountCurrency(e.currentTarget.value)}
                    }
                }
            />
            <input type="hidden" name="id" value={id}/>
            <input type="hidden" name="target_id" value={targetAccountID?targetAccountID:""}/>
    
            <CustomButton>Enter</CustomButton>
        </form>
    )
}