export type Theme = 'light' | 'dark';

export type SearchbarProps = {
    setQuery: (query: string) => void;
}

export type MainProps = {
    query: string;
    queryData: TLDRProps[];
    mode: Mode;
}

export type HeaderProps = {
    mode: Mode;
    setMode: (mode: Mode) => void;
    setQueryData: (data: TLDRProps[]) => void;
}

export type LogoProps = {
    normalText: string;
    colouredText: string;
    colour: string;
}

export type Mode = "standard" | "research-apa" | "research-mla";

export type ModeSelectorProps = {
    mode: Mode;
    setMode: (mode: Mode) => void;
}

export type TLDRProps = {
    title: string;
    author: string;
    date: string;
    tldr: string;
    url: string;
    saved: boolean;
    mode: Mode;
    publication?: string;
    edition?: string;
}

export type Subject = {
    subjectId: string;
    subjectName: string;
    tldr: TLDRProps;
}

export type Profile = {
    id: number;
    name: string;
    email: string;
    signupDate: string;
    colour: string;
    profilePicture?: string;
}

export type DividerProps = {
    size: number;
}