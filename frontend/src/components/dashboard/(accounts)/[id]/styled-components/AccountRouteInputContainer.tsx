"use client"
import { ComponentProps } from "react"

import InputContainer from "@/components/globals/inputContainer"
import AccountRouteInput from "./AccountRouteInput"
import AccountRouteLabel from "./AccountRouteLabel"

import { theme } from "@/theme/auth"

export default function AccountRouteInputContainer(
    {inputAttrs}: Pick<ComponentProps<typeof InputContainer>, "inputAttrs">
) {
    return (
        <InputContainer 
            inputAttrs={inputAttrs} 
            inputStyle={theme.inputStyle}
            InputObject={AccountRouteInput}
            LabelObject={AccountRouteLabel}
        />
    )
}