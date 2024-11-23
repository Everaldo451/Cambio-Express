import React, { useContext } from 'react'
import { CSRFContext} from '../../../../main'
import CommonStyleProps from '../../../../components/CommonButton'
import { InputContainer} from '../../../../components/StyledInputLabel'
import { NLabel, NInput, SubmitInput, StyledForm, FormProps, onSubmitType } from '..'

function LoginForm ({children,url,onSubmit}:FormProps & onSubmitType) {

    const [csrf] = useContext(CSRFContext)

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
            <input type="hidden" name='csrfmiddlewaretoken' value={csrf?csrf:""}/>
            <SubmitInput {...submitProps} type='submit' value="Enter"/>
        </StyledForm>
    )

}

export default LoginForm