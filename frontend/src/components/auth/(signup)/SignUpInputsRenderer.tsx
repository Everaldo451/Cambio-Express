"use client"

import { useState } from "react"

import AuthInputContainer from "../styled-components/AuthInputContainer"
import { CheckBoxDiv, CheckBoxLabel } from "../styled-components/checkboxElements"

export default function SignUpInputsRenderer(
    {children}:
    {children: React.ReactNode}
) {
    const [isCompany, setIsCompany] = useState<boolean>(false)
    return (
        <>
            {
                isCompany?
                <>
                    <AuthInputContainer inputAttrs={{name:"name",id:"name",required: true}}/>
                    <AuthInputContainer inputAttrs={{name:"CNPJ",id:"CNPJ",required: true}}/>
                </>
                :
                <AuthInputContainer inputAttrs={{name:"full_name",id:"full_name",required: true}}/>
            }
            {children}
            <CheckBoxDiv>
                <input type='checkbox' name="is_company" id="is_company" onClick={(_) => {setIsCompany(!isCompany)}}/>
                <CheckBoxLabel htmlFor='is_company'>Is Company?</CheckBoxLabel>
            </CheckBoxDiv>
        </>
    )
}