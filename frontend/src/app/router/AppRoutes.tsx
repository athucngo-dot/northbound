import { BrowserRouter } from "react-router-dom";
import AppRouter from "./routes";

export default function AppRoutes() {
    return (
        <BrowserRouter>
            <AppRouter />
        </BrowserRouter>
    );
}