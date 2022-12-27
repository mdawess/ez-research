import React from 'react'

type Link = {
    firstNode: string;
    secondNode: string;
    weight: number;
}

export default function link({ firstNode, secondNode }: Link) {
  return (
    <div>link</div>
  )
}
