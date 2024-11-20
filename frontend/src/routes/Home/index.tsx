import styled, {ThemeProvider} from "styled-components";
import { ReactNode, useContext, useState } from "react";
import { UserContext } from "../../main";
import FeedBacks from "../../components/FeedBacks";
import APIConsumer from "./ApiConsume";
import Introduction from "./Frames/Introduction";
import WeOffer from "./Frames/PositivePoints";


function Home() {

    const [user,_] = useContext(UserContext)

    return (
        <main>
            <Introduction/>
            <WeOffer/>
            <FeedBacks/>
        </main>
    )
}


export default Home
