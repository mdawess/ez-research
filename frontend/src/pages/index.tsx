import { useState } from 'react'
import type { NextPage } from 'next'
import ThemeButton from '../components/ThemeButton'
import Header from '../sections/Header'
import Hero from '../sections/Hero'
import { Mode, TLDRProps } from '../types/types'
// import sampleData from '../sampledata/sample'


const Home: NextPage = () => {
  // May need to convert the data to a list of objects on request
  const [query, setQuery] = useState('')
  const [queryData, setQueryData] = useState([] as TLDRProps[])
  const [mode, setMode] = useState("standard")
  const [loading, setLoading] = useState(false)

  // For testing only
  // const [queryData, setQueryData] = useState(sampleData as TLDRProps[])

  return (
    <div className='p-20'>
      <Header 
        query={query}
        setQuery={setQuery}
        queryData={queryData}
        setQueryData={setQueryData} 
        mode={mode as Mode} 
        setMode={setMode} 
        setLoading={setLoading}
      />
      <Hero 
        loading={loading}
        query={query} 
        queryData={queryData} 
        mode={mode as Mode} 
      />
    </div>
  )
}

export default Home
