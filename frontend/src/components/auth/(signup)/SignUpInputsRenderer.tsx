"use client"

import { useState } from "react"


import { RadioDiv, RadioLabel } from "../styled-components/radioInputElements"
import UserTypeFields from "./strategy/UserTypeFields"

interface UserTypeInputProps {
    children: React.ReactNode,
    inputProps: React.InputHTMLAttributes<React.HTMLAttributes<HTMLInputElement>>,
    setUserType: React.Dispatch<React.SetStateAction<string>>,
}
function UserTypeInput({children, inputProps, setUserType}:UserTypeInputProps) {
    return (
        <>
            <input 
                type='radio' 
                name="user_type" 
                id={inputProps.id} 
                value={inputProps.value}
                onClick={(e) => {setUserType(e.currentTarget.value)}}
            />
            <RadioLabel htmlFor={inputProps.id}>
                {children}
            </RadioLabel>
        </>
    )
}

export default function SignUpInputsRenderer(
    {children}:
    {children: React.ReactNode}
) {
    const [userType, setUserType] = useState<string>('standard')
    return (
        <>
            <UserTypeFields userType={userType}/>
            {children}
            <RadioDiv>
                <UserTypeInput 
                    inputProps={{id:'company', value: 'company'}} 
                    setUserType={setUserType}
                >
                    Company
                </UserTypeInput>
                <UserTypeInput
                    inputProps={{id:'standard', value: 'standard'}} 
                    setUserType={setUserType}
                >
                    Person
                </UserTypeInput>
            </RadioDiv>
        </>
    )
}