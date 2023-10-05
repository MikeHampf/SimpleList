import { useNavigate } from "react-router-dom"
import { useState, useEffect, useContext, createContext } from "react"
import { api } from "../utilities"
import { userContext } from "../App"

export default function LoginPage(){

    const[email, setEmail] = useState("")
    const[password, setPassword] = useState("")
    const navigate = useNavigate()
    const { setUser } = useContext(userContext)

    const loginHandler = async (event) => {
        console.log("LOGGING IN")
        event.preventDefault()
        let response = await api.post("/listers/login/", {
            email: email,
            password: password,
        })
        console.log(response.data)
        let token = response.data.token
        let user = response.data.lister 
        let id = response.data.id
        localStorage.setItem("token", token)
        localStorage.setItem("lister", user)
        localStorage.setItem("id", id)
        api.defaults.headers.common["Authorization"] = `Token ${token}`
        setUser(user)
        setEmail("")
        setPassword("")
        if(token){
            navigate("/listers/items/")
        }
    }

    return (
        <div className="login">
            <input className="email" placeholder="email"
                type="text" 
                value={email}
                onChange={(event) => setEmail(event.target.value)}    
                ></input>
            <input className="password" placeholder="password"
                type="text" 
                value={password}
                onChange={(event) => setPassword(event.target.value)}
                ></input>
                <button className="login_button" onClick={loginHandler}>LOGIN AND START LISTING!</button>
        </div>
    )
}