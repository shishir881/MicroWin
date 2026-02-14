import { Type } from "lucide-react"
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select"
import { useTheme } from "@/contexts/ThemeContext"

export function FontSwitcher() {
    const { font, setFont } = useTheme()

    return (
        <Select value={font} onValueChange={(value: any) => setFont(value)}>
            <SelectTrigger className="w-[140px] h-9 gap-2">
                <Type className="h-4 w-4" />
                <SelectValue placeholder="Select Font" />
            </SelectTrigger>
            <SelectContent>
                <SelectItem value="inter" className="font-inter">
                    Default (Inter)
                </SelectItem>
                <SelectItem value="opendyslexic" className="font-opendyslexic">
                    OpenDyslexic
                </SelectItem>
                <SelectItem value="verdana" className="font-verdana">
                    Verdana
                </SelectItem>
            </SelectContent>
        </Select>
    )
}
