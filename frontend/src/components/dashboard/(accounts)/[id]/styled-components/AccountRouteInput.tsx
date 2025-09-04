import { ComponentProps } from 'react'
import Input from '@/components/globals/inputContainer/Input'

export default function AccountRouteInput(props:ComponentProps<typeof Input>) {
    return (
        <Input {...props} className="self-start bg-transparent text-[#BEC1C1] font-instrument-sans border-solid border-[2px] border-white"/>
    )
}