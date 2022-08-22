
export const apa_citation = (author: string, title: string, year: string, publisher: string, edition: string = '1st', url: string = '') => {
    const last_name = author.split(' ')[-1]
    const first_initial = author.split(' ')[0][0]
    let full = `${capitalize(last_name)}, ${first_initial}. (${year}). ${title} \n (${edition} ed.). ${publisher}.`
    const text = `(${last_name}, ${year})`

    if (url != '') {
        full += '\n' + url
    }
    return [full, text]
}



export const mla_citation = (author: string, title: string, year: string, publisher: string, edition: string = '1st', url: string = '') => {
    const last_name = author.split(' ')[-1]
    const first_name = author.split(' ')[0]
    let full = `${capitalize(last_name)}, ${capitalize(first_name)}. ${title}. ${edition}, ${publisher}, \n${year}.`
    const text = `(${last_name}, ${year})`

    if (url != '') {
        full += ' ' + url
    }
    return [full, text]
}

const capitalize = (s: string) => {
    if (typeof s !== 'string') return ''
    return s.charAt(0).toUpperCase() + s.slice(1)
}