'use client' 
import { useState } from "react"

import CustomButton from "@/components/dashboard/(accounts)/[id]/CustomButton"
import AccountRouteInputContainer from "@/components/dashboard/(accounts)/[id]/styled-components/AccountRouteInputContainer"

import { AccountType } from "@/types"
import { depositIntoAccount } from "@/actions/accounts/deposit"

interface FormProps {
    id: Pick<AccountType, "id">["id"],
}
export default function Form({id}:FormProps) {
    const [error, setError] = useState<string|null>(null)

    return (
        
        <form className="flex flex-col" action={depositIntoAccount} method="POST">
            <AccountRouteInputContainer inputAttrs={{name:"amount",id:"amout",required: true}}/>
            <AccountRouteInputContainer inputAttrs={{name:"currency",id:"currency",required: true}}/>
            {error?
                <span>{error}</span>
                :null
            }
            <input type="hidden" name="id" value={id}/>
            <CustomButton>Enter</CustomButton>
        </form>
    )
}