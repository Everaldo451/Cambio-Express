"use client"

import { ComponentProps } from 'react'
import { Label } from '@/components/StyledInputLabel'

export default function AuthLabel(props:ComponentProps<typeof Label>) {
    return (
        <Label {...props} className='font-instrument-sans'/>
    )
}