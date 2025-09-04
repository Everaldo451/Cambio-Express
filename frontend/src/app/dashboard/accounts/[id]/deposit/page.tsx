import CustomButton from "@/components/dashboard/(accounts)/[id]/CustomButton"
import AccountRouteInputContainer from "@/components/dashboard/(accounts)/[id]/styled-components/AccountRouteInputContainer"

export default function AccountDepositPage() {
    return (
        <>
            <form className="flex flex-col">
                <AccountRouteInputContainer inputAttrs={{name:"amount",id:"amout",required: true}}/>
                <AccountRouteInputContainer inputAttrs={{name:"currency",id:"currency",required: true}}/>
                <CustomButton>Enter</CustomButton>
            </form>
        </>
    )
}