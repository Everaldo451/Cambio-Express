import styled from "styled-components";
import { ConfigRoute } from "../page";
import { useContext } from "react";
import { UserContext } from "../../../../main";


function Seguranca() {

    const [user] = useContext(UserContext)

    return (
        <ConfigRoute>
            <p>Username: <span>{user?.first_name}</span></p>
        </ConfigRoute>
    )

}

export default Seguranca