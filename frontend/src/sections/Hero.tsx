import React from 'react'
import Divider from '../components/Divider'
import Sidebar from '../components/Sidebar'
import TLDR from '../components/TLDR'
import { MainProps } from '../types/types'

export default function Hero(props: MainProps) {
  const { query } = props
  return (
    <div className='flex'>
      <div className='flex mt-10 h-full align-top justify-start sticky'>
        <Sidebar />
        {/* Need to align the left hand bar */}
        <div className='mx-0.5' ></div>
        <Divider size={36}/>
      </div>
      <div className='w-3/4'>
        <div className='bg-tldr-purple bg-opacity-40 mt-10 border-2 border-tldr-purple p-3 sticky'>
          <h1 className=''>{`Showing top 10 results for "${query}"`}</h1>
        </div>
        <div>
          <TLDR 
            title='A really short story'
            author='Michael Dawes'
            date='2022-01-01'
            tldr={dummyText}
            url='https://jmulholland.com/small-group/?curius=1294'
            saved={false}
            mode={'standard'}
            publication='MIT Press'
            edition='2nd Edition'
          />
          <TLDR 
            title='A really short story'
            author='Michael Dawes'
            date='2022-01-01'
            tldr={dummyText}
            url='https://jmulholland.com/small-group/?curius=1294'
            saved={false}
            mode={'standard'}
            publication='MIT Press'
            edition='2nd Edition'
          />
          <TLDR 
            title='A really short story'
            author='Michael Dawes'
            date='2022-01-01'
            tldr={dummyText}
            url='https://jmulholland.com/small-group/?curius=1294'
            saved={false}
            mode={'standard'}
            publication='MIT Press'
            edition='2nd Edition'
          />
          <TLDR 
            title='A really short story'
            author='Michael Dawes'
            date='2022-01-01'
            tldr={dummyText}
            url='https://jmulholland.com/small-group/?curius=1294'
            saved={false}
            mode={'standard'}
            publication='MIT Press'
            edition='2nd Edition'
          />
          <TLDR 
            title='A really short story'
            author='Michael Dawes'
            date='2022-01-01'
            tldr={dummyText}
            url='https://jmulholland.com/small-group/?curius=1294'
            saved={false}
            mode={'standard'}
            publication='MIT Press'
            edition='2nd Edition'
          />
          <TLDR 
            title='A really short story'
            author='Michael Dawes'
            date='2022-01-01'
            tldr={dummyText}
            url='https://jmulholland.com/small-group/?curius=1294'
            saved={false}
            mode={'standard'}
            publication='MIT Press'
            edition='2nd Edition'
          />
        </div>
      </div>
    </div>
  )
}

const dummyText = `
Lorem ipsum dolor sit amet,
consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. 
Aenean massa. 
Cum sociis natoque penatibus et magnis dis parturient montes, 
nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, 
pretium quis, sem. Nulla consequat massa quis enim. Donec.
`
