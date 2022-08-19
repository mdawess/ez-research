import React from 'react'
import { useTheme } from 'next-themes'

export default function ThemeButton() {
    const { theme, setTheme } = useTheme()
    return (
        <div>
            {theme === 'dark' ? 
                <button className="text-white bg-gray-800"
                onClick={() => setTheme('light')}
                >
                    
                </button>  
                :
                <button className="bg-white"
                onClick={() => setTheme('dark')}
                >
                    
                </button>
            }
        </div>
    )
}
