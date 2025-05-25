import { UserContext } from "../../main";
import { useContext, useState, useEffect, ReactNode, useRef, SetStateAction, HTMLAttributes } from "react";
import { apiAxios } from "@/axios/api";

export interface FeedBack {
    first_name: string,
    date: Date,
    comment:string
}

interface ArrowProps {
    setElement: React.Dispatch<SetStateAction<number>>,
    feedbacks: FeedBack[]
}

/*HTML Css Components*/

function Section(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <section
            {...props}
            className="bg-theme p-[60px_40px]"
        >
            {props.children}
        </section>
    )
}


function H2(props:React.HTMLAttributes<HTMLHeadingElement>) {
    return (
        <h2
            {...props}
            className="text-white m-[0] font-instrument-sans"
        >
            {props.children}
        </h2>
    )
}


function GridDiv(props:React.HTMLAttributes<HTMLDivElement>) {
    return (
        <div
            {...props}
            className="grid grid-cols-[auto_1fr_auto] grid-flow-col mt-[30px]"
        >
            {props.children}
        </div>
    )
}


function FeedbackDisplaySection(
    props:React.DetailedHTMLProps<HTMLAttributes<HTMLDivElement>, HTMLDivElement>
) {
    return (
        <section
            {...props}
            className="grid grid-cols-[calc(24%_-_(14px/4))] grid-flow-col gap-[calc(4%/3)] m-[0_10px] overflow-hidden"
        >
            {props.children}
        </section>
    )
}


function FeedbackDiv(
    props:React.DetailedHTMLProps<HTMLAttributes<HTMLDivElement>, HTMLDivElement>
) {
    return (
        <div
            {...props}
            className="bg-[#BEC1C1] rounded-[20px_0] p-[20px] font-instrument-sans shadow-[7px_10px_10px_var(--box-shadow-theme)]"
        >
            {props.children}
        </div>
    )
}

function FeedbackH5(props:React.HTMLAttributes<HTMLHeadingElement>) {
    return (
        <h5
            {...props}
            className="text-[15px] m-[0]"
        >
            {props.children}
        </h5>
    )
}

function FeedbackH6(props:React.HTMLAttributes<HTMLHeadingElement>) {
    return (
        <h6
            {...props}
            className="text-[10px] text-[#5F5F5F] m-[0] font-normal"
        >
            {props.children}
        </h6>
    )
}

function FeedbackParagraph(props:React.HTMLAttributes<HTMLParagraphElement>) {
    return (
        <p
            {...props}
            className="text-[12px] m-[20px_0_30px_0]"
        >
            {props.children}
        </p>
    )
}


function LeftArrowButton(
    props:React.ImgHTMLAttributes<HTMLImageElement> & ArrowProps
) {
    function onClick(_:React.MouseEvent<HTMLButtonElement, MouseEvent>) {
        props.setElement(prev => prev-1>=0?prev-1:prev)
    }

    return (
        <button onClick={onClick}>
            <img 
                {...props}
                className="w-[20px] m-[auto_0]"
            />
        </button>
    )
}


function RightArrowButton(
    props:React.ImgHTMLAttributes<HTMLImageElement> & ArrowProps
) {
    function onClick(_:React.MouseEvent<HTMLButtonElement, MouseEvent>) {
        props.setElement(prev => prev+1<=props.feedbacks.length?prev+1:prev)
    }

    return (
        <button onClick={onClick}>
            <img 
                {...props}
                className="w-[20px] m-[auto_0] transform-[rotate(180deg)]"
            />
        </button>
    )
}


/*Process Data Components*/

function FeedbackComponent({first_name, date, comment}:FeedBack) {

    return (
        <FeedbackDiv>
            <FeedbackH5 className="name">{first_name}</FeedbackH5>
            <FeedbackH6>{`${date.getDate()}/${date.getMonth()}/${date.getFullYear()}`}</FeedbackH6>
            <div className="avaliation">
                <FeedbackParagraph>Lorem ipsum dolor sit amet consectetur adipisicing elit. 
                    Repellendus, consectetur cum natus sunt iure tempora dolor, aliquid, dolorum 
                    praesentium laudantium sequi soluta quibusdam ipsam. Vitae quidem error ipsum velit eos.
                </FeedbackParagraph>
            </div>            
        </FeedbackDiv>  
    )

}


interface FeedDisplayProps {
    children: ReactNode,
    elementIndex: number,
}

function FeedbackDisplay({children,elementIndex}:FeedDisplayProps) {

    const sectionRef = useRef<HTMLDivElement|null>(null)

    useEffect(() => {

        console.log(elementIndex)

        if (sectionRef.current) {
            const childrens = sectionRef.current.querySelectorAll(":scope > div")

            const element = childrens[elementIndex]
            console.log(element)
            if (element) {
                element.scrollIntoView({
                    inline:"start",
                    behavior:"smooth"
                })
            }
        }
        
    },[elementIndex])

    return (
        <FeedbackDisplaySection ref={sectionRef}>
            {children}
        </FeedbackDisplaySection>
    )
}


function FeedBacks() {

    const [user] = useContext(UserContext)
    const [feedbacks, setFeedBacks] = useState<FeedBack[]>([])
    const [element, setElement] = useState<number>(0)

    async function getFeedBacks() {

        try{
            const response = await apiAxios.get("/feedbacks/search/")
            const responseData = response.data

            if (responseData satisfies FeedBack[]) {
                setFeedBacks(responseData)
            }
            setFeedBacks(prev => [...prev, 
                {first_name:"João", date: new Date(), comment: "asadasd"},
                {first_name:"Maria", date: new Date(), comment: "asadasd"},
                {first_name:"Rafaela", date: new Date(), comment: "asadasd"},
                {first_name:"José", date: new Date(), comment: "asadasd"},
            ])

        } catch(e) {}

    }

    useEffect(() => {
        getFeedBacks()
    },[])

    return (
        <Section>
            <H2>Comentários</H2>
            <GridDiv>
                <LeftArrowButton src={"/images/triangle.png"} setElement={setElement} feedbacks={feedbacks}/>
                <FeedbackDisplay elementIndex={element}>
                    {
                        user && feedbacks?.filter((feedback) => feedback.first_name == user.first_name).length==0?
                            <FeedbackComponent first_name={user.first_name} comment="adsad" date={new Date()}/>
                        :null
                    }
                    {
                        feedbacks.map((fdb) => 
                            <FeedbackComponent first_name={fdb.first_name} date={fdb.date} comment={fdb.comment}/>
                        )   
                    }
                </FeedbackDisplay>
                <RightArrowButton src={"/images/triangle.png"} setElement={setElement} feedbacks={feedbacks}/>
            </GridDiv>
        </Section>
    )
}

export default FeedBacks