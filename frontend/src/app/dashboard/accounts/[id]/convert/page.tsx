import CustomButton from "@/components/dashboard/(accounts)/[id]/CustomButton"
import AccountRouteInputContainer from "@/components/dashboard/(accounts)/[id]/styled-components/AccountRouteInputContainer"

import { authUserAxios } from "@/lib/server/authUserAxios"
import { transferToAnotherAccount } from "./actions"

import { AccountType } from "@/types"

export default function AccountConversionPage({
    params,
}:{
    params: Promise<{id: Pick<AccountType, "id">}>,
}) {

    return (
        <>
            <form className="flex flex-col" action={transferToAnotherAccount}>
                <AccountRouteInputContainer inputAttrs={{name:"amount",id:"amout",required: true}}/>
                <AccountRouteInputContainer inputAttrs={{name:"target_account",id:"target_account",required: true}}/>
                <CustomButton>Enter</CustomButton>
            </form>
        </>
    )
}