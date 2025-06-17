"use client"
import { useState } from 'react'


import FormRenderer from '@/components/auth/FormRenderer'
import { InputContainer } from '@/components/StyledInputLabel'
import { AuthLabel, AuthInput, AuthSubmitInput, CheckBoxDiv, CheckBoxLabel } from '@/components/auth/styled-components'

import { theme } from '@/theme/auth'


export default function RegisterPage() {

    const [isCompany, setIsCompany] = useState<boolean>(false)

    return (
        <FormRenderer action={`/users/`} method='POST'>
                {
                    isCompany?
                    <>
                        <InputContainer
                            inputStyle={theme.inputStyle} 
                            inputAttrs={{name:"name",id:"name",required: true}}
                            InputObject={AuthInput}
                            LabelObject={AuthLabel}
                        />
                        <InputContainer 
                            inputStyle={theme.inputStyle} 
                            inputAttrs={{name:"CNPJ",id:"CNPJ",required: true}}
                            InputObject={AuthInput}
                            LabelObject={AuthLabel}
                        />
                        <InputContainer 
                            inputStyle={theme.inputStyle} 
                            inputAttrs={{name:"phone",id:"phone",required: true}}
                            InputObject={AuthInput}
                            LabelObject={AuthLabel}
                        />
                    </>
                    :
                    <InputContainer 
                        inputStyle={theme.inputStyle} 
                        inputAttrs={{name:"full_name",id:"full_name",required: true}}
                        InputObject={AuthInput}
                        LabelObject={AuthLabel}
                    />
                }
            <InputContainer 
                inputStyle={theme.inputStyle} 
                inputAttrs={{name:"email",id:"email",required: true}}
                InputObject={AuthInput}
                LabelObject={AuthLabel}
            />
            <InputContainer 
                inputStyle={theme.inputStyle} 
                inputAttrs={{name:"password",id:"password",required: true,type:"password"}}
                InputObject={AuthInput}
                LabelObject={AuthLabel}
            />
                
            <CheckBoxDiv>
                <input type='checkbox' name="is_company" id="is_company" onClick={(_) => {setIsCompany(!isCompany)}}/>
                <CheckBoxLabel htmlFor='is_company'>Is Company?</CheckBoxLabel>
            </CheckBoxDiv>
                
            <AuthSubmitInput {...theme.submitProps} type='submit' value="Enter"/>
        </FormRenderer>
    )

}