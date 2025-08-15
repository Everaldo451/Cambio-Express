'use client'
import Arrow, {FeedbackArrowProps} from "."

export default function LeftArrow(
    {imgProps, setElement}: Omit<FeedbackArrowProps, 'feedbacks'>
) {
    function onClick(_:React.MouseEvent<HTMLButtonElement, MouseEvent>) {
        setElement(prev => prev-1>=0?prev-1:prev)
    }

    return <Arrow 
        imgProps={imgProps} 
        onClick={onClick} 
    />
}