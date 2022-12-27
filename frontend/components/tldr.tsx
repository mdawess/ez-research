import React from 'react'

type TLDR = {
    title: string;
    tldr: string;
    links: string[];
}

export default function tldr({ title, tldr, links }: TLDR) {

    return (
        <div className="">
            <h1>{title}</h1>
            <p>{tldr}</p>
        </div>
    )
}
