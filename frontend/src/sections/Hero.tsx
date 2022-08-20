import React from 'react'
import Divider from '../components/Divider'
import Sidebar from '../components/Sidebar'
import { MainProps } from '../types/types'

export default function Hero(props: MainProps) {
  const { query } = props
  return (
    <div className='flex'>
      <div className='flex mt-10 h-full align-top justify-start sticky'>
        <Sidebar />
        <div className='mx-2.5' ></div>
        <Divider size={36}/>
      </div>
      <div>
        <div className='bg-tldr-purple bg-opacity-40 mt-10 border-2 border-tldr-purple p-3 w-full sticky'>
          <h1 className=''>{`Showing top 10 results for "${query}"`}</h1>
        </div>
        <div>
          
        </div>
      </div>
    </div>
  )
}
