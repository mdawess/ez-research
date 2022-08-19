import React from 'react'
import { useTheme } from 'next-themes'
import { Sun, Moon } from 'react-bootstrap-icons';

export default function ThemeButton() {
    const { theme, setTheme } = useTheme()
    return (
        <div className='flex mx-5 w-14 h-14 items-center justify-center'>
            {theme === 'dark' ? 
                <button className=""
                    onClick={() => setTheme('light')}
                >
                    <Moon size={36} />
                </button>  
                :
                <button className="bg-white"
                    onClick={() => setTheme('dark')}
                >
                    <Sun size={36} />
                </button>
            }
        </div>
    )
}
