import Link from 'next/link';
import React, { useState, useMemo } from 'react'
import { TLDRProps } from '../types/types'
import { apaCitation, mlaCitation } from '../utils/citationGenerator';

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
        <p className='text-tldr-grey mt-1'>{author} • {date}</p>
      </div>
      <p className='text-lg mb-4 mt-2'>
        {tldr}
      </p>
      <Link href={link} >
        <a target='_blank' className='text-tldr-blue border-b-2'>
          {'link: ' + link}
        </a>
      </Link>
      <div className='flex justify-between mt-4'>
      {
        mode === 'research-apa' && publication ?
          apaCitation(author, title, date, publication, edition, url) 
          :
          mode === 'research-mla' && publication ?
            mlaCitation(author, title, date, publication, edition, url)
          : 
          null
      }
      </div>
    </div>
  )
}




