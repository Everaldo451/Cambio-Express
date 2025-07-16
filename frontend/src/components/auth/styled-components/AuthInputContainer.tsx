"use client"
import { ComponentProps } from "react"

import { InputContainer } from "@/components/StyledInputLabel"
import AuthInput from "./AuthInput"
import AuthLabel from "./AuthLabel"

import { theme } from "@/theme/auth"

export default function AuthInputContainer(
    {inputAttrs}: Pick<ComponentProps<typeof InputContainer>, "inputAttrs">
) {
    return (
        <InputContainer 
            inputAttrs={inputAttrs} 
            inputStyle={theme.inputStyle}
            InputObject={AuthInput}
            LabelObject={AuthLabel}
        />
    )
}