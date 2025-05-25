import { FormThemeType } from './FormRenderer'
import { InputContainer} from '../../../../components/StyledInputLabel'
import { FormProps, onSubmitType } from './FormRenderer'
import { NLabel, NInput, SubmitInput, StyledForm, } from './styled-components'


function LoginForm ({children,onSubmit,theme}:Pick<FormProps,"children"> & onSubmitType & FormThemeType) {

    return (
        <StyledForm action={`/auth/login/`} method='POST' onSubmit={onSubmit}>
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
            <SubmitInput {...theme.submitProps} type='submit' value="Enter"/>
        </StyledForm>
    )

}

export default LoginForm