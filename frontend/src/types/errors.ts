export type FieldError = {
    field: string;
    message: string;
};

export type ErrorProps = {
    errors: FieldError[];
};