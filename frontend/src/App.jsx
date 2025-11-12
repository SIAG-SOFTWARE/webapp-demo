import React, { useState } from "react";
import { login, getStats } from "./api";

export default function App(){
  const [user, setUser] = useState("");
  const [pw, setPw] = useState("");
  const [token, setToken] = useState("");
  const [stats, setStats] = useState(null);
  const [err, setErr] = useState("");

  async function handleLogin(e){
    e.preventDefault();
    setErr("");
    try {
      const { access_token } = await login(user, pw);
      setToken(access_token);
      const data = await getStats(access_token);
      setStats(data);
    } catch (e) {
      setErr(e.message);
    }
  }

  return (
    <div style={{fontFamily:"sans-serif", padding:20}}>
      <h1>SIAG Webapp Demo</h1>
      {!token ? (
        <form onSubmit={handleLogin}>
          <div><input placeholder="username" value={user} onChange={e=>setUser(e.target.value)} /></div>
          <div><input placeholder="password" type="password" value={pw} onChange={e=>setPw(e.target.value)} /></div>
          <button type="submit">Login</button>
        </form>
      ) : (
        <div>
          <h3>Welcome</h3>
          <pre>{JSON.stringify(stats, null, 2)}</pre>
        </div>
      )}
      {err && <p style={{color:"red"}}>{err}</p>}
    </div>
  );
}
