import { useTheme } from 'next-themes'
import { Theme } from '../types/types'

const changeTheme = (newTheme: Theme) => {
    const { theme, setTheme } = useTheme()
    setTheme(theme as Theme)
}