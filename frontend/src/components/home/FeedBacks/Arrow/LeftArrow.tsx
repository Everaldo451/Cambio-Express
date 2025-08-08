'use client'
import Arrow, {FeedbackArrowProps} from "."

export default function LeftArrow(
    {feedbacks, imgProps, setElement}: FeedbackArrowProps
) {
    function onClick(_:React.MouseEvent<HTMLButtonElement, MouseEvent>) {
        setElement(prev => prev-1>=0?prev-1:prev)
    }

    return <Arrow 
        imgProps={imgProps} 
        onClick={onClick} 
    />
}