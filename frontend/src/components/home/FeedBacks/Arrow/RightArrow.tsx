'use client'
import Arrow, {FeedbackArrowProps} from "."

export default function RightArrow(
    {feedbacks, imgProps, setElement}: FeedbackArrowProps
) {
    function onClick(_:React.MouseEvent<HTMLButtonElement, MouseEvent>) {
        setElement(prev => prev+1<=feedbacks.length?prev+1:prev)
    }
    
    return <Arrow 
        imgProps={{...imgProps, className: 'transform-[rotate(180deg)]'}}
        onClick={onClick} 
    />
}