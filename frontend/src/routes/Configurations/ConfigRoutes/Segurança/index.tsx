import styled from "styled-components";
import { ConfigRoute } from "../..";
import { useContext } from "react";
import { UserContext } from "../../../../main";


function Seguranca() {

    const [user] = useContext(UserContext)

    return (
        <ConfigRoute>
            <p>Username: <span>{user?.username}</span></p>
        </ConfigRoute>
    )

}

export default Seguranca