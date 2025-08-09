export default function formDataToJson(formData:FormData) {
    const jsonObject:{[key:string]: any} = {}
    formData.forEach((value, key) => {
        jsonObject[key] = value
    })
    return jsonObject
}