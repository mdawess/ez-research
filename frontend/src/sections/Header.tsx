import React, { useState, useEffect, useRef, useMemo } from 'react'
import Divider from '../components/Divider'
import Logo from '../components/Logo'
import ModeSelector from '../components/ModeSelector'
import Searchbar from '../components/Searchbar'
import ThemeButton from '../components/ThemeButton'
import { HeaderProps, Mode } from '../types/types'
import { convertToArray } from '../utils/convertToArray'
import { TLDRProps } from '../types/types'

export default function Header(props: HeaderProps) {
    const { 
      query, 
      setQuery, 
      queryData,
      setQueryData, 
      mode, 
      setMode,
      setLoading, 
    } = props

    const [page, setPage] = useState(1)
    const [submit, setSubmit] = useState(false)
    

    const sendSearchQuery = async (query: string, page: number) => {
      // const url = process.env.SERVER_API_URL
      const url = 'https://tldr-production.up.railway.app'
      // const url = 'http://127.0.0.1:8080'

      const response = await fetch(`${url}/search/${query}/${page}`, {
        method: 'POST',
        headers: {
          'Access-Control-Allow-Origin': '*',
        }
      })
      
      const data = await response.json()
      const formattedData = convertToArray(data.results)
      setQueryData(formattedData as TLDRProps[]) 
    }

    const searchQuery = (query: string, page: number) => {
        const keyDownHandler = (event: any) => {
          if (event.keyCode === 13) {
            event.preventDefault();
            setSubmit(!submit)
          }
        };
        document.addEventListener('keydown', keyDownHandler);
        if (submit) {
          setLoading(true)
          sendSearchQuery(query, page)
        }
        return () => {
          document.removeEventListener('keydown', keyDownHandler);
          if (queryData.length !== 0) {
            setLoading(false)
          }
        };
    }
      
    useEffect(() => {
        searchQuery(query, page)
    }, [submit, page])

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

