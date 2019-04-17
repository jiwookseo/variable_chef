import React, { Component, Fragment } from 'react';
import { Grid } from 'semantic-ui-react';
// import styled from 'styled-components';

import Heading from './Heading';
import SearchBar from './SearchBar';
import WordList from './WordList';

class Template extends Component {
  constructor(props) {
    super(props)
    this.state = {
      value: '',
      lang: '',
    }
    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleSubmit = this.handlSubmit.bind(this);
  }

  handleInputChange(e) {

  }

  handleSubmit() {

  }

  render() {
    return (
      <Fragment>
        <Heading/>
        <Grid centered columns={2}>
          <SearchBar 
            value={value}
            onChange={this.handleInputChange}
            onSubmit={this.handleSubmit}
          />
        </Grid>
        <Grid centered columns={3}>
          <WordList />
        </Grid>
      </Fragment>
    );
  }
}

export default Template;