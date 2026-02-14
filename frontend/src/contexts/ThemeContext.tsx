import React, { createContext, useContext, useEffect, useState } from 'react';

type FontType = 'inter' | 'opendyslexic' | 'verdana';

interface ThemeContextType {
    font: FontType;
    setFont: (font: FontType) => void;
}

const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

export function ThemeProvider({ children }: { children: React.ReactNode }) {
    const [font, setFont] = useState<FontType>(() => {
        const savedFont = localStorage.getItem('font-preference');
        return (savedFont as FontType) || 'verdana';
    });

    useEffect(() => {
        // Remove all font classes
        document.body.classList.remove('font-inter', 'font-opendyslexic', 'font-verdana');
        // Add current font class
        document.body.classList.add(`font-${font}`);
        // Save to local storage
        localStorage.setItem('font-preference', font);
    }, [font]);

    return (
        <ThemeContext.Provider value={{ font, setFont }}>
            {children}
        </ThemeContext.Provider>
    );
}

export function useTheme() {
    const context = useContext(ThemeContext);
    if (context === undefined) {
        throw new Error('useTheme must be used within a ThemeProvider');
    }
    return context;
}
