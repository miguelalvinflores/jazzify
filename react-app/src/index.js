import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
// import Palette from 'react-palette';
import './index.css';
import App from './App';
import configureStore from './store';

const store = configureStore();

ReactDOM.render(
  <React.StrictMode>
      <Provider store={store}>
        <App
        // Palette={
        //   <Palette src={IMAGE_URL}>
        //     {({ data, loading, error }) => (
        //       <div style={{ color: data.vibrant }}>
        //         Text with the vibrant color
        //       </div>
        //     )}
        //   </Palette>
        // }
        />
      </Provider>

  </React.StrictMode>,
  document.getElementById('root')
);
