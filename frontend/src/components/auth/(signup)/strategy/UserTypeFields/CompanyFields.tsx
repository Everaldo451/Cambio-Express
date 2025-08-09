import AuthInputContainer from "@/components/auth/styled-components/AuthInputContainer"
import { useEffect, useState } from "react"

export default function CompanyFields() {
    const [name, setName] = useState("")
    const [CNPJ, setCNPJ] = useState("")
    const [companyValue, setCompanyValue] = useState("")

    useEffect(() => {
        setCompanyValue(JSON.stringify({
            'name':name,
            'CNPJ':CNPJ
        }))
    },[name, CNPJ])
    return (
        <>
            <AuthInputContainer 
                inputAttrs={
                    {
                        name:"name",
                        id:"name",
                        required:false,
                        value:name,
                        onInput:(e) => {setName(e.currentTarget.value)}
                    }
                }
            />
            <AuthInputContainer 
                inputAttrs={
                    {
                        name:"CNPJ",
                        id:"CNPJ",
                        required:false,
                        value:CNPJ,
                        onInput:(e) => {setCNPJ(e.currentTarget.value)}
                    }
                }
            />
            <input type="hidden" name="company" value={companyValue} required/>
        </>
    )
}