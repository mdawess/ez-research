/** @type {import('tailwindcss').Config} */ 
module.exports = {
  content: [
    "./**/pages/**/*.{js,ts,jsx,tsx}",
    "./**/components/**/*.{js,ts,jsx,tsx}",
    "./**/sections/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'tldr-purple': '#8C54D0',
        'tldr-blue': '#444FAD',
        'tldr-green': '#19B092',
        'tldr-red': '#B51515',
        'tldr-orange': '#EF5F33',
        'tldr-grey': '#515C5D',
        'tldr-pink': '#E26A6A',
      }
    },
  },
  plugins: [],
  safelist: [{
    pattern: /(bg|text|border)-tldr-(purple|pink|orange|blue|green|red|grey)/
  }],
}
