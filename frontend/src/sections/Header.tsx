import React, { useState, useEffect } from 'react'
import Divider from '../components/Divider'
import Logo from '../components/Logo'
import ModeSelector from '../components/ModeSelector'
import Searchbar from '../components/Searchbar'
import ThemeButton from '../components/ThemeButton'
import { HeaderProps, Mode } from '../types/types'

export default function Header(props: HeaderProps) {
    const { setQueryData, mode, setMode } = props
    const [query, setQuery] = useState('')
    // const [mode, setMode] = useState('standard')
    const searchQuery = () => {
        const keyDownHandler = (event: any) => {
          if (event.code === 'Enter') {
            event.preventDefault();
            console.log('You pressed enter!');
          }
        };
        document.addEventListener('keydown', keyDownHandler);
      
        return () => {
          document.removeEventListener('keydown', keyDownHandler);
        };
    }
      

    useEffect(() => {
        searchQuery()
    }, [])

    return (
        <div className='sticky'>
            <div className='flex items-center'>
                <Logo normalText='tl' colouredText='dr' colour='#8C54D0' />
                <Divider size={14} />
                <Searchbar  query={query} setQuery={setQuery} />
                {/* <ThemeButton /> */}
            </div>
            <div className='ml-5'>
                <ModeSelector mode={mode as Mode} setMode={setMode} />
            </div>
        </div>
  )
}

