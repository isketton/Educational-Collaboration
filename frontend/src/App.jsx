import React from "react";
import Landing from "./pages/landing";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Outlet } from 'react-router-dom'
import Navbar from "./components/navbar";
import HomeNavbar from "./components/homenavbar";
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
    <Navbar />
    <main className="main-content">
      <Outlet />
    </main>
  </>         
);

const HomeLayout = () => (
  <>
    <HomeNavbar />
    <main className="main-content">
      <Outlet />
    </main>
  </> 
);
function App() {
  return (
    <Router>
        <Routes>
          <Route element={<AppLayout/>}>
            <Route path="/" element={<Landing />} />
          </Route>
          <Route path="/register" element={<Register />} />
          <Route path="/schoolregister" element={<SchoolRegister />} />
          <Route element={<HomeLayout/>}>
            <Route path="/sign-in" element={<SignIn />} />
            <Route path="/reports" element={<ReportCard />} />
            <Route path="/grades" element={<Grades />} />
          </Route>
          <Route path="/home" element={<Home />} />
          <Route path="/grades" element={<Grades />} />
          <Route path="/clubs" element={<Clubs />} />
        </Routes>
    </Router>
  );
}

export default App;
