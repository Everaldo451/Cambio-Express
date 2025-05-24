import { useState } from 'react'


import { FormThemeType } from './FormRenderer'
import { InputContainer } from '../../../../components/StyledInputLabel'
import { FormProps, onSubmitType } from './FormRenderer'
import { NLabel, NInput, SubmitInput, StyledForm, CheckBoxDiv, CheckBoxLabel } from './styled-components'


function RegisterForm ({children,onSubmit, theme}:Pick<FormProps,"children"> & onSubmitType & FormThemeType) {

    const [isCompany, setIsCompany] = useState<boolean>(false)

    return (
        <StyledForm action={`api/users/`} method='POST' onSubmit={onSubmit}>
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
                <input type='checkbox' name="is_company" id="is_company" onClick={(_) => {setIsCompany(!isCompany)}}/>
                <CheckBoxLabel htmlFor='is_company'>Is Company?</CheckBoxLabel>
            </CheckBoxDiv>
                
            <SubmitInput {...theme.submitProps} type='submit' value="Enter"/>
        </StyledForm>
    )

}

export default RegisterForm