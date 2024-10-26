import styled from "styled-components";
import { UserContext } from "../../main";
import { ReactNode, useContext, useState, useEffect, SetStateAction, createContext } from "react";
import Stars from "./Stars";
import Avatar from "../FeedBacks/assets/avatar.png"

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

export const StarsContext = createContext<[number,React.Dispatch<SetStateAction<number>>]>([0,() => {}])

export interface FeedBack {
    username: string,
    stars?: number,
    readonly: boolean,
    comment:string
}

interface StarInputAttrs {
    inputAttrs: React.InputHTMLAttributes<HTMLInputElement>,
}
function StarInput({inputAttrs}:StarInputAttrs) {

    const [stars] = useContext(StarsContext)

    return <input {...inputAttrs} value={stars}/>
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

                {readonly==true?
                    <div className="avaliation">
                        <p>{comment}</p>
                    </div>
                    :
                    <form>
                        <div className="avaliation">
                            <textarea name="comment"></textarea>
                        </div>

                        <StarInput inputAttrs={{type:"hidden", name:"stars"}}/>

                        <input type="submit" value="Enviar"/>
                    </form>
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

            const response = await fetch("/api/feedbacks/get/",{
                method:"GET",
                credentials:"include"
            })

            const feedbacks = await response.json()

            if (feedbacks instanceof Array) {
                setFeedBacks(feedbacks)
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
                    <FeedBack username={fdb.username} stars={fdb.stars} comment={fdb.comment} readonly={true}/>
                )   
            }
            <FeedBack username={"João"} stars={3} comment="adsad" readonly={true}/>
        </FeedBackSection>
    )
}

export default FeedBacks