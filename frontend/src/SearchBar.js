import React, { Fragment } from 'react';
import { Button, Select, Input } from 'semantic-ui-react';
// import styled from 'styled-components';
// import theme from './theme';

const options = [
  { key: '1', text: 'Python', value: 'python' },
  { key: '2', text: 'JavaScript', value: 'javascript' },
]

const SearchBar = () => {
  return (
    <Fragment style={{ marginBottom: '3em' }}>
    <Input>
      <Select compact options={options} defaultValue='python'></Select>
      <input />
      <Button type='submit' inverted color='green'>Cook</Button>
    </Input>
    </Fragment>
  );
};

export default SearchBar;