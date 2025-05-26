import { InputContainer} from '@/components/StyledInputLabel'
import FormRenderer from '@/components/auth/FormRenderer'
import { NLabel, NInput, SubmitInput } from '@/components/auth/styled-components'
import { theme } from "@/theme/auth"


export default function LoginPage() {

    return (
        <FormRenderer action={`/auth/login/`} method='POST'>
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
        </FormRenderer>
    )

}