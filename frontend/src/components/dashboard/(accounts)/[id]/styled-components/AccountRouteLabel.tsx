"use client"

import { ComponentProps } from 'react'
import Label from '@/components/globals/inputContainer/Label'

export default function AccountRouteLabel(props:ComponentProps<typeof Label>) {
    return (
        <Label {...props} className='font-instrument-sans'/>
    )
}