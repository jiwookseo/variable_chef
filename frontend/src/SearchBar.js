import React from 'react';
import { Button, Select, Input } from 'semantic-ui-react';
// import styled from 'styled-components';
// import theme from './theme';

const options = [
  { key: '1', text: 'Python', value: 'python' },
  { key: '2', text: 'JavaScript', value: 'javascript' },
]

const SearchBar = () => {
  return (
    <Input>
      <input />
      <Select compact options={options} defaultValue='python'></Select>
      <Button type='submit' color='olive'>Cook</Button>
    </Input>
  );
};

export default SearchBar;