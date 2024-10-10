const main = document.querySelector("main")
const content = main.querySelector(".introduction")
const container = content?.querySelector(".imgcontainer")
const img = container?.querySelector("img")

const buttons = container?.querySelectorAll("button")

async function fetchData(coin) {

    try {
        const response = await fetch(`/graphs/get/${coin}`)
        const data = await response.json()

        if (img) {
            img.src = data.image
        }

        return
    }
    catch (error) {}
}

fetchData("USD")

if (buttons) {
    for (const button of buttons) {

        const input = button.querySelector("input")

        button.addEventListener("click",(e) => {
            e.preventDefault()
            fetchData(input.value)
        })
    }
}

class Star {
    constructor(imgsrc) {

        const img = document.createElement("img")

        img.src = imgsrc

        return img
    }
}

class StarCounter {

    #starsarray
    #src

    constructor(starsarray, img, readOnly, total) {

        if (starsarray instanceof NodeList && starsarray[0] instanceof HTMLImageElement) {

            this.#src = img
            this.#starsarray = starsarray

            if (readOnly == true && total) {
                this.starImageModify(total)
            } else if (readOnly == false) {

                starsarray.forEach((star,key) => {

                    const enter = star.addEventListener("mouseenter",(e) => {
                        this.starImageModify(key)
                    })
                    const leave = star.addEventListener("mouseleave",(e) => {
                        this.starImageModify(key)
                    })

                })
            }

            this.counter = 0
        }

    }

    starImageModify(key) {

        let inputsrc = null

        for (var i = 0; i <= key; i++) {
    
            const star = this.#starsarray[i]
            const src = star.src
            star.src = this.#src

            inputsrc = src
        }

        this.counter = key
        this.#src = inputsrc?inputsrc:this.#src
    }

}

class Feedback {

    constructor(parentElement, readOnly, enterImg, leaveImg, noneUserImg) {

        if (parentElement instanceof HTMLElement && parentElement.classList.contains("feedbacks")) {

            //USER AVALIATION
            const feedback = document.createElement("div")
            feedback.classList.add(["feedback"])
            parentElement.appendChild(feedback)

            const person = document.createElement("div")
            person.classList.add(["person"])
            feedback.appendChild(person)

            const userimg = document.createElement("img")
            userimg.src = noneUserImg
            person.appendChild(userimg)

            const username = document.createElement("p")
            username.innerHTML = "None"
            person.appendChild(username)

            const divstars = document.createElement("div")
            divstars.classList.add(["stars"])
            person.appendChild(divstars)

            for (let i = 1; i<=5; i++) {
                const star = document.createElement("img")

                star.src = enterImg
                divstars.appendChild(star)
            }
            const stars = divstars.querySelectorAll("img")

            new StarCounter(stars, leaveImg, readOnly, readOnly?0:null)

            //USER COMMENT
            const avaliation = document.createElement("div")
            avaliation.classList.add(["avaliation"])
            feedback.appendChild(avaliation)
        }
    }
}


const feedbacks = main.querySelector("section.feedbacks")
if (feedbacks) {

    const enterimg = feedbacks.querySelector("input.enterimg")
    const leaveimg = feedbacks.querySelector("input.leaveimg")
    const noneUserImg = feedbacks.querySelector("input.noneuser")

    console.log(enterimg,leaveimg)

    if (enterimg instanceof HTMLInputElement && leaveimg instanceof HTMLInputElement && noneUserImg instanceof HTMLInputElement) {
        console.log(feedbacks)
        new Feedback(feedbacks, false, enterimg.value, leaveimg.value, noneUserImg.value)
    }
}
/*
const feedbackList = feedbacks.querySelectorAll("div.feedback")

if (feedbackList) {

    for (const feedback of feedbackList) {

        const divstars = feedback.querySelector("div.stars")
        const stars = divstars.querySelectorAll("img")
        const imginput = divstars.querySelector("input")

        if (imginput) {new StarCounter(stars,imginput.value,false)}
    }
}*/