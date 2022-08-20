import { useState } from 'react'
import type { NextPage } from 'next'
import ThemeButton from '../components/ThemeButton'
import Header from '../sections/Header'
import Hero from '../sections/Hero'
import { TLDR } from '../types/types'


const Home: NextPage = () => {
  const [queryData, setQueryData] = useState({} as TLDR)
  return (
    <div className='p-20'>
      <Header setQueryData={setQueryData} />
      <Hero query='Python'/>
    </div>
  )
}

export default Home
