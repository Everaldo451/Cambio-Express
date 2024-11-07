import React, { SetStateAction } from "react"

export interface UserType {
    username: string,
    email: string,
    is_staff: boolean
}

export type UserContextType = [UserType|null, React.Dispatch<SetStateAction<UserType|null>>]

export interface JWT {
    refresh: string,
    access: string
}

export type JWTContextType = [JWT|null, React.Dispatch<SetStateAction<JWT|null>>]

export type CSRFType = string

export type CSRFContextType = [CSRFType|null, React.Dispatch<SetStateAction<CSRFType|null>>]
