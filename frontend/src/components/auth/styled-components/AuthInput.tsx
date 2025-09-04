import { ComponentProps } from 'react'
import Input from '@/components/globals/inputContainer/Input'

export default function AuthInput(props:ComponentProps<typeof Input>) {
    return (
        <Input {...props} className="bg-transparent text-[#BEC1C1] font-instrument-sans border-solid border-b-[2px] border-b-white"/>
    )
}