import React, { Component, Fragment } from 'react';
import { Grid } from 'semantic-ui-react';
// import styled from 'styled-components';

import Heading from './Heading';
import SearchBar from './SearchBar';
import WordList from './WordList';

class Template extends Component {
  render() {
    return (
      <Fragment>
        <Heading/>
        <Grid centered columns={2}>
          <SearchBar/>
        </Grid>
        <Grid centered columns={3}>
          <WordList />
        </Grid>
      </Fragment>
    );
  }
}

export default Template;