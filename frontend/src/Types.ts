import React, { SetStateAction } from "react"

export interface UserType {
    username: string,
    email: string,
}

export type UserContextType = [UserType|null, React.Dispatch<SetStateAction<UserType|null>>]

export interface CSRFType {
    csrf:string
}

export type CSRFContextType = [CSRFType|null, React.Dispatch<SetStateAction<CSRFType|null>>]
