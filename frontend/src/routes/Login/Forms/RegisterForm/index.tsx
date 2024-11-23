import React, { useState, useContext } from 'react'
import { CSRFContext } from '../../../../main'
import CommonStyleProps from '../../../../components/CommonButton'
import { InputContainer } from '../../../../components/StyledInputLabel'
import { NLabel, NInput, SubmitInput, StyledForm, CheckBoxDiv, FormProps, onSubmitType } from '..'


function RegisterForm ({children,url,onSubmit}:FormProps & onSubmitType) {

    const [csrf] = useContext(CSRFContext)
    const [isCompany, setIsCompany] = useState<boolean>(false)

    const inputStyle:React.CSSProperties= {
        paddingTop: 10,
        paddingLeft: 15,
        fontSize:15,
    }

    const submitProps:CommonStyleProps = {
        color:"white",
        hoverBg:"#2C2D52",
        borderColor:"white",
        hoverColor:"white"
    }

    return (
        <StyledForm action={`api/auth/${url}/`} method='POST' onSubmit={onSubmit}>
            {children}
                {
                    isCompany?
                    <>
                        <InputContainer
                            inputStyle={inputStyle} 
                            inputAttrs={{name:"name",id:"name",required: true}}
                            InputObject={NInput}
                            LabelObject={NLabel}
                        />
                        <InputContainer 
                            inputStyle={inputStyle} 
                            inputAttrs={{name:"CNPJ",id:"CNPJ",required: true}}
                            InputObject={NInput}
                            LabelObject={NLabel}
                        />
                        <InputContainer 
                            inputStyle={inputStyle} 
                            inputAttrs={{name:"phone",id:"phone",required: true}}
                            InputObject={NInput}
                            LabelObject={NLabel}
                        />
                    </>
                    :
                    <InputContainer 
                        inputStyle={inputStyle} 
                        inputAttrs={{name:"full_name",id:"full_name",required: true}}
                        InputObject={NInput}
                        LabelObject={NLabel}
                    />
                }
            <InputContainer 
                inputStyle={inputStyle} 
                inputAttrs={{name:"email",id:"email",required: true}}
                InputObject={NInput}
                LabelObject={NLabel}
            />
            <InputContainer 
                inputStyle={inputStyle} 
                inputAttrs={{name:"password",id:"password",required: true,type:"password"}}
                InputObject={NInput}
                LabelObject={NLabel}
            />
                
            <CheckBoxDiv>
                <input type='checkbox' name="is_company" id="is_company" onClick={(e) => {setIsCompany(!isCompany)}}/>
                <label htmlFor='is_company'>Is Company?</label>
            </CheckBoxDiv>
                
            <input type="hidden" name='csrfmiddlewaretoken' value={csrf?csrf:""}/>
            <SubmitInput {...submitProps} type='submit' value="Enter"/>
        </StyledForm>
    )

}

export default RegisterForm