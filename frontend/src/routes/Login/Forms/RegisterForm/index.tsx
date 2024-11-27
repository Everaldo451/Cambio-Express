import React, { useState, useContext } from 'react'
import { CSRFContext } from '../../../../main'


import { FormThemeType } from '..'
import { InputContainer } from '../../../../components/StyledInputLabel'
import { NLabel, NInput, SubmitInput, StyledForm, CheckBoxDiv, FormProps, onSubmitType } from '..'


function RegisterForm ({children,url,onSubmit, theme}:FormProps & onSubmitType & FormThemeType) {

    const [csrf] = useContext(CSRFContext)
    const [isCompany, setIsCompany] = useState<boolean>(false)

    return (
        <StyledForm action={`api/auth/${url}/`} method='POST' onSubmit={onSubmit}>
            {children}
                {
                    isCompany?
                    <>
                        <InputContainer
                            inputStyle={theme.inputStyle} 
                            inputAttrs={{name:"name",id:"name",required: true}}
                            InputObject={NInput}
                            LabelObject={NLabel}
                        />
                        <InputContainer 
                            inputStyle={theme.inputStyle} 
                            inputAttrs={{name:"CNPJ",id:"CNPJ",required: true}}
                            InputObject={NInput}
                            LabelObject={NLabel}
                        />
                        <InputContainer 
                            inputStyle={theme.inputStyle} 
                            inputAttrs={{name:"phone",id:"phone",required: true}}
                            InputObject={NInput}
                            LabelObject={NLabel}
                        />
                    </>
                    :
                    <InputContainer 
                        inputStyle={theme.inputStyle} 
                        inputAttrs={{name:"full_name",id:"full_name",required: true}}
                        InputObject={NInput}
                        LabelObject={NLabel}
                    />
                }
            <InputContainer 
                inputStyle={theme.inputStyle} 
                inputAttrs={{name:"email",id:"email",required: true}}
                InputObject={NInput}
                LabelObject={NLabel}
            />
            <InputContainer 
                inputStyle={theme.inputStyle} 
                inputAttrs={{name:"password",id:"password",required: true,type:"password"}}
                InputObject={NInput}
                LabelObject={NLabel}
            />
                
            <CheckBoxDiv>
                <input type='checkbox' name="is_company" id="is_company" onClick={(e) => {setIsCompany(!isCompany)}}/>
                <label htmlFor='is_company'>Is Company?</label>
            </CheckBoxDiv>
                
            <input type="hidden" name='csrfmiddlewaretoken' value={csrf?csrf:""}/>
            <SubmitInput {...theme.submitProps} type='submit' value="Enter"/>
        </StyledForm>
    )

}

export default RegisterForm