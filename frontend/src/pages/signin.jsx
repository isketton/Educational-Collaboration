import React, { useState } from "react";
import "../styles/signin.css"
import {
  useQuery,
  useMutation,
  useQueryClient,
  QueryClient,
  QueryClientProvider,
} from '@tanstack/react-query'
import axios from "axios"
/*
async function fetchUser(email, password) {
  const response = await fetch('/user/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json'},
    body: JSON.stringify({email, password}),
  });
  
  if (!response.ok) {
    throw new Error('Login failed');
  }

  return await response.json();
}
*/
export default function SignIn() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();

    const body = {
      username,
      password,
    };
    try {
      const response = await axios.post('http://localhost:8001/schoolapp/login/', body,{
        withCredentials: true
      });
      console.log("Login successful:", response.data);
      
    }
    catch {
      console.error("Login failed:", error);
    }
  }

  return (
    <div className="box">
      <div className="box_header">
        <h2> Sign In </h2>
      </div>
      <div className="box_content">
        <form onSubmit={handleSubmit}>
          <label htmlFor="username">Username</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
            />
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <button type="submit">Sign In</button>
        </form>
      </div>
    </div>
  )
}