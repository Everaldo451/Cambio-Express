import FormRenderer from '@/components/auth/FormRenderer'

import { AuthSubmitInput } from '@/components/auth/styled-components/AuthSubmitButton'
import AuthInputContainer from '@/components/auth/styled-components/AuthInputContainer'

import { theme } from "@/theme/auth"
import generateSubmitHandler from '../generateSubmitHandler'


export default function LoginPage() {
    return (
        <FormRenderer action={generateSubmitHandler("/auth/login/")} method='POST'>
            <AuthInputContainer inputAttrs={{name:"email",id:"email",required: true}}/>
            <AuthInputContainer inputAttrs={{name:"password",id:"password",required: true,type:"password"}}/>
            <AuthSubmitInput {...theme.submitProps} type='submit' value="Enter"/>
        </FormRenderer>
    )

}