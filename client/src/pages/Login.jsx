import React from 'react'
import { useState } from 'react'
import { appAxios } from "../utils/appAxios"


export default function Login() {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")


  const submitLogin = () => {
    appAxios.post("/auth/login",{
      username,
      password
    },{withCredentials: true})
    .then((res) => {
      console.log(res);
    })
    .catch(err=>{

    })
  }



  return (
    <div>
      <div className="flex h-screen bg-indigo-700">
        <div className="w-full max-w-xs m-auto bg-indigo-100 rounded p-5">
          <header>
            <img className="w-20 mx-auto mb-5" src="https://img.icons8.com/fluent/344/year-of-tiger.png" />
          </header>
          <div>
            <div>
              <label className="block mb-2 text-indigo-500" for="username">Username</label>
              <input onChange={(e)=>setUsername(e.target.value)} className="w-full p-2 mb-6 text-indigo-700 border-b-2 border-indigo-500 outline-none focus:bg-gray-300" type="text" name="username" />
            </div>
            <div>
              <label className="block mb-2 text-indigo-500" for="password">Password</label>
              <input onChange={(e)=>setPassword(e.target.value)}  className="w-full p-2 mb-6 text-indigo-700 border-b-2 border-indigo-500 outline-none focus:bg-gray-300" type="password" name="password" />
            </div>
            <div>
              <button onClick={submitLogin} className="w-full bg-indigo-700 hover:bg-indigo-800 text-white font-bold py-2 px-4 mb-6 rounded" type="submit" >Log In</button>
            </div>
          </div>

        </div>
      </div>
    </div>
  )
}
