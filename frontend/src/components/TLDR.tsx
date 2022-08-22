import Link from 'next/link';
import React, { useState, useMemo } from 'react'
import { TLDRProps } from '../types/types'

export default function TLDR(props: TLDRProps) {
  const {
    title,
    author,
    date,
    tldr,
    url,
    saved,
    mode,
    publication,
    edition
  } = props;

  const [link, setLink] = useState('');

  const shortenLink = async (url: string) => {
    const response = await fetch('https://api-ssl.bitly.com/v4/shorten', {
      method: 'POST',
      headers: {
          'Authorization': `Bearer ${process.env.BITLY_API_KEY}`,
          'Content-Type': 'application/json'
      },
      // Update to tldr.study
      body: JSON.stringify({ "long_url": url, "domain": "bit.ly" })
    });
    const json = await response.json();
    const link: string = json.link;
    setLink(link);
  }
  
  useMemo(() => {
    shortenLink(url);
  } , []);

  return (
    <div className='border-tldr-grey w-full flex flex-col border-2 mt-10 p-6 font-mono'>
      <h1 className='text-xl font-bold'>{title}</h1>
      <div className='flex'>
        <p className='text-tldr-grey'>{author} • {date}</p>
      </div>
      <p className='text-lg mb-5'>
        {tldr}
      </p>
      <Link href={link} >
        <a target='_blank' className='text-tldr-blue border-b-2'>
          {'link: ' + link}
        </a>
      </Link>
    </div>
  )
}




