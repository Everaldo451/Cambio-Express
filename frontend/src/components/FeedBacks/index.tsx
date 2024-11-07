import styled from "styled-components";
import { UserContext } from "../../main";
import { useContext, useState, useEffect, SetStateAction, createContext } from "react";
import { StyledInput } from "../CommonButton";
import Stars from "./Stars";
import Avatar from "../FeedBacks/assets/avatar.png"
import { customAxios } from "../../main";

const FeedBackSection = styled.section`
    background-color: lightgray;
    padding: 40px 20px;

    & > h2 {
        text-align: center;
        text-transform: uppercase;
    }
`

const FeedBackDIV = styled.div`
    border-radius: 20px;
    padding: 10px;
    border: 1px solid black;

    &:nth-child(n+1) {
        margin-top: 20px;
    }
`

const PersonDIV = styled.div`
    display: flex;
    align-items: center;
    margin-bottom: 20px;

    & > img {
        width: 30px;
        height: 30px;
        margin-right: 10px;
    }
`

const Form = styled.form`
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;

    & textarea {
        width: 100%;
        resize: none;
        margin-bottom: 20px;
        border: 1px solid black;
        min-height: 100px;
    }
`

export const StarsContext = createContext<[number,React.Dispatch<SetStateAction<number>>]>([0,() => {}])

export interface FeedBack {
    username: string,
    stars?: number,
    readonly: boolean,
    comment:string
}

function FeedBack({username,stars,readonly,comment}:FeedBack) {

    return (
        <StarsContext.Provider value={useState(stars?stars:0)}>

            <FeedBackDIV>

                <PersonDIV>
                    <img src={Avatar}/>
                    <p className="name">{username}</p>
                    <Stars readonly={readonly}/>
                </PersonDIV>

                {readonly?
                    <div className="avaliation">
                        <p>{comment}</p>
                    </div>
                    :
                    <Form method="POST" action="/api/feedbacks/set/">
                        <textarea name="comment" required></textarea>

                        <StarsContext.Consumer>
                            {context => <input type="hidden" name="stars" value={context[0]} required/>}
                        </StarsContext.Consumer>

                        <StyledInput
                            borderColor="black"
                            color="black"
                            hoverBg="rgb(150,50,0)"
                            hoverColor="white"
                         type="submit" value="Send"/>
                    </Form>
                }   

            </FeedBackDIV>
        </StarsContext.Provider>
    )
}



function FeedBacks() {

    const [user] = useContext(UserContext)
    const [feedbacks, setFeedBacks] = useState<Array<FeedBack>|null>(null)

    async function GetFeedBacks() {

        try{

            const response = await customAxios.get("/api/feedbacks/get/")

            const feedbacks = response.data

            if (feedbacks instanceof Array) {
                setFeedBacks(feedbacks.map((value) => {
                    return {...value, readonly:true}
                }))
            }

        } catch(e) {}

    }

    useEffect(() => {
        GetFeedBacks()
        console.log(feedbacks)
    },[])

    return (
        <FeedBackSection>
            <h2>FeedBacks</h2>
            {
                user && feedbacks?.filter((feedback) => feedback.username == user.username).length==0?
                    <FeedBack username={user.username} comment="adsad" readonly={false}/>
                :null
            }
            {
                feedbacks?.map((fdb) => 
                    <FeedBack username={fdb.username} stars={fdb.stars} comment={fdb.comment} readonly={fdb.readonly}/>
                )   
            }
            <FeedBack username={"João"} stars={3} comment="adsad" readonly={true}/>
        </FeedBackSection>
    )
}

export default FeedBacks