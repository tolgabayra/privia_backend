import { useSelector } from "react-redux";
import { useRoutes } from "react-router-dom";
import Feed from "./pages/Feed";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";




const ProtectedRoute = () => {
  const user = useSelector((state)=> state.auth.user)
  if (!user) {
    return <Login />
  }
  return <Feed />
}



export default function Routes(){
    return useRoutes([
        {
            path: "/",
            element: <Home />
        },
        {
            path: "/login",
            element: <Login />
        },
        {
            path: "/register",
            element: <Register />
        },
        {
            path: "/feed",
            element: <ProtectedRoute />,
            children: [
                {path: "", element: <Feed />}
            ]
        }
    ])
}