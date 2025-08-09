export interface Company {
    name: string,
    phone: string,
    CNPJ: string
}

export interface AccountType {
    id: number,
    code: string,
    balance: string
}

export interface UserType {
    first_name: string,
    email: string,
    company: Company | null,
    money: number,
}

export type ThemeType = {
    bgColor: string,
    fontFamily: string,
    boxShadowColor: string,
    divColor: string
}

export interface TokenType {
    value: string,
    lifetime: number
}
