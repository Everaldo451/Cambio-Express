import CustomButton from "@/components/dashboard/(accounts)/[id]/CustomButton"
import AccountRouteInputContainer from "@/components/dashboard/(accounts)/[id]/styled-components/AccountRouteInputContainer"

import { AccountType } from "@/types"
import { authUserAxios } from "@/lib/server/authUserAxios"
import formDataToJson from "@/utils/formDataToJson"
import { useState } from "react"
import Form from "@/components/dashboard/(accounts)/[id]/(deposit)/Form"

export default async function AccountDepositPage({
    params,
}:{
    params: Promise<{id: Pick<AccountType, "id">["id"]}>,
}) {
    return (
        <Form id={(await params).id}/>
    )
}