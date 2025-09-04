import CustomButton from "@/components/dashboard/(accounts)/[id]/CustomButton"
import AccountRouteInputContainer from "@/components/dashboard/(accounts)/[id]/styled-components/AccountRouteInputContainer"

export default function AccountConversionPage() {
    return (
        <>
            <form className="flex flex-col">
                <AccountRouteInputContainer inputAttrs={{name:"amount",id:"amout",required: true}}/>
                <AccountRouteInputContainer inputAttrs={{name:"target_account",id:"target_account",required: true}}/>
                <CustomButton>Enter</CustomButton>
            </form>
        </>
    )
}