import React from 'react'
import getRandomColour from '../utils/getRandomColour';

const colours = ['tldr-purple','tldr-blue','tldr-green','tldr-red','tldr-orange','tldr-grey','tldr-pink']

export default function Sidebar() {
    const subjects = ["sustainability", "ai", "finance", "blockchain"];



    return (
        <div className='w-40'>
            <h4 className='font-mono text-xl pr-10'>Subjects</h4>
            <div className='mt-5'></div>
            {subjects.map((subject: any, index: number) => {
                return (
                    <div key={index} className='flex py-2'>
                        <Subject subject={subject} colour={colours[index]} />   
                    </div>
                )
            })}
        </div>
    )
}



const Subject = (props: any) => {
    return (
        <div className={`bg-${props.colour} bg-opacity-30 p-1 rounded-sm pr-4`}>
            <button 
                // Add a function to pull data from the database
                onClick={() => console.log(props.colour)}
            >
                <h4 className='font-mono text-lg'>{props.subject}</h4>
            </button>
        </div>
    )
}
