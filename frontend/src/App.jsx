import React from "react";
import Landing from "./pages/landing";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/navbar";
import Register from "./pages/register";
import SchoolRegister from "./pages/schoolregister";
import SignIn from "./pages/signin";
import Home from "./pages/home";
import ReportCard from "./pages/reportcard";
import Grades from "./pages/grades";
import Clubs from "./pages/clubs";
import "./App.css"

const AppLayout = () => (
  <>
    <NavBar />
    <main className="main-content">
      <Outlet />
    </main>
  </>           nihmfgd
);
function App() {
  return (
    <Router>
      <Navbar />
      <main className="main-content">
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/register" element={<Register />} />
          <Route path="/schoolregister" element={<SchoolRegister />} />
          <Route path="/sign-in" element={<SignIn />} />
          <Route path="/home" element={<Home />} />
          <Route path="/reportcard" element={<ReportCard />} />
          <Route path="/grades" element={<Grades />} />
          <Route path="/clubs" element={<Clubs />} />
        </Routes>
      </main>
    </Router>
  );
}

export default App;
