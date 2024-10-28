import React, { useState, useEffect, SetStateAction, useContext } from "react"
import styled from "styled-components"
import StarImage from "../../FeedBacks/assets/star.png"
import SelectedStarImage from "../../FeedBacks/assets/selectedstar.png"
import { FeedBack, StarsContext } from ".."

interface StarItf {
    starIndex: number,
    setIndex?: React.Dispatch<SetStateAction<number>>,
    src:string
}

interface StarsType {
    readonly: FeedBack['readonly'],
}

interface setStar{
    setArr:React.Dispatch<SetStateAction<Array<JSX.Element>>>,
    setIndex?: React.Dispatch<SetStateAction<number>>,
    init: number,
    end: number,
    src: string
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

    function MouseEnter(e: React.MouseEvent<HTMLImageElement, MouseEvent>) {
        if (!clicked && setIndex && starIndex != stars) {setIndex(starIndex)}
        if (clicked) {setClicked(false)}
    }

    function MouseLeave(e:React.MouseEvent<HTMLImageElement, MouseEvent>) {
        if (!clicked && setIndex) {setIndex(0)}
    }
    
    if (setIndex) {
        return <StyledStarImage src={src}
            onMouseEnter={MouseEnter}
            onMouseLeave={MouseLeave}
            onClick={(e) => {setClicked(!clicked)}}
        />
    } else {return <StyledStarImage src={src}/>}
    
}


function Stars({readonly}:StarsType){

    const [stars, setStars] = useContext(StarsContext)

    console.log(stars)

    //const [Arr,setArr] = useState<Array<JSX.Element>>([])

    /*
    function setStarsSrc({setArr,setIndex,init,end,src}:setStar) {

        for (let i=init; i<=end; i++) {
            setArr((previtems) => [
                ...previtems,
                <Star starIndex={i} setIndex={setIndex} src={src} key={i}/>
            ])
        }
    }

    function setSelectedStars(func:setStar['setArr'],setIndex:setStar['setIndex']) {
        setStarsSrc({setArr: func, setIndex: setIndex, init: 1, end: stars, src: SelectedStarImage})
    }

    function setCommonStars(func:setStar['setArr'],setIndex:setStar['setIndex']) {
        setStarsSrc({setArr: func, setIndex: setIndex, init: stars + 1, end: 5, src: StarImage})
    }
    */

    const Array:Array<JSX.Element> = []

    for (let i=1; i<= 5; i++) {
        Array.push(<Star starIndex={i} setIndex={readonly?undefined:setStars} src={StarImage} key={i}/>)
    }
    
    /*
    useEffect(() => {

        setArr([])
        setSelectedStars(setArr, readonly?undefined:setStars)
        setCommonStars(setArr, readonly?undefined:setStars)
            
    },[stars])
    */
   

    return (
        <StarsDIV>
            {Array.map((value, index) => {

                    if (index < stars) {
                        return <Star {...value.props} src={SelectedStarImage}/>
                    }
                    return value
                }
            )}
        </StarsDIV>
    )
}

export default Stars
