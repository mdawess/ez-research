import React from 'react'
import { LogoProps } from '../types/types'

export default function Logo(props: LogoProps) {

  const { normalText, colouredText, colour } = props
  return (
    <div className='flex items-center'>
      <h1 className='text-red-50 text-xl'>{normalText}</h1>
      <h1>;</h1>
      <h1 className='text-tldr-purple'>{colouredText}</h1>
    </div>
  )
}
