
const getRandomColour = () => {
    const colours: any = {
        purple: '#8C54D0',
        blue: '#444FAD',
        green: '#19B092',
        red: '#B51515',
        orange: '#EF5F33',
        grey: '#515C5D',
        pink: '#E26A6A',
    };
    const randomColour: any = Object.keys(colours)[Math.floor(Math.random() * Object.keys(colours).length)];
    return colours[randomColour];
}

export default getRandomColour;