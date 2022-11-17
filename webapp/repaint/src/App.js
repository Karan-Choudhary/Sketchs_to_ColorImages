
import './App.css';
import Header from './components/Header';
import { MainContent } from './components/MainContent';
import { Preview } from './components/Preview';
import { Output } from './components/Output';
import React, {useState} from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route
} from "react-router-dom";

function App() {

  const [ImagesNames, setImagesNames] = useState([]);

  const [resultImages, setResultImages] = useState([]);



  // console.log(ImagesNames);


  return (
    <>
      <Router>
      <Header title="Sketch To Color Images"/>
      <Routes>
          <Route exact path="/" element={
            <>
            <MainContent setImagesNames={setImagesNames}/>
            </>
          }>
          </Route>

          <Route exact path="/Preview" element={
            <>
            <Preview ImagesNames={ImagesNames} setResultImages={setResultImages} />
            </>
          }>
          </Route>

          <Route exact path="/Output" element={
            <>
            <Output resultImages={resultImages}/>
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
