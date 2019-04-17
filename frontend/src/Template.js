import React, { Component } from 'react';
import { Container } from 'semantic-ui-react';
// import styled from 'styled-components';

import Header from './Heading';
import SearchBar from './SearchBar';
import WordList from './WordList';

class Template extends Component {
  render() {
    return (
      <Container>
        <Header />
        <SearchBar />
        <WordList />
      </Container>
    );
  }
}

export default Template;