import styled from "styled-components";
import { Navigate } from "react-router-dom";
import { useContext } from "react";
import { UserContext } from "../../main";

function Login() {

    const [user] = useContext(UserContext)

    if (user) {return <Navigate to={"/"}/>}
    else {
        return (
            <>
            </>
        )
    }
}

export default Login