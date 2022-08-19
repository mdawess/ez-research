import React from 'react'
import { DividerProps } from '../types/types'

export default function Divider(props: DividerProps) {
    const { size } = props
    
    return (
        <div className={`w-1 h-${size} bg-black mx-10`}></div>
  )
}
