import { InputContainer} from '@/components/StyledInputLabel'
import FormRenderer from '@/components/auth/FormRenderer'
import { AuthLabel, AuthInput, AuthSubmitInput } from '@/components/auth/styled-components'
import { theme } from "@/theme/auth"


export default function LoginPage() {

    return (
        <FormRenderer action={`/auth/login/`} method='POST'>
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
            <AuthSubmitInput {...theme.submitProps} type='submit' value="Enter"/>
        </FormRenderer>
    )

}