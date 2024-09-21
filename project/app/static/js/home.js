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

const feedbacks = main.querySelector("section.feedbacks")
const feedbackList = feedbacks.querySelectorAll("div.feedback")

if (feedbackList) {

    for (const feedback of feedbackList) {

        const divstars = feedback.querySelector("div.stars")
        const stars = divstars.querySelectorAll("img")
        const imginput = divstars.querySelector("input")

        if (imginput) {new StarCounter(stars,imginput.value,false)}
    }
}