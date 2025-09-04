import CustomButton from "@/components/dashboard/(accounts)/[id]/CustomButton"

export default function AccountInfoPage() {
    const account = {
        currency: "USD",
        balance: 250.0,
        created_at: ""

    }
    return (
        <>
            <h4>Currency: {account.currency}</h4>
            <h4>Balance: {account.balance}</h4> 
            <h4>Created At: {account.created_at}</h4>
            <CustomButton>Delete</CustomButton>
        </>
    )
}