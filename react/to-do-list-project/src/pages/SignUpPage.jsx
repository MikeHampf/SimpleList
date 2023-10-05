export default function SignUpPage(){
    return (
        <div className="signup">
            <h1>SignUP</h1>
            <input className="name" 
                    placeholder="Name" 
                    type="text"></input>
            <input className="email" 
                    placeholder="Email *REQUIRED"
                    type="text"></input>
            <input className="password" 
                    placeholder="Password *REQUIRED"
                    type="text"></input>
            <button>SignUP AND START LISTING</button>
        </div>
    )
}