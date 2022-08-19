
const getRandomColour = () => {
    const colours: any = {
        'tldr-purple': '#8C54D0',
        'tldr-blue': '#444FAD',
        'tldr-green': '#19B092',
        'tldr-red': '#B51515',
        'tldr-orange': '#EF5F33',
        'tldr-grey': '#515C5D',
        'tldr-pink': '#E26A6A',
    };
    const randomColour: any = Object.keys(colours)[Math.floor(Math.random() * Object.keys(colours).length)];
    return randomColour;
}

export default getRandomColour;