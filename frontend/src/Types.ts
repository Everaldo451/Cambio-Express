import React, { SetStateAction } from "react"

export interface UserType {
    username: string,
    email: string,
}

export type UserContextType = [UserType|null, React.Dispatch<SetStateAction<UserType|null>>]
