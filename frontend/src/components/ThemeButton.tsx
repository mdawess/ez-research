import React from 'react'
import { useTheme } from 'next-themes'
import { Sun, Moon } from 'react-bootstrap-icons';

export default function ThemeButton() {
    const { theme, setTheme } = useTheme()
    return (
        <div className='rounded-xl'>
            {theme === 'dark' ? 
                <button className="text-white bg-gray-800"
                    onClick={() => setTheme('light')}
                >
                    <Moon size={28} />
                </button>  
                :
                <button className="bg-white"
                    onClick={() => setTheme('dark')}
                >
                    <Sun size={28} />
                </button>
            }
        </div>
    )
}
