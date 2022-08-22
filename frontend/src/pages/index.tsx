import { useState } from 'react'
import type { NextPage } from 'next'
import ThemeButton from '../components/ThemeButton'
import Header from '../sections/Header'
import Hero from '../sections/Hero'
import { Mode, TLDRProps } from '../types/types'


const Home: NextPage = () => {
  // May need to convert the data to a list of objects on request
  const [queryData, setQueryData] = useState([] as TLDRProps[])
  const [mode, setMode] = useState("standard")

  return (
    <div className='p-20'>
      <Header setQueryData={setQueryData} mode={mode as Mode} setMode={setMode} />
      <Hero query='Python' queryData={queryData} mode={mode as Mode} />
    </div>
  )
}

export default Home
