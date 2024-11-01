import styled from "styled-components";
import { ConfigRoute } from "../..";
import { useContext } from "react";
import { UserContext } from "../../../../main";





function DadosPessoais() {

    const [user] = useContext(UserContext)

    return (
        <ConfigRoute>
            <p>Username: <span>{user?.username}</span></p>
            <p>Email: <span>{user?.email}</span></p>

            <p>Conta Empresarial:</p>
            <ul>
            </ul>
        </ConfigRoute>
    )

}

export default DadosPessoais