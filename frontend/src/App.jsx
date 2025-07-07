import { useState } from 'react'

function App() {
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")
  const [message, setMessage] = useState("")
  const [userRole, setUserRole] = useState(null)
  const [loggedInUser, setLoggedInUser] = useState("")

  const handleLogin = async () => {
    const token = btoa(`${username}:${password}`)
    try {
      const response = await fetch("http://127.0.0.1:8000/api/v1/protected", {
        headers: {
          "Authorization": `Basic ${token}`
        }
      })

      if (!response.ok) throw new Error("Unauthorized")

      const data = await response.json()
      console.log("DATA FROM BACKEND:", data)
      setMessage(data.message)
      setUserRole(data.role)
      setLoggedInUser(username)
    } catch (error) {
      console.error("Login failed:", error)
      setMessage("Wrong credentials or server error")
    }
  }

  // Якщо залогінений
  if (userRole) {
    return (
      <div style={{ padding: "2rem" }}>
        <h1>Welcome, {loggedInUser}!</h1>
        <p>{message}</p>
        {userRole === "picker" && (
          <div>
            <button onClick={() => alert("Заказ взято!")}>Взяти заказ</button>
          </div>
        )}
        {userRole === "admin" && (
          <div>
            <button onClick={() => alert("Показуємо товари...")}>Переглянути товари</button>
            <button onClick={() => alert("Створюємо товар...")}>Додати товар</button>
            <button onClick={() => alert("Переглядаємо замовлення...")}>Переглянути замовлення</button>
          </div>
        )}
      </div>
    )
  }

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Login</h1>
      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={e => setUsername(e.target.value)}
      /><br /><br />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={e => setPassword(e.target.value)}
      /><br /><br />
      <button onClick={handleLogin}>Login</button>

      {message && <p>{message}</p>}
    </div>
  )
}

export default App
