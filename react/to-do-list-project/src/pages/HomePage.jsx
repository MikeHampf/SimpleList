import { useNavigate } from "react-router-dom"

export default function HomePage(){
    const navigate = useNavigate()
    return (
        <div id="homepage">
        <h2>SimpleList: the simplest way to a simple list</h2>
        <div className="card">
          <button onClick={()=>navigate("signup")}>SIGN UP!</button>
          <button onClick={()=>navigate("login")}>LOGIN!</button>
        </div>
      </div>
    )
}