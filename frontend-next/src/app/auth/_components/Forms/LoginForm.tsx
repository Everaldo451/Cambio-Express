import { useContext } from 'react'
import { CSRFContext} from '../../../../main'
import { FormThemeType } from './FormRenderer'
import { InputContainer} from '../../../../components/StyledInputLabel'
import { NLabel, NInput, SubmitInput, StyledForm, FormProps, onSubmitType } from './FormRenderer'


function LoginForm ({children,onSubmit,theme}:Pick<FormProps,"children"> & onSubmitType & FormThemeType) {

    const [csrf] = useContext(CSRFContext)

    return (
        <StyledForm action={`api/auth/login/`} method='POST' onSubmit={onSubmit}>
            {children}
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
            <input type="hidden" name='csrfmiddlewaretoken' value={csrf?csrf:""}/>
            <SubmitInput {...theme.submitProps} type='submit' value="Enter"/>
        </StyledForm>
    )

}

export default LoginForm