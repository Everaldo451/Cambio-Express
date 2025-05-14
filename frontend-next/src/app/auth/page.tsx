import styled from "styled-components";
import { Navigate } from "react-router-dom";
import { useContext, useState } from "react";
import { UserContext } from "../../main";
import FormRenderer, {FormProps} from "./_components/Forms/FormRenderer";
import ChangeFormURL from "./_components/ChangeFormURL";

const Main = styled.main`
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: ${props => props.theme.bgColor};
`

export default function Auth() {

    const [user] = useContext(UserContext)
    const [url, setURL] = useState<FormProps['url']>("login")

    if (user) {return <Navigate to={"/"}/>}
    else {
        return (
            <Main>
                <FormRenderer url={url}>
                    <ChangeFormURL setURL={setURL}/>
                </FormRenderer>
            </Main>
        )
    }
}