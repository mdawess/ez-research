import React from 'react'
import Divider from '../components/Divider'
import Sidebar from '../components/Sidebar'
import TLDR from '../components/TLDR'
import { MainProps } from '../types/types'

export default function Hero(props: MainProps) {
  const { query, queryData, mode, loading } = props
  return (
    <div className='flex'>
      <div className='flex mt-10 h-full align-top justify-start sticky'>
        <Sidebar />
        {/* Need to align the left hand bar */}
        <div className='mx-0.5' ></div>
        <Divider size={36}/>
      </div>
      {queryData.length === 0 ?
        <div className='flex align-middle justify-center font-mono py-10 px-5'>
          <h1 className='font-2xl'>Search for something!</h1>
        </div> 
       :
        // Appears once someones searched for something 
        <div className='w-3/4'>
          <div className='bg-tldr-purple bg-opacity-40 mt-10 border-2 border-tldr-purple p-3 sticky'>
            {/* Replace # of results with search time */}
            <h1 className=''>{`Showing results for "${query}"`}</h1>
          </div>
          <div>
            {
              queryData.map((resp, index) => {
                return <div key={index}>
                        <TLDR
                          title={resp.title}
                          author={resp.author}
                          date={resp.date}
                          tldr={resp.tldr}
                          url={resp.url}
                          saved={resp.saved}
                          mode={mode}
                          publication=''
                          edition=''
                        />
                      </div>
              })
            }
            
          </div>
        </div>
      }
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
