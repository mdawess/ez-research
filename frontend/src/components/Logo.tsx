import React from 'react'
import { LogoProps } from '../types/types'

export default function Logo(props: LogoProps) {

  const { normalText, colouredText, colour } = props
  return (
    <div className='flex items-center'>
      <h1 className='text-6xl font-mono font-semibold'>{normalText}</h1>
      <h1 className='text-6xl font-mono font-semibold'>;</h1>
      <h1 className='text-tldr-purple text-6xl font-mono font-semibold'>{colouredText}</h1>
    </div>
  )
}
