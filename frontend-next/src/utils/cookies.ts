export function getCookieByName(name:string) {
    for (const x of document.cookie.trim().split(";")) {
        if (x.startsWith(`${name}=`)) {
            return x.split("=")[1]
        }
    }

    return null
}