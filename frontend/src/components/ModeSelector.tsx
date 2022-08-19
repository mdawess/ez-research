import React from 'react'
import { Mode, ModeSelectorProps } from '../types/types'

export default function ModeSelector(props: ModeSelectorProps) {
    const { mode, setMode } = props

    return (
      <div className='ml-2 mt'>
        <div className='w-3/4 border-grey-300 border-b-2 ml-60'>
          <h2 className='text-gray-500 font-mono my-5'>Searches full string once you hit enter!</h2>
          <div className='flex justify-left'>
            {
              modes.map((currMode: Mode) => {
                return (
                  <button 
                    key={currMode} 
                    className={`w-full h-12 bg-white text-black text-center font-mono text-2xl justify-start ${mode === currMode ? 'border-b-4 border-black' : ''}`}
                    onClick={() => setMode(currMode)}
                  >
                    {currMode}
                  </button>
                )
              })
            } 
          </div>
        </div>
      </div>
    )
}

const modes: Mode[] = ['standard', 'research-apa', 'research-mla']
