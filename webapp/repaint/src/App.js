
import './App.css';
import Header from './components/Header';
import { MainContent } from './components/MainContent';
import { Preview } from './components/Preview';
import { Loading } from './components/Loading';
import { Output } from './components/Output';
import React from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route
} from "react-router-dom";

function App() {

  const imgs = ['asdfghjkl','lkjhgfdsa','qwertyuiop','poiuytrewq'];

  return (
    <>
      <Router>
      <Header title="Sketch To Color Images"/>
      <Routes>
          <Route exact path="/" element={
            <>
            {/* <MainContent /> */}
            {/* <Preview imgArray={imgs} /> */}
            {/* <Loading/> */}
            <Output/>
            </>
          }>
          </Route>
        </Routes>
      {/* <Footer/> */}
    </Router>
    </>
  );
}

export default App;
