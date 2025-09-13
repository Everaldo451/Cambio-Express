'use server'

import { redirect } from 'next/navigation'

import { authUserAxios } from '@/lib/server/authUserAxios'
import formDataToJson from '@/utils/formDataToJson'

function verifyRequiredFieldsErrors(
    formData:FormData,
    requiredFieldsAndErrorMessage:{[key:string]: string}
): [boolean, {[key:string]: string}] {
    let errorExist = false
    const errors:{[key:string]: string} = {}
    for (const [requiredField, errorMessage] of Object.entries(requiredFieldsAndErrorMessage)) {
        if (!formData.get(requiredField)) {
            errorExist = true
            errors[requiredField] = errorMessage
        }
    }
    return [errorExist, errors]
}

export async function depositIntoAccount(formData:FormData) {
    const requiredFieldsAndErrorMessage = {
        "id": "You must send an account id.",
    }
    const [errorExist, _] = verifyRequiredFieldsErrors(formData, requiredFieldsAndErrorMessage)
    if (errorExist) {
        return 
    }
    const id = formData.get("id")
    formData.delete("id")
    try {
        await authUserAxios.request({
            url: `/accounts/${id}/deposit/`,
            method: "POST",
            data: JSON.stringify(formDataToJson(formData)),
            withCredentials: true,
            headers: {
                "Content-Type": "application/json"
            }
        })
    } catch (error) {
        console.log(error)
    }
    redirect("/dashboard/accounts/")
}