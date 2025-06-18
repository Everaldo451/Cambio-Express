import { ComponentProps } from 'react'
import { StyledInput } from '@/components/CommonButton'

export function AuthSubmitInput(props:ComponentProps<typeof StyledInput>) {
    return (
        <StyledInput {...props} className="mt-[40px] text-[14px]"/>
    )
}