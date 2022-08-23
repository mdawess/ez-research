import React, { useEffect } from 'react'
import { SearchbarProps } from '../types/types'

export default function Searchbar(props: SearchbarProps) {
    const { query, setQuery } = props


    return (
      <div className='h-14 w-3/4'>
        <input 
          type='text' 
          placeholder='Search' 
          onChange={(e: any) => setQuery(e.target.value)} 
          className='w-full h-full bg-slate-100 outline-none indent-4 font-mono text-2xl dark:caret-black text-black'
        />
      </div>
    )
}
