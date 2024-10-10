import styled from "styled-components";
import { UserContext } from "../../main";
import { ReactNode, useContext, useState, useEffect, SetStateAction } from "react";
import StarImage from "../FeedBacks/assets/star.png"
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
`

const PersonDIV = styled.div`
    display: flex;
    align-items: center;

    & > img {
        width: 30px;
        height: 30px;
    }
`

const StarsDIV = styled.div`
    margin-left: auto;

    & img {
        width: 20px;
    }
`

export interface FeedBack {
    
    username: string,
    stars: number,
    readonly: boolean,
    comment:string
}

interface StarItf {
    starIndex: number,
    indexState:number,
    setIndex: React.Dispatch<SetStateAction<number>>
}

function Star({starIndex, indexState, setIndex}:StarItf) {

    function onClick() {
        if (indexState == 0) {
            setIndex(starIndex)
        } else {
            setIndex(0)
        }
    }

    return <img src={StarImage} onMouseEnter={(e) => {setIndex(starIndex)}}/>
    
}

function Stars({readonly}:Pick<FeedBack,"readonly">){

    const [index,setIndex] = useState(0)

    const Arr:Array<JSX.Element> = []

    for (let i = 0; i<=4; i++) {

        Arr.push(<Star starIndex={i} indexState={index} setIndex={setIndex}/>)
    }

    return (
        <StarsDIV>
            {Arr.map(value => 
                value
            )}
        </StarsDIV>
    )
}

function FeedBack({username,stars,readonly,comment}:FeedBack) {

    return (
        <FeedBackDIV>

            <PersonDIV>
                <img src={Avatar}/>
                <p className="name">{username}</p>
                <Stars readonly={readonly}/>
            </PersonDIV>
            <div className="avaliation">
                {comment}
            </div>

        </FeedBackDIV>
    )
}

function FeedBacks() {

    const [user,setUser] = useContext(UserContext)

    return (
        <FeedBackSection>
            <h2>FeedBacks</h2>
            {user?
            <FeedBack username={user.username} stars={1} comment="adsad" readonly={true}/>
            :null
            }
            <FeedBack username={"João"} stars={1} comment="adsad" readonly={true}/>
        </FeedBackSection>
    )
}

export default FeedBacks