import React, { Component } from 'react';
import Template from './Template';
import { GlobalStyle } from './global-styles';

class App extends Component {
  render() {
    return (
      <div className="App">
        <GlobalStyle />
        <Template />
      </div>
    );
  }
}

export default App;
