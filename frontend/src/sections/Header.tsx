import React, { useState, useEffect } from 'react'
import Divider from '../components/Divider'
import Logo from '../components/Logo'
import Searchbar from '../components/Searchbar'
import ThemeButton from '../components/ThemeButton'

export default function Header() {
    const [query, setQuery] = useState('')

    useEffect(() => {
        // Update to a fucntion to send query to server
        console.log(query)
    }, [query])

    return (
        <div className='flex items-center'>
            <Logo normalText='tl' colouredText='dr' colour='#8C54D0' />
            <Divider size={14} />
            <Searchbar setQuery={setQuery} />
            <ThemeButton />
        </div>
  )
}
