import styled from "styled-components";
import { UserContext } from "../../main";
import { useContext, useState, useEffect, ReactNode, useRef } from "react";
import Triangle from "./assets/Triangle.png"
import {customAxios} from "../../load";

const Section = styled.section`
    background-color: #3F4156;
    padding: 60px 40px;

    & > h2 {
        color:white;
        margin:0;
        font-family: InstrumentSans;
    }
`

const Div = styled.div`
    margin-top: 30px;
    display: grid;
    grid-template-columns: auto 1fr auto;
    grid-auto-flow: column;
`

const FeedSection = styled.section`
    margin: 0 10px;
    display: grid;
    grid-auto-columns: calc(24% - (14px/4));
    gap: calc(4%/3);
    grid-auto-flow: column;
    overflow: hidden;
`

const FeedBackDIV = styled.div`
    border-radius: 20px 0;
    background-color: #BEC1C1;
    padding:20px;
    font-family: InstrumentSans;
    box-shadow: 7px 10px 10px #2D2F3F;

    & h5 {
        font-size: 15px;
        margin: 0;
    }

    & h6 {
        font-size: 10px;
        color: #5F5F5F;
        margin: 0;
        font-weight: normal;
    }

    & p {
        font-size: 12px;
        margin: 20px 0 30px 0;
    }
`

const Seta = styled.img`
    width: 20px;
    margin: auto 0;
`

const Seta2 = styled(Seta)`
    transform: rotate(180deg);
`

export interface FeedBack {
    first_name: string,
    date: Date,
    comment:string
}

interface Feed {
    children: ReactNode,
    elNum: number,
}

function FeedBack({first_name,date,comment}:FeedBack) {

    return (
        
        <FeedBackDIV>

            <h5 className="name">{first_name}</h5>
            <h6>{`${date.getDate()}/${date.getMonth()}/${date.getFullYear()}`}</h6>
            
            <div className="avaliation">
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Repellendus, consectetur cum natus sunt iure tempora dolor, aliquid, dolorum praesentium laudantium sequi soluta quibusdam ipsam. Vitae quidem error ipsum velit eos.</p>
            </div>            

        </FeedBackDIV>
        
    )

}

function FeedComponent({children,elNum}:Feed) {

    const sectionRef = useRef<HTMLElement|null>(null)

    useEffect(() => {

        console.log(elNum)

        if (sectionRef.current) {
            const childrens = sectionRef.current.querySelectorAll(":scope > div")

            const element = childrens[elNum]
            console.log(element)
            if (element) {
                element.scrollIntoView({
                    inline:"start",
                    behavior:"smooth"
                })
            }
        }
        
    },[elNum])

    return (
        <FeedSection ref={sectionRef}>
            {children}
        </FeedSection>
    )
}


function FeedBacks() {

    const [user] = useContext(UserContext)
    const [feedbacks, setFeedBacks] = useState<Array<FeedBack>>([])
    const [element, setElement] = useState<number>(0)

    async function GetFeedBacks() {

        try{

            const response = await customAxios.get("/api/feedbacks/get/")

            const feedbacks = response.data

            if (feedbacks instanceof Array) {
                setFeedBacks(feedbacks)
            }

        } catch(e) {}

    }

    useEffect(() => {
        GetFeedBacks()
        console.log(feedbacks)

        setFeedBacks(prev => [...prev, 
            {first_name:"João", date: new Date(), comment: "asadasd"},
            {first_name:"Maria", date: new Date(), comment: "asadasd"},
            {first_name:"Rafaela", date: new Date(), comment: "asadasd"},
            {first_name:"José", date: new Date(), comment: "asadasd"},
        ])
    },[])

    return (
        <Section>
            <h2>Comentários</h2>
            <Div>
                <Seta 
                    src={Triangle} 
                    onClick={(e) => {setElement(prev => prev-1>=0?prev-1:prev)}}
                />
                <FeedComponent elNum={element}>
                    {
                        user && feedbacks?.filter((feedback) => feedback.first_name == user.first_name).length==0?
                            <FeedBack first_name={user.first_name} comment="adsad" date={new Date()}/>
                        :null
                    }
                    {
                        feedbacks.map((fdb) => 
                            <FeedBack first_name={fdb.first_name} date={fdb.date} comment={fdb.comment}/>
                        )   
                    }
                </FeedComponent>
                <Seta2 
                    src={Triangle} 
                    onClick={(e) => {setElement(prev => prev+1<=feedbacks.length?prev+1:prev)}}
                />
            </Div>
        </Section>
    )
}

export default FeedBacks