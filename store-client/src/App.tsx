import React, { useEffect } from 'react';
import { Routes, Route } from 'react-router-dom';

import * as Pages from './pages';
import { Navbar } from './components';
import './App.css';

const App: React.FC = () => {
  useEffect(() => {
    console.log('App mounted');
    document.title = 'SEP (tm)';
  }, []);

  const routes = (
    <Routes>
      <Route path="/details" element={<Pages.ProductDetails />} />
      <Route path="/listing" element={<Pages.ProductListing />} />
      <Route path="*" element={<Pages.Home />} />
    </Routes>
  );

  return (
    <div className="App">
      <header>
        <Navbar />
      </header>
      <main>
        {routes}
      </main>
    </div>
  );
};

export default App;
