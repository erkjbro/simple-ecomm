import { StrictMode } from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import * as ReactDOM from 'react-dom/client';

import App from './App';
import './index.css';

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement,
);

root.render(
  <StrictMode>
    <Router>
      <App />
    </Router>
  </StrictMode>
);
