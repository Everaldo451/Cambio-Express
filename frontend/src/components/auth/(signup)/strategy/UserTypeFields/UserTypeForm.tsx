import { useState } from "react"

import formDataToJson from "@/utils/formDataToJson"


export default function UserTypeForm(
    {userTypeField, children}:{userTypeField:string, children:React.ReactNode}
) {
    const [fieldValue, setFieldValue] = useState("")
  
    async function handleInternalFormSubmit(e:React.FormEvent<HTMLFormElement>) {
        e.preventDefault()
    }
    async function handleInternalFormInput(e:React.FormEvent<HTMLFormElement>) {
        const formData = new FormData(e.currentTarget)
        const jsonData = formDataToJson(formData)
        setFieldValue(JSON.stringify(jsonData))
    }

    return (
        <>
            <input type="hidden" name={userTypeField} value={fieldValue}/>
            <form onInput={handleInternalFormInput} onSubmit={handleInternalFormSubmit}>
                {children}
            </form>
        </>
    )
}