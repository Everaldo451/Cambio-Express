import styled from "styled-components";
import { Navigate } from "react-router-dom";
import { SetStateAction, useContext, useState } from "react";
import { UserContext } from "../../main";
import LoginForm from "./LoginForm";
import { FormProps } from "./LoginForm";
import ChangeURL from "./ChangeURL";

const Main = styled.main`
    display: flex;
    flex-direction: column;
    align-items: center;
`


function Login() {

    const [user] = useContext(UserContext)
    const [url, setURL] = useState<FormProps['url']>("login")

    if (user) {return <Navigate to={"/"}/>}
    else {
        return (
            <Main>
                <LoginForm url={url}>
                    <ChangeURL setURL={setURL}/>
                </LoginForm>
            </Main>
        )
    }
}

export default Login