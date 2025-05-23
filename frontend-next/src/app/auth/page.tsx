import { useRouter } from "next/router";
import { useContext, useEffect, useState } from "react";
import { UserContext } from "../../main";
import FormRenderer, {FormProps} from "./_components/Forms/FormRenderer";
import ChangeFormURL from "./_components/ChangeFormURL";

function Main(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <main
            {...props}
            className={`flex flex-col align-center justify-center bg-theme`}
        >
            {props.children}
        </main>
    )
}


export default function Auth() {

    const [user, _] = useContext(UserContext)

    if (user) {
        const router = useRouter()

        useEffect(() => {
            router.push("/")
        },[router])
        return <></>
    }
    else {
        const [url, setURL] = useState<FormProps['url']>("login")
        return (
            <Main>
                <FormRenderer url={url}>
                    <ChangeFormURL setURL={setURL}/>
                </FormRenderer>
            </Main>
        )
    }
}