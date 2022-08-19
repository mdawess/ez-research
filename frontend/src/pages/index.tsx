import type { NextPage } from 'next'
import ThemeButton from '../components/ThemeButton'
import Header from '../sections/Header'
import Hero from '../sections/Hero'


const Home: NextPage = () => {
  return (
    <div className='p-20'>
      <Header />
      <Hero />
    </div>
  )
}

export default Home
