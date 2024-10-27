import { useState, useEffect, SetStateAction, useContext } from "react"
import styled from "styled-components"
import StarImage from "../../FeedBacks/assets/star.png"
import SelectedStarImage from "../../FeedBacks/assets/selectedstar.png"
import { FeedBack, StarsContext } from ".."

interface StarItf {
    starIndex: number,
    setIndex?: React.Dispatch<SetStateAction<number>>,
    src:string
}

const StarsDIV = styled.div`
    margin-left: auto;

    & img {
        width: 20px;
    }
`

const StyledStarImage = styled.img`

    &:nth-child(n+2) {
        margin-left:2px;
    }
`

function Star({starIndex, setIndex, src}:StarItf) {

    const [stars] = useContext(StarsContext)
    const [clicked, setClicked] = useState(false)

    function onMouse() {
        if (setIndex) {
            if (stars == 0) {
                setIndex(starIndex)
            } else {
                setIndex(0)
            }
        }

    }
    
    if (setIndex) {
        return <StyledStarImage src={src} 
            onMouseEnter={(e) => {!clicked?onMouse():null;setClicked(false)}} 
            onMouseLeave={(e) => {!clicked?onMouse():null}} 
            onClick={(e) => {setClicked(!clicked)}}
        />
    } else {return <StyledStarImage src={src}/>}
    
}

interface StarsType {
    readonly: FeedBack['readonly'],
}

function Stars({readonly}:StarsType){

    const [stars, setStars] = useContext(StarsContext)

    const [Arr,setArr] = useState<Array<JSX.Element>>([])

    interface setStar{
        func:React.Dispatch<SetStateAction<Array<JSX.Element>>>,
        setIndex?: React.Dispatch<SetStateAction<number>>
    }

    function setSelectedStars(func:setStar['func'],setIndex:setStar['setIndex']) {
        for (let i=1; i<=stars; i++) {
            func((previtems) => [
                ...previtems,
                <Star starIndex={i} setIndex={setIndex} src={SelectedStarImage} key={i}/>
            ])
        }
    }

    function setCommonStars(func:setStar['func'],setIndex:setStar['setIndex']) {
        for (let i=stars+1; i<=5; i++) {
            func((previtems) => [
                ...previtems, 
                <Star starIndex={i} setIndex={setIndex} src={StarImage} key={i}/>
            ])
        }
    }

    if (readonly) {
        useEffect(() => {

            setArr([])
            setSelectedStars(setArr, undefined)
            setCommonStars(setArr, undefined)
            
        },[])
    } else {
        useEffect(() => {

            setArr([])
            setSelectedStars(setArr, setStars)
            setCommonStars(setArr, setStars)

        },[stars])
    }

    return (
        <StarsDIV>
            {Arr.map(value => 
                value
            )}
        </StarsDIV>
    )
}

export default Stars
