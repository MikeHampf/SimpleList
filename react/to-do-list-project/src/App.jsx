import { useState, useContext, createContext, useEffect } from 'react'
import './App.css'
import { useNavigate, Outlet } from 'react-router-dom'
import { api } from "./utilities"

export const userContext = createContext()

export default function App() {
  const [user,setUser] = useState()
  const navigate = useNavigate()

  const logOut = async () => {
    // console.log(token, user)
    let response = await api.post("listers/logout/")
    if (response.status === 204){
      localStorage.removeItem("token")
      localStorage.removeItem("lister")
      delete api.defaults.headers.common["Authorization"]
      setUser(null)
      navigate("/")
    }
  }

  useEffect(() => {
    const whoAmI = async () => {
      let token = localStorage.getItem("token")
      if(token){
        api.defaults.headers.common["Authorization"] = `Token ${token}`
        let response = await api.get("listers/info/")
        if(response.data.email){
          setUser(response.data)
          navigate("/"), {user: response.data}
        }
      }
      else{
        navigate("/")
      }
    }
    whoAmI()
  },[])

  return (
    <div id="app">
      <button onClick={()=>logOut()}>LOGOUT!</button>
      <h1>SimpleList</h1>
      <userContext.Provider value={{user, setUser}}>
        <Outlet />
      </userContext.Provider>
    </div>
  )
}

