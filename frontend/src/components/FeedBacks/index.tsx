import styled from "styled-components";
import { UserContext } from "../../main";
import { ReactNode, useContext, useState, useEffect, SetStateAction } from "react";
import StarImage from "../FeedBacks/assets/star.png"
import SelectedStarImage from "../FeedBacks/assets/selectedstar.png"
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

const StarsDIV = styled.div`
    margin-left: auto;

    & img {
        width: 20px;
    }
`

export interface FeedBack {
    
    username: string,
    stars?: number,
    readonly: boolean,
    comment:string
}

interface StarItf {
    starIndex: number,
    indexState:number,
    setIndex?: React.Dispatch<SetStateAction<number>>,
    src:string
}

function Star({starIndex, indexState, setIndex,src}:StarItf) {

    function onMouse() {
        if (setIndex) {
            if (indexState == 0) {
                setIndex(starIndex)
            } else {
                setIndex(0)
            }
        }

    }
    
    if (setIndex) {
        return <img src={src} onMouseEnter={(e) => {onMouse()}} onMouseLeave={(e) => {onMouse()}}/>
    } else {return <img src={src}/>}
    
}

interface StarsType {
    readonly: FeedBack['readonly'],
    starNumber?: FeedBack['stars']
}

function Stars({readonly, starNumber}:StarsType){

    const [index,setIndex] = useState(starNumber?starNumber:0)

    const [Arr,setArr] = useState<Array<JSX.Element>>([])

    interface setStar{
        func:React.Dispatch<SetStateAction<Array<JSX.Element>>>,
        setIndex?: React.Dispatch<SetStateAction<number>>
    }

    function setSelectedStars(func:setStar['func'],setIndex:setStar['setIndex']) {
        for (let i=1; i<=index; i++) {
            func((previtems) => [
                ...previtems,
                <Star starIndex={i} indexState={index} setIndex={setIndex} src={SelectedStarImage} key={i}/>
            ])
        }
    }

    function setCommonStars(func:setStar['func'],setIndex:setStar['setIndex']) {
        for (let i=index+1; i<=5; i++) {
            func((previtems) => [
                ...previtems, 
                <Star starIndex={i} indexState={index} setIndex={setIndex} src={StarImage} key={i}/>
            ])
        }
    }


    if (readonly) {
        useEffect(() => {
            setSelectedStars(setArr, undefined)
            setCommonStars(setArr, undefined)
        },[])
    } else {
        useEffect(() => {

            setArr([])
            setSelectedStars(setArr, setIndex)
            setCommonStars(setArr, setIndex)

        },[index])
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
                <Stars readonly={readonly} starNumber={stars?stars:undefined}/>
            </PersonDIV>
            <div className="avaliation">
                {comment}
            </div>

        </FeedBackDIV>
    )
}

function FeedBacks() {

    const [user] = useContext(UserContext)

    return (
        <FeedBackSection>
            <h2>FeedBacks</h2>
            {user?
            <FeedBack username={user.username} comment="adsad" readonly={false}/>
            :null
            }
            <FeedBack username={"João"} stars={3} comment="adsad" readonly={true}/>
        </FeedBackSection>
    )
}

export default FeedBacks