import { createBrowserRouter } from "react-router-dom"
import App from "./App"
import LoginPage from "./pages/LoginPage"
import HomePage from "./pages/HomePage"
import SignUpPage from "./pages/SignUpPage"
import ListPage from "./pages/ListPage"

const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        children: [ // refers to outlet
            {
                index: true,
                element: <HomePage />
            },
            {
                path: "login/",
                element: <LoginPage />,
            },
            {
                path: "signup/",
                element: <SignUpPage />,
            },
            {
                path: "listers/items/",
                element: <ListPage />
            },
        ]
    }
])
export default router