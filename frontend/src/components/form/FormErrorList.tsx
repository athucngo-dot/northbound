import type { ErrorProps } from "../../types/errors";


export default function FormErrorList({ errors }: ErrorProps) {
    if (!errors.length) return null;

    return (
        <div className="text-red-500 text-sm space-y-1">
            {errors.map(({ field, message }) => (
                <div key={field}>
                    {message}
                </div>
            ))}
        </div>
    );
}