"use client"
import { useState } from 'react'

import FormRenderer from '@/components/auth/FormRenderer'

import AuthInputContainer from '@/components/auth/styled-components/AuthInputContainer'
import { AuthSubmitInput } from '@/components/auth/styled-components/AuthSubmitButton'

import { CheckBoxDiv, CheckBoxLabel } from '@/components/auth/styled-components/checkboxElements'

import { theme } from '@/theme/auth'
import generateSubmitHandler from '../generateSubmitHandler'


export default function RegisterPage() {

    const [isCompany, setIsCompany] = useState<boolean>(false)
    return (
        <FormRenderer action={generateSubmitHandler("/users/")} method='POST'>
                {
                    isCompany?
                    <>
                        <AuthInputContainer inputAttrs={{name:"name",id:"name",required: true}}/>
                        <AuthInputContainer inputAttrs={{name:"CNPJ",id:"CNPJ",required: true}}/>
                        <AuthInputContainer inputAttrs={{name:"phone",id:"phone",required: true}}/>
                    </>
                    :
                    <AuthInputContainer inputAttrs={{name:"full_name",id:"full_name",required: true}}/>
                }
            <AuthInputContainer inputAttrs={{name:"email",id:"email",required: true}}/>
            <AuthInputContainer inputAttrs={{name:"password",id:"password",required: true,type:"password"}}/>
                
            <CheckBoxDiv>
                <input type='checkbox' name="is_company" id="is_company" onClick={(_) => {setIsCompany(!isCompany)}}/>
                <CheckBoxLabel htmlFor='is_company'>Is Company?</CheckBoxLabel>
            </CheckBoxDiv>
                
            <AuthSubmitInput {...theme.submitProps} type='submit' value="Enter"/>
        </FormRenderer>
    )

}