import styled from "styled-components";
import { Navigate } from "react-router-dom";
import { useContext, useState } from "react";
import { UserContext } from "../../main";
import FormRenderer, {FormProps} from "./Forms";
import ChangeURL from "./ChangeURL";

const Main = styled.main`
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: ${props => props.theme.bgColor};
`

function Login() {

    const [user] = useContext(UserContext)
    const [url, setURL] = useState<FormProps['url']>("login")

    if (user) {return <Navigate to={"/"}/>}
    else {
        return (
            <Main>
                <FormRenderer url={url}>
                    <ChangeURL setURL={setURL}/>
                </FormRenderer>
            </Main>
        )
    }
}

export default Login