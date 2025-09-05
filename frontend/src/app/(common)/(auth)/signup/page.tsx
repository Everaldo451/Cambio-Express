import FormRenderer from '@/components/auth/FormRenderer'

import AuthInputContainer from '@/components/auth/styled-components/AuthInputContainer'
import { AuthSubmitInput } from '@/components/auth/styled-components/AuthSubmitButton'

import { theme } from '@/theme/auth'


import SignUpInputsRenderer from '@/components/auth/(signup)/SignUpInputsRenderer'
import { registerUser } from '../actions'


export default function RegisterPage() {
    return (
        <FormRenderer action={registerUser} method='POST'>
            <SignUpInputsRenderer>
                <AuthInputContainer inputAttrs={{name:"email",id:"email",required: true}}/>
                <AuthInputContainer inputAttrs={{name:"password",id:"password",required: true,type:"password"}}/>
            </SignUpInputsRenderer>
                
            <AuthSubmitInput {...theme.submitProps} type='submit' value="Enter"/>
        </FormRenderer>
    )

}